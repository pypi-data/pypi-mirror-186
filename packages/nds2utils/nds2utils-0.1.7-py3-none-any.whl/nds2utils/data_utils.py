"""
Library for useful python functions for acquiring data via nds2,
and for taking power spectral densities and transfer functions.

To be able to acquire LIGO data, users must run:

$ kinit albert.einstein@LIGO.ORG

Craig Cahillane
Nov 3, 2019
"""

import copy
import os
import pickle
import signal
import sys
import time
import gpstime

try:
    import warnings

    import deepdish
    from tables import NaturalNameWarning

    warnings.filterwarnings("ignore", category=NaturalNameWarning)
except ModuleNotFoundError:
    print("\033[91m")
    print("ModuleNotFoundError", end="")
    print("\033[0m", end="")
    print(": No module named 'deepdish'")
    print()
    print("Skipping this import and continuing.")

import nds2
import numpy as np
import scipy.constants as scc
import scipy.integrate as sciint
import scipy.signal as sig
from scipy.optimize import fsolve


# dB conversions
def db_to_mag(db):
    """Takes in number in dB, returns magnitude = 10^(dB/20)"""
    return 10 ** (db / 20.0)


def mag_to_db(mag):
    """Takes in number in magnitude, returns in dB = 20*log10(mag)"""
    return 20.0 * np.log10(mag)


# Complex Algebra
def complex_pole_pair(qq, f0):
    """Takes in Q and f0 (center frequency in Hz) and returns a complex pole pair"""
    f0_2 = f0**2
    real = 0.5 / qq
    imag = np.sqrt(f0_2 - real**2)
    poles = np.array([real + 1j * imag, real - 1j * imag])
    return poles


### .pkl file save and load
def save_pickle(data_dict, savefile):
    """Saves a .pkl file from the data_dict input at savefile."""
    with open(savefile, "wb") as outfile:
        pickle.dump(data_dict, outfile)
    return


def load_pickle(savefile):
    """Load a pickle file."""
    with open(savefile, "rb") as infile:
        data_dict = pickle.load(infile)
    return data_dict


### .hdf5 file save and load using deepdish
def save_hdf5(data_dict, savefile):
    """Saves a .hdf5 file using deepdish,
    use blosc compression to greatly enhance speed"""
    deepdish.io.save(savefile, data_dict, compression="blosc")
    return


def load_hdf5(loadfile, group=None):
    """Loads an hdf5 file using deepdish"""
    if not group:
        data_dict = deepdish.io.load(loadfile)
    else:
        data_dict = deepdish.io.load(loadfile, group=group)

    return data_dict


# FFT parameters
def dtt_time(averages, bandwidth, overlap, verbose=False):
    """
    Takes in number of averages, bandwidth, overlap of a FFT.
    Returns and prints the amount of data time in seconds the FFT will need.
    """
    if overlap > 1.0:  # overlap is in percent
        overlap = overlap / 100.0
    if verbose:
        print("Averages = {}".format(averages))
        print("Bandwidth = {} Hz".format(bandwidth))
        print("Overlap = {} %".format(overlap * 100.0))

    duration = (1 + (averages - 1) * (1 - overlap)) / bandwidth
    if verbose:
        print("\033[93m Total DTT Spectrum Time = {} seconds \033[0m".format(duration))
        print(
            "\033[91m Total DTT Spectrum Time = {} minutes \033[0m".format(
                duration / 60.0
            )
        )
    return duration


def dtt_averages(duration, bandwidth, overlap, verbose=False):
    """Takes in duration of clean data, bandwidth, overlap of a DTT template.
    Returns and prints the number of averages we can compute using this data.

    Inputs:
    -------
    duration: float
        total time of the data in seconds
    bandwidth: float
        FFT frequency bin width desired in Hz
    overlap: float
        decimal between 0 and 1 (or percent, which will be divided by 100)
        by which the FFT windows should overlap.

    Output:
    -------
    averages: int
        number of averages that can fit into the length of data given
    """
    if overlap > 1.0:  # overlap is in percent
        overlap = overlap / 100.0
    if verbose:
        print("Time = {} s".format(duration))
        print("Bandwidth = {} Hz".format(bandwidth))
        print("Overlap = {} %".format(overlap * 100.0))

    averages = (duration * bandwidth - 1) / (1 - overlap) + 1
    if verbose:
        print("\033[93m Averages = {} \033[0m".format(averages))

    if not averages == int(averages):
        print(
            "\033[93m"
            + "WARNING"
            + "\033[0m"
            + f": averages = {averages} is not possible to compute."
        )
        print(f"         Returning {int(averages)} instead.")

    averages = int(averages)
    return averages


def minimum_coherent_power(averages, overlap):
    """Given the number of averages taken and the overlap between FFTs,
    returns the expected value of the minimum measureable coherent power between two signals.

    In other words, if you compute the coherence between two completely uncorrelated signals a and b,
    then the coherence function <a,b><b,a>/<a,a><b,b> will return values around this number.
    A measured coherence considerably above this number can be considered resolved.

    This is equal to 1/(averages * (1 - overlap))
    In reality, we will see an extremely noisy curve
    """
    if overlap > 1.0:  # overlap is in percent
        overlap = overlap / 100.0
    if overlap < 0.0 or overlap > 1.0:  # if overlap is still not in range
        print("overlap is not valid, must be between 0 and 100 percent, or 0 and 1.")
        print("overlap = {} %".format(overlap * 100.0))
        return

    min_expected_coherent_power = 1.0 / (averages * (1 - overlap))
    return min_expected_coherent_power


def convert_density_to_std(psd, fs):
    """Takes in a white noise power spectral density in V**2/Hz
    and sampling frequency fs in Hz,
    and returns the Guassian standard deviation in V.
    Needed to input into np.random.normal(scale=noise_std)
    to generate the noise time series.

    Input:
    ------
    psd: float
        power spectral density level desired in V**2/Hz
    fs: int
        sampling frequency in Hertz

    Output:
    -------
    noise_amplitude: float
        Guassian standard deviation in V
    """
    noise_power = psd * fs / 2
    noise_amplitude = np.sqrt(noise_power)
    return noise_amplitude


###   Signal processing convenience functions   ###
# Time series
def apply_zpk_to_time_series(data, zeros_Hz, poles_Hz, gain_Hz, fs):
    """Accepts some time series data and a zpk filter defined in (positive) Hz,
    and applies that filter to the data and returns the resulting data.

    Inputs:
    -------
    data: 1d array of floats
        time series data as input to the filter
    zeros_Hz: 1d array of floats
        zeros of the filter in Hz
    poles_Hz: 1d array of floats
        poles of the filter in Hz
    gain_Hz: float
        gain of the filter
    fs: int
        sampling frequency in Hz

    Output:
    -------
    filtered_data: 1d array of floats
        time series data output from the filter

    Example:
    total_time = 5 # seconds
    fs = 2**14 # Hz
    noise_psd = 1e-3 # V**2/Hz

    xx = np.random.normal(scale=np.sqrt(noise_psd*fs/2), size=total_time*fs)
    yy = apply_zpk_to_time_series(xx, [], np.array([400.0]), 1.0, fs)
    """
    # zpk in rad/s
    zeros_rads = -2 * np.pi * zeros_Hz  # rad/s
    poles_rads = -2 * np.pi * poles_Hz  # rad/s
    gain_rads = gain_Hz * np.abs(np.prod(poles_rads) / np.prod(zeros_rads))

    # zpk in units of z-plane normalized frequency
    zeros_n, poles_n, gain_n = sig.bilinear_zpk(zeros_rads, poles_rads, gain_rads, fs)

    # Apply zpk filter to xx data to produce filtered yy data
    sos = sig.zpk2sos(zeros_n, poles_n, gain_n)

    zi = sig.sosfilt_zi(sos)
    filtered_data, _ = sig.sosfilt(sos, data, zi=zi * data[0])

    return filtered_data


def apply_sos_to_time_series(data, sos):
    """Accepts some time series data and a second-order sections filter,
    and applies that filter to the data and returns the resulting data.

    Inputs:
    -------
    data: 1d array of floats
        time series data as input to the filter
    sos: multi-dimensional array of floats
        second-order sections like (n_sections, 6)
    fs: int
        sampling frequency in Hz

    Output:
    -------
    filtered_data: 1d array of floats
        time series data output from the filter
    """

    zi = sig.sosfilt_zi(sos)
    filtered_data, _ = sig.sosfilt(sos, data, zi=zi * data[0])

    return filtered_data


# Transfer function from ZPK
def get_transfer_function_from_zpk(ff, zeros_Hz, poles_Hz, gain_Hz):
    """Accepts a zpk in Hz,
    returns the (analog) transfer function of that filter.


    Inputs:
    -------
    ff: 1d array of floats
        frequency vector in Hz
    zeros_Hz: 1d array of floats
        zeros of the filter in Hz
    poles_Hz: 1d array of floats
        poles of the filter in Hz
    gain_Hz: float
        DC gain of the filter

    Output:
    -------
    tf: 1d array of complex floats
        transfer function of zpk filter
    """
    # zpk in rad/s
    zeros_rads = -2 * np.pi * zeros_Hz  # rad/s
    poles_rads = -2 * np.pi * poles_Hz  # rad/s
    gain_rads = gain_Hz * np.abs(np.prod(poles_rads) / np.prod(zeros_rads))

    ## Analog
    ww = 2 * np.pi * ff  # rad/s
    _, hh = sig.freqs_zpk(zeros_rads, poles_rads, gain_rads, worN=ww)

    return hh

# nds2 server selection
def select_server(channels, gps_start):
    """Do some logic to select the server:port combo best for retrieving data
    """

    # are we on a CDS machine?
    if "NDSSERVER" in os.environ:
        on_cds_machine = True
    else:
        on_cds_machine = False

    # choose our NDS host
    gps_now = int(gpstime.gpsnow())

    # if on CDS and data is less than 28 days old
    if on_cds_machine and gps_now - gps_start < 3600 * 24 * 28:
        server = "h1daqnds0"
        port = 8088
        allow_data_on_tape = "False"
    else:
        all_chans_in_h1 = np.all(["H1:" in chan for chan in channels])
        if all_chans_in_h1:
            server = "nds.ligo-wa.caltech.edu"
            port = 31200
            allow_data_on_tape = "True"
        elif np.all(["L1:" in chan for chan in channels]):
            server = "nds.ligo-la.caltech.edu"
            port = 31200
            allow_data_on_tape = "True"
        else:
            server = "nds.ligo.caltech.edu"
            port = 31200
            allow_data_on_tape = "True"
    return server, port, allow_data_on_tape

def select_port_given_server(server):
    """Returns the port associated with a server
    """
    if server == "h1daqnds0":
        port = 8088
    elif server == "h1daqnds1":
        port = 8088
    elif server == "nds.ligo-wa.caltech.edu":
        port = 31200
    elif server == "nds.ligo-la.caltech.edu":
        port = 31200
    elif server == "nds.ligo.caltech.edu":
        port = 31200
    return port


# nds2 data acquistion/storage/manipulation
def find_channels(
    channel_glob="*",
    channel_type=None,
    data_type=None,
    min_sample_rate=0.0,
    max_sample_rate=999999995904.0,
    timespan=None,
    host_server="nds.ligo-wa.caltech.edu",
    port_number=31200,
    allow_data_on_tape="False",
    gap_handler="STATIC_HANDLER_NAN",
    verbose=True,
):
    """
    Use nds2 to find channels available in LIGO data.

    Inputs:
    channel_glob       -- A bash link glob pattern used to match channel names. Default is '*'.
    channel_type       -- str. Choose channels types to limit the search to.
                               Acceptable strings are any one of the following:
                               'UNKNOWN', 'ONLINE', 'RAW', 'RDS', 'STREND', 'MTREND', 'TEST_POINT', 'STATIC'
    data_type          -- str. Choose data types to limit the search to.
                               Acceptable strings are any one of the following:
                               'UNKNOWN', 'INT16', 'INT32', 'INT64', 'FLOAT32', 'FLOAT64', 'COMPLEX32', 'UINT32'
    min_sample_rate    -- A minimum sample rate to search for.
    max_sample_rate    -- A maximum sample rate to search for.
    timespan           -- Optional time span to limit available channel search to.  This may be an nds2.epoch or a tuple of [start, stop) times.
    host_server        -- str. Valid nds2 server.  Default is `nds.ligo-wa.caltech.edu`
    port_number        -- int. Valid port from which to access the server.  Default is 31200
    allow_data_on_tape -- str. String should be `True` or `False`.  Set to `True` if need really old data, is slower.
    gap_handler        -- str.  Defines how gaps in the data should be handled by nds2.  String default is 'STATIC_HANDLER_NAN'.
                          Usual nds2 default is 'ABORT_HANDLER', which kills your request if there's any unavailable data.
                          More info at https://www.lsc-group.phys.uwm.edu/daswg/projects/nds-client/doc/manual/ch04s02.html.
    verbose            -- bool.  Automatically displays available channels.  Displays ",m-trend" on minute trend channels.   Default is True.

    Output:
    buffers = buffers native to nds2 (indexed with numbers), with no data

    Valid Host Sever:Port Number combos:
    h1nds1:8088                   # only good on LHO CDS computers
    h1nds0:8088                   # only good on LHO CDS computers
    nds.ligo-wa.caltech.edu:31200 # LHO frame cache
    nds.ligo-la.caltech.edu:31200 # LLO frame cache
    nds.ligo.caltech.edu:31200    # Caltech frame cache

    ### Examples ###
    # Get DQed Hanford DARM channel names
    find_channels('H1:LSC-DARM_*DQ')

    # Get only 'online' channels which can be streamed using stitch_real_time_data()
    find_channels('H1:CAL-DELTAL*DQ', channel_type='ONLINE')

    # Get DQed Livingston DARM channel names
    find_channels('L1:LSC-DARM_*DQ', host_server='nds.ligo-la.caltech.edu')

    # Get Hanford ITMY ISI stuff, including second and minute trend
    find_channels('H1:ISI-GND_STS_ITMY_Y_*')

    # Get Hanford ITMY ISI stuff, only the minute trends
    find_channels('H1:ISI-GND_STS_ITMY_Y_*', channel_type='MTREND')
    """

    if channel_type == None:
        channel_type_mask = 127  # accept all channels
    elif channel_type == "UNKNOWN":
        channel_type_mask = 0
    elif channel_type == "ONLINE":
        channel_type_mask = 1
    elif channel_type == "RAW":
        channel_type_mask = 2
    elif channel_type == "RDS":
        channel_type_mask = 4
    elif channel_type == "STREND":
        channel_type_mask = 8
    elif channel_type == "MTREND":
        channel_type_mask = 16
    elif channel_type == "TEST_POINT":
        channel_type_mask = 32
    elif channel_type == "STATIC":
        channel_type_mask = 64
    else:
        print(
            "\033[93m"
            + "WARNING: {channel_type} is not a valid channel type".format(
                channel_type=channel_type
            )
            + "\033[0m"
        )
        print("Continuing with no mask")
        print()

    if data_type == None:
        data_type_mask = 127  # accept all channels
    elif data_type == "UNKNOWN":
        data_type_mask = 0
    elif data_type == "INT16":
        data_type_mask = 1
    elif data_type == "INT32":
        data_type_mask = 2
    elif data_type == "INT64":
        data_type_mask = 4
    elif data_type == "FLOAT32":
        data_type_mask = 8
    elif data_type == "FLOAT64":
        data_type_mask = 16
    elif data_type == "COMPLEX32":
        data_type_mask = 32
    elif data_type == "UINT32":
        data_type_mask = 64
    else:
        print(
            "\033[93m"
            + "WARNING: {data_type} is not a valid channel type".format(
                data_type=data_type
            )
            + "\033[0m"
        )
        print("Continuing with no mask")
        print()

    params = nds2.parameters(host_server, port_number)
    params.set("ALLOW_DATA_ON_TAPE", allow_data_on_tape)
    params.set("GAP_HANDLER", gap_handler)

    buffers = nds2.find_channels(
        channel_glob=channel_glob,
        channel_type_mask=channel_type_mask,
        data_type_mask=data_type_mask,
        min_sample_rate=min_sample_rate,
        max_sample_rate=max_sample_rate,
        timespan=timespan,
        params=params,
    )

    if verbose:
        if timespan:
            ts = "GPS {ts1}-{ts2}".format(ts1=timespan[0], ts2=timespan[1])
        else:
            ts = "GPS now"
        print("\033[92m")
        print(
            "Displaying channels that match {glob} on {hs}:{pn} for {ts}".format(
                glob=channel_glob, hs=host_server, pn=port_number, ts=ts
            )
        )
        print("\033[0m")
        try:
            first_buff = buffers[0]  # to trigger the IndexError

            if len(buffers) < 1000:
                max_name_length = 0
                for buff in buffers:
                    if max_name_length < len(buff.name):
                        max_name_length = len(buff.name)
            else:
                max_name_length = 60

            max_name_length += 8  # add 8 in case there are minute or second trends
            for buff in buffers:
                name = buff.name
                fs = buff.sample_rate
                name_long = buff.NameLong()
                suffix = ""
                suffix_type = ""
                if "STREND" in name_long:
                    suffix = ",s-trend"
                    suffix_type = "STREND"
                elif "MTREND" in name_long:
                    suffix = ",m-trend"
                    suffix_type = "MTREND"
                elif "RAW" in name_long:
                    suffix_type = "RAW"
                elif "ONLINE" in name_long:
                    suffix_type = "ONLINE"
                elif "TEST_POINT" in name_long:
                    suffix_type = "TEST_POINT"

                name = "{}{}".format(name, suffix)
                print(
                    "{name:{max_name_length}}    fs = {fs:6.0f} Hz    type = {suffix_type:6}".format(
                        name=name,
                        max_name_length=max_name_length,
                        suffix_type=suffix_type,
                        fs=fs,
                    )
                )
            print("\033[92m")
            print(
                "Displaying channels that match {glob} on {hs}:{pn} for {ts}".format(
                    glob=channel_glob, hs=host_server, pn=port_number, ts=ts
                )
            )
            print("\033[0m")

        except IndexError:
            print(
                "\033[93m"
                + "WARNING: No channels matching {glob} found on {hs}:{pn} for {ts}".format(
                    glob=channel_glob, hs=host_server, pn=port_number, ts=ts
                )
                + "\033[0m"
            )
            print()
        except RuntimeError:
            print(
                "\033[93m"
                + "RuntimeError: Failed to establish a connection[INFO: Error occurred trying to write to socket]"
                + "\033[0m"
            )
            print()
            print(
                "\033[93m" + "Did you run `kinit albert.einstein@LIGO.ORG`?" + "\033[0m"
            )
            print()
            print("\033[93m" + "Are your nds2 parameters set correctly?" + "\033[0m")
            print_nds2_params(params)

    return buffers


def check_channels_existance(
    channels,
    gps_start,
    gps_stop,
    host_server="nds.ligo-wa.caltech.edu",
    port_number=31200,
    allow_data_on_tape="False",
    gap_handler="STATIC_HANDLER_NAN",
):
    """Uses find_channels() to determine which channels exist in a list.
    Returns nothing, outputs
    Input:
    channels = list of channels
    """
    print()
    print(f"Checking existance of channel in list on {host_server}:{port_number} from GPS {gps_start} to {gps_stop}")
    for chan in channels:
        buf = find_channels(
            chan,
            timespan=(gps_start, gps_stop),
            host_server=host_server,
            port_number=port_number,
            allow_data_on_tape=allow_data_on_tape,
            gap_handler=gap_handler,
            verbose=False,
        )
        try:
            buf[0]
            print("\033[92m" + f'"{chan}" found' "\033[0m")
        except IndexError:
            print("\033[93m" + f'"{chan}" does not exist' "\033[0m")

    return


def print_nds2_params(params):
    """Print the nds2 parameters which govern data collection."""
    for prm in params.parameter_list():
        print(f"{prm} = {params.get(prm)}")
    return


def make_array_from_buffers(buffers):
    """
    Input:
    buffers = native nds2 buffers, like from the output of find_channels().
    Outputs:
    channel_names = np.array() with the channel names as elements
    """
    channel_names = np.array([])
    for buff in buffers:
        name = buff.name
        name_long = buff.NameLong()
        suffix = ""
        if "STREND" in name_long:
            suffix = ",s-trend"
        elif "MTREND" in name_long:
            suffix = ",m-trend"

        name = "{}{}".format(name, suffix)
        channel_names = np.append(channel_names, name)
    return channel_names


def acquire_data(
    channels,
    gps_start: int,
    gps_stop: int,
    host_server: str = None,
    port_number: int = None,
    allow_data_on_tape: str = "False",
    gap_handler: str = "STATIC_HANDLER_NAN",
    is_minute_trend: bool = False,
    return_nds2_buffers: bool = False,
):
    """
    Use python nds2 client to get LIGO data.

    Inputs:
    -------
    channels            = array of strs. Valid LIGO channels from which to fetch data
    gps_start           = int. Valid GPS time at which to start acquiring data
    gps_stop            = int. Valid GPS time at which to stop acquiring data
    host_server         = str. Valid nds2 server.  Default is `nds.ligo-wa.caltech.edu`
    port_number         = int. Valid port from which to access the server.  Default is 31200
    allow_data_on_tape  = str. String should be `True` or `False`.  Set to `True` if need really old data, is slower.
    gap_handler         = str.  Defines how gaps in the data should be handled by nds2.  String default is 'STATIC_HANDLER_NAN'.
                          Usual nds2 default is 'ABORT_HANDLER', which kills your request if there's any unavailable data.
                          More info at https://www.lsc-group.phys.uwm.edu/daswg/projects/nds-client/doc/manual/ch04s02.html.
    is_minute_trend     = bool.  If true, will adjust gps_times to align with minute trend boundaries.  Default is False.
    return_nds2_buffers = bool.  If true, will return the native nds2 buffers and not the usual data dictionary.  Default is False.

    Output:
    -------
    data_dict: dictionary
        python dictionary with the channel names as keys and the channel info and data as a value

    Valid Host Sever:Port Number combos:
    h1daqnds1:8088 # only good on LHO CDS computers
    h1daqnds0:8088
    nds.ligo-wa.caltech.edu:31200
    nds.ligo-la.caltech.edu:31200
    nds.ligo.caltech.edu:31200

    If you request minute trends of a channel by ending a channel name with ,m-trend
    this script will automatically adjust your gps_start and gps_stop times to align
    with the minute trend boundaries (basically the gpstimes must be divisible by 60)

    ### Examples ###

    # Get DARM error signal and control signal
    data_dict = acquire_data(['H1:LSC-DARM_IN1_DQ', 'H1:LSC-DARM_OUT_DQ'], 1256340013, 1256340167)

    # Get minute and second trends.  Beware of getting minute trends too close to the present, will return only nans
    data_dict = acquire_data(['H1:ISI-GND_STS_ITMY_Y_BLRMS_30M_100M.mean,m-trend',
                            'H1:ISI-GND_STS_ITMY_Y_BLRMS_30M_100M.mean,s-trend'],
                            1256340013,
                            1256340563)
    """
    # always intify the inputs
    gps_start = int(gps_start)
    gps_stop = int(np.ceil(gps_stop))

    # Check if ,m-trend is in any channel name
    if not is_minute_trend:
        for chan in channels:
            if ",m-trend" in chan:
                is_minute_trend = True
                break

    if is_minute_trend:
        new_gps_start = int(np.floor(gps_start / 60.0) * 60.0)
        new_gps_stop = int(np.ceil(gps_stop / 60.0) * 60.0)
        if not new_gps_start == gps_start or not new_gps_stop == gps_stop:
            print()
            print(
                "Adjusting gps_start and gps_stop times to align with minute trend boundaries:"
            )
            print("User Inputs:")
            print("gps_start = {}".format(gps_start))
            print("gps_stop  = {}".format(gps_stop))
            gps_start = int(new_gps_start)
            gps_stop = int(new_gps_stop)
            print("Adjusted GPS times:")
            print("gps_start = {}".format(gps_start))
            print("gps_stop  = {}".format(gps_stop))

    # If server or port is not selected, choose for the user
    if host_server is None:
        host_server, port_number, allow_data_on_tape = select_server(channels, gps_start)
    else:
        port_number = select_port_given_server(host_server)

    print()
    print(
        "Fetching data from {hs}:{pn} with GPS times {start} to {stop}".format(
            hs=host_server, pn=port_number, start=gps_start, stop=gps_stop
        )
    )
    print("from {channels}".format(channels=channels))
    try:
        params = nds2.parameters(host_server, port_number)
        params.set("ALLOW_DATA_ON_TAPE", allow_data_on_tape)
        params.set("GAP_HANDLER", gap_handler)
        buffers = nds2.fetch(channels, gps_start, gps_stop, params=params)
    except RuntimeError:
        print()
        print(
            "\033[93m"
            + "RuntimeError: Failed to establish a connection[INFO: Error occurred trying to write to socket]"
            + "\033[0m"
        )
        print()
        print("\033[93m" + "Did you run `kinit craig.cahillane@LIGO.ORG`?" + "\033[0m")
        print()
        print("\033[93m" + "Are your nds2 parameters set correctly?" + "\033[0m")
        print_nds2_params(params)
        print()
        print(
            "\033[93m"
            + "Checking if channels are valid with find_channels():"
            + "\033[0m"
        )
        check_channels_existance(
            channels,
            gps_start,
            gps_stop,
            host_server=host_server,
            port_number=port_number,
            allow_data_on_tape=allow_data_on_tape,
            gap_handler=gap_handler,
        )
        print("Exiting...")
        sys.exit(1)

    try:
        first_buff = buffers[0]
        print()
        for buff in buffers:
            number_of_nans = np.sum(np.isnan(buff.data))
            if number_of_nans > 0:
                print(
                    "\033[93m"
                    + "WARNING: channel {name} returned {nan} nans".format(
                        name=buff.name, nan=number_of_nans
                    )
                    + "\033[0m"
                )

    except IndexError:
        print()
        print(
            "\033[93m"
            + "WARNING: No channel buffers returned for {channels}".format(
                channels=channels
            )
            + "\033[0m"
        )
        print()

    if return_nds2_buffers:
        return buffers

    duration = gps_stop - gps_start
    data_dict = extract_dict(buffers, duration=duration)
    return data_dict


def stitch_real_time_data(
    channels,
    duration,
    host_server="nds.ligo-wa.caltech.edu",
    port_number=31200,
    verbose=True,
):
    """
    Stitches together data broadcast from nds2 in real time.
    Useful for recording data during injections.

    Inputs:
    channels           = array of strs. Valid LIGO channels from which to fetch data.
                         All channels must be an "ONLINE" channel type.
    duration           = length of time to record data in seconds.
                         This script will take this number of seconds as it records the data in real time.
    host_server        = str. Valid nds2 server.  Default is `nds.ligo-wa.caltech.edu`
    port_number        = int. Valid port from which to access the server.  Default is 31200
    verbose            = bool.  Prints helpful statements of what's happening.  Default is True.

    Output:
    Dictionary of dicts with the channel names as keys, and the data and sampling rate fs as values.

    "real time" for some servers is slower than others.
    For nds.ligo-wa.caltech.edu the latency is ~ 2 seconds.
    If on LHO CDS computers, h1nds1:8088 is the best host_server:port_number combo.

    Valid Host Sever:Port Number combos:
    h1nds1:8088 # only good on LHO CDS computers
    h1nds0:8088
    nds.ligo-wa.caltech.edu:31200
    nds.ligo-la.caltech.edu:31200
    nds.ligo.caltech.edu:31200

    ### Example ###

    """
    data_dict = {}
    time_elapsed = 0
    skip_seconds = 2  # Because conn.iterate takes some time to make a true connection with the channel on h1nds1.  Needs at least two seconds.
    skipped = False
    duration_ceiling = int(np.ceil(duration))

    if verbose:
        print("Establish connection to {}:{}".format(host_server, port_number))

    try:
        conn = nds2.connection(host_server, port_number)
    except:
        print()
        print(
            "\033[91m"
            + "Failed to establish connection to {}:{}".format(host_server, port_number)
            + "\033[0m"
        )
        print("Did you run kinit albert.einstein@LIGO.ORG ?")
        print("Are your host_server and port_number valid?")
        print()
        sys.exit(0)

    # Set up Ctrl+C handling
    def free_testpoints():
        """Function to be called when Ctrl+C is pressed during stitch_real_time_data().
        This will close the connection to nds2 used for iteration.
        Sleep for a second afterward to make sure the connection closes.
        """
        print()
        print("Closing nds2 connection")
        conn.close()
        time.sleep(1)
        return

    def signal_handler(sig, frame):
        print("\033[91m")
        print("You pressed Ctrl+C!")
        print("\033[0m")
        print(
            f"Freeing testpoints and closing connection to nds2 server {host_server}:{port_number}"
        )
        free_testpoints()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    if verbose:
        print("Start gathering {} seconds of data!".format(duration_ceiling))

    repeating_warn_dict = {}
    for chan in channels:
        repeating_warn_dict[chan] = False

    for buff in conn.iterate(channels):
        time_elapsed += 1

        if (time_elapsed <= skip_seconds) and (
            skipped is False
        ):  # skip the first two seconds
            if verbose:
                print("Skipping next {} seconds".format(skip_seconds - time_elapsed))
            continue
        elif skipped is False:
            skipped = True
            time_elapsed = 0

        for ii in range(len(channels)):
            buffer = buff[ii]
            chan = buffer.name
            if not len(data_dict.keys()) == len(channels):
                data_dict[chan] = {}
                data_dict[chan]["fs"] = int(buffer.sample_rate)
                data_dict[chan]["gpsStart"] = buffer.gps_seconds
                data_dict[chan]["data"] = buffer.data
                if (
                    buffer.data[0] == 0.0
                ):  # if the data is identically 0, something is wrong
                    print()
                    print(
                        "\033[91m"
                        + "Data for {} is identically zero.  Continuing data acquisition.".format(
                            chan
                        )
                        + "\033[0m"
                    )
                    print()
                    # return 'ZerosError'
            else:
                if (
                    buffer.data[-1] == data_dict[chan]["data"][-1]
                    and not repeating_warn_dict[chan]
                ):  # if the data is repeating for some reason
                    repeating_warn_dict[chan] = True
                    print()
                    print(
                        "\033[91m"
                        + "Data for {} is repeating.  Continuing data acquisition.".format(
                            chan
                        )
                        + "\033[0m"
                    )
                    print()
                    # return 'ZerosError'

                data_dict[chan]["data"] = np.append(
                    data_dict[chan]["data"], buffer.data
                )

        sys.stdout.write("\r")
        sys.stdout.write(
            "{:d} seconds acquired / {:d} seconds total.".format(
                time_elapsed + 1, duration_ceiling
            )
        )
        sys.stdout.flush()
        if time_elapsed >= duration_ceiling - 1:
            break

    free_testpoints()

    for chan in data_dict.keys():
        data = data_dict[chan]["data"]
        fs = data_dict[chan]["fs"]

        nn = len(data)
        total_time = nn / fs
        fraction_time = duration / total_time
        cutoff_index = int(fraction_time * nn)

        good_data = data[:cutoff_index]
        data_dict[chan]["data"] = good_data
        data_dict[chan]["duration"] = duration

    return data_dict


def extract_dict(nds2_buffers, duration):
    """
    Creates the usual data dictionary from the output of nds2.fetch(),
    The dict keys are the channel names.
    """
    data_dict = {}
    for buffer in nds2_buffers:
        chan = buffer.name
        data_dict[chan] = {}
        data_dict[chan]["fs"] = buffer.sample_rate
        data_dict[chan]["gpsStart"] = buffer.gps_seconds
        data_dict[chan]["data"] = buffer.data
        data_dict[chan]["duration"] = duration

    for chan in data_dict.keys():
        data = data_dict[chan]["data"]
        fs = data_dict[chan]["fs"]

        nn = len(data)
        total_time = nn / fs
        fraction_time = duration / total_time
        cutoff_index = int(fraction_time * nn)

        good_data = data[:cutoff_index]
        data_dict[chan]["data"] = good_data

    return data_dict


def trim_dict(data_dict, duration):
    """Trims a dictionary with a long data stream down to a dictionary with a
    shorter data stream.  Good for taking fewer averages if some time is glitchy
    """
    for chan in data_dict.keys():
        data = data_dict[chan]["data"]
        fs = data_dict[chan]["fs"]

        nn = len(data)
        total_time = nn / fs
        fraction_time = duration / total_time
        cutoff_index = int(fraction_time * nn)

        good_data = data[:cutoff_index]

        data_dict[chan]["data"] = good_data

    return data_dict


def check_loaded_data_dict(data_dict, channels):
    """Check to make sure the loaded data_dict and the
    requested data_dict is not None,
    have the same channels, and do not have NaNs for data.

    Inputs:
    -------
    data_dict: nds2utils dictionary data structure
        dictionary containing the requested data and relevant info
    channels: list of strs
        list of channel names desired

    Output:
    -------
    loaded_data_dict_contains_requested_data_dict: bool
        True if data_dict has all the channels requested.
        False if data_dict does not have some requested channels.
    """
    loaded_data_dict_is_nonetype = False
    if not data_dict:
        print(f"data_dict = {data_dict}")
        loaded_data_dict_is_nonetype = True

    loaded_data_dict_contains_requested_data_dict = False
    loaded_data_dict_contains_nans = False
    if not loaded_data_dict_is_nonetype:
        if all(chan in data_dict for chan in channels):
            loaded_data_dict_contains_requested_data_dict = True
        else:
            print(f"data_dict does not contain all requested channels")

        for chan, temp_dict in data_dict.items():
            if np.isnan(temp_dict["data"][0]):
                print(f"data_dict contains NaNs")
                loaded_data_dict_contains_nans = True

    is_loaded_data_dict_acceptable = (
        not loaded_data_dict_is_nonetype
        and loaded_data_dict_contains_requested_data_dict
        and not loaded_data_dict_contains_nans
    )
    return is_loaded_data_dict_acceptable


def load_data_to_dict_directly(chan, data, fs, duration, gps_start=0, data_dict=None):
    """Creates a new entry to a data_dict structure,
    or if no data_dict is provided, creates a data_dict struture with the channel data provided.

    If data_dict[chan] already exists,
    this function will overwrite what's in data_dict[chan] with what's provided.

    Inputs:
    -------
    chan: str
        name of the data channel
    data: array of floats
        data to be uploaded
    fs: float
        sampling frequency in Hz
    gps_start: int
        GPS start time of the data
        Default is 0, just a default placeholder.
    duration: float
        total time of the data stream in seconds
    data_dict: dictionary
        data dictionary structure containing channel data.
        Default is None, will return a fresh data_dict containing the provided data in data_dict[chan]["data"]

    Output:
    -------
    data_dict: dictionary
        same data_dict structure that was input, but with additionary data and chan information
    """
    if not data_dict:
        data_dict = {}

    data_dict[chan] = {}
    data_dict[chan]["data"] = data
    data_dict[chan]["fs"] = fs
    data_dict[chan]["gpsStart"] = gps_start
    data_dict[chan]["duration"] = duration

    return data_dict


# calibrated the PSDs of the data_dict
def calibrate_chan(
    data_dict, chan, zeros=[], poles=[], gain=1.0, units="cts", apply_cal=True
):
    """
    Calibrates the PSD, CSD, and TF of the channel in data_dict using the zeros, poles, and gain.
    If Runs calibrate_dict().

    Inputs:
    -------
    data_dict  = data dictionary structure containing chan data
    chan      = str.    channel name we want to calibrate
    zeros     = list.   zeros associated with the calibration.  Default is []
    poles     = list.   poles associated with the calibration.  Default is []
    gain      = float.  gain associated with the calibration.  Default is 1.0
    units     = str.    units we are calibrating into.
    apply_cal = bool.   run calibrate_dict() on data_dict to immediately calibrate chan's PSD.  Default is True.

    Outputs:
    data_dict = same data_dict as before, but populated with the calibration.

    ### Example ###
    zeros = [ 30,  30,  30,  30,  30,  30]
    poles = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3]
    gain  = 1.0
    cal_data_dict = calibrate_chan(data_dict, 'H1:CAL-DELTAL_EXTERNAL_DQ', zeros, poles, gain )
    """
    cal_data_dict = copy.deepcopy(data_dict)

    def cal_func(fff):
        """Intermediate calibration as function of frequency"""
        return tf_zpk(fff, zeros, poles, gain)

    cal_data_dict[chan]["calFunc"] = cal_func
    cal_data_dict[chan]["calUnits"] = units

    if apply_cal:
        cal_data_dict = calibrate_dict(cal_data_dict)  # run the calibration

    return cal_data_dict


def calibrate_dict(data_dict, recalculate=False):
    '''Calibrates the data_dict based on the user-provided calibrations.

    Example Usage:
    data_dict['H1:CAL-DELTAL_EXTERNAL_DQ']['calFunc'] = DARMcalFunc
    data_dict['H1:CAL-DELTAL_EXTERNAL_DQ']['calUnits'] = "m"  # not necessary but good practice
    data_dict['H1:CAL-PCALY_RX_PD_OUT_DQ']['calFunc'] = PCALcalFunc
    data_dict['H1:CAL-PCALY_RX_PD_OUT_DQ']['calUnits'] = "m"  # not necessary but good practice
    data_dict = calibrate_dict(data_dict)

    Example calFunc:
    def myChanCalFunc(fff):
        """Scale myChan PSD by a factor of 3.7 with a pole at 12.34 Hz"""
        return tf_zpk(fff, [], [12.34], 3.7)
    # Use myChan calFunc
    data_dict[myChan]['calFunc'] = myChanCalFunc

    In the data_dict data structure, each key is a channel.
    Under each channel list of values, there is a keyword that this function looks for called "calFunc".
    "calFunc" stands for calibration function, which should take in a frequency vector only and return a calibrated transfer function only.
    If "calFunc" is defined for at least one channel, a new calibrated PSD is calculated and stored under "calPSD" for only that channel.
    If "calFunc" is defined for at least two channels, a new calibrated CSD and TF is calculated and stored under "calCSD" and "calTF" for only those channels.

    Returns a dictionary with calibrated PSDs, CSDs, and TFs for all channels with "calFunc" defined
    '''
    # Find channels with calibrations applied
    cal_channels = np.array([])
    channels = data_dict.keys()
    for chan in channels:
        if "calFunc" in data_dict[chan].keys():
            cal_channels = np.append(cal_channels, chan)

    # Apply those calibrations
    # PSDs
    for chan in cal_channels:
        ff_psd = data_dict[chan]["ff"]
        calFunc = data_dict[chan]["calFunc"]
        data_dict[chan]["calPSD"] = (
            data_dict[chan]["PSD"] * np.abs(calFunc(ff_psd)) ** 2
        )

    # CSDs
    for chan in cal_channels:
        for chan2 in cal_channels:
            if chan == chan2:
                continue

            # if we've already calculated the CSD, take it's complex conjugate and store it
            if chan in data_dict[chan2].keys() and not recalculate:
                if "calCSD" in data_dict[chan2][chan].keys():
                    data_dict[chan][chan2]["ff"] = data_dict[chan2][chan]["ff"]
                    data_dict[chan][chan2]["calCSD"] = np.conj(
                        data_dict[chan2][chan]["calCSD"]
                    )
                    data_dict[chan][chan2]["calTF"] = (
                        1.0 / data_dict[chan2][chan]["calTF"]
                    )
                    continue

            if chan2 in data_dict[chan].keys():
                if "CSD" in data_dict[chan][chan2].keys():
                    ff_csd = data_dict[chan][chan2]["ff"]
                    calFunc = data_dict[chan]["calFunc"]
                    calFunc2 = data_dict[chan2]["calFunc"]
                    # C_xy = <x*|y>
                    # coherence = |C_xy|^2/(P_xx P_yy) = (C_xy C_xy^*)/(P_xx P_yy)
                    # H = C_xy/P_xx = P_yy/C_xy^* (perfect coherence = 1)
                    # |H|^2 = P_xx/P_yy
                    # |H| = A_xx/A_yy
                    data_dict[chan][chan2]["calCSD"] = (
                        data_dict[chan][chan2]["CSD"]
                        * np.conj(calFunc(ff_csd))
                        * calFunc2(ff_csd)
                    )
                    data_dict[chan][chan2]["calTF"] = (
                        data_dict[chan][chan2]["TF"]
                        * calFunc(ff_csd)
                        / calFunc2(ff_csd)
                    )
    return data_dict


def check_sampling_frequency_vs_bandwidth(data_dict, bandwidth):
    """Takes in a data_dict, finds the lowest sampling frequency,
    and checks to make sure the bandwidth is an integer multiple of
    that sampling frequency.

    Inputs:
    -------
    data_dict: dictionary
        dict data structure with nds2 data
    bandwidth: float
        FFT binwidth in Hertz

    Output:
    -------
    bandwidth: float
        Usually will be the same bandwidth as input,
        but will be adjusted to fit perfectly into the
        requested minimum sampling frequency in the data_dict
    """
    min_fs = np.inf
    channels = data_dict.keys()
    for chan in channels:
        fs = data_dict[chan]["fs"]
        if fs < min_fs:
            min_fs = fs

    ratio = min_fs / bandwidth
    if not ratio == int(ratio):
        print(
            "\033[93m"
            + "WARNING"
            + "\033[0m"
            + f": requested bandwidth = {bandwidth} Hz is not compatible with lowest data sampling frequency = {min_fs} Hz"
        )
        print(f"         ratio = {min_fs}/{bandwidth} = {ratio}.")

        round_ratio = np.round(ratio)
        new_bandwidth = min_fs / round_ratio
        print(
            f"         Adjusting bandwidth to {new_bandwidth} Hz such that ratio is an integer."
        )

        bandwidth = new_bandwidth

    return bandwidth


def check_duration(data_dict, averages, bandwidth, overlap):
    """Checks the duration of the actual data_dict vs the user requested data length
    as calculated by their input averages, bandwidth, overlap.

    Inputs:
    -------
    data_dict: dictionary
        dict data structure with nds2 data
    averages: int
        number of PSDs to averages together from the data
    bandwidth: float
        FFT binwidth in Hertz
    overlap: float
        level of overlap between windows

    Output:
    -------
    duration: float
        either the user's requested duration of the dictionary,
        or the actual duration if the user's request is not possible
    """
    # Should be the same duration of data for all channels
    channels = data_dict.keys()
    for chan in channels:
        # if we have an old dictionary which did not save duration
        if not "duration" in data_dict[chan]:
            data = data_dict[chan]["data"]
            fs = data_dict[chan]["fs"]
            data_dict[chan]["duration"] = len(data) / fs

        actual_duration = data_dict[chan]["duration"]

    # duration implicitly specified by the user with their averages, bandwidth, overlap trio
    requested_duration = dtt_time(averages, bandwidth, overlap)

    # Some code dealing with bad duration requests from the user
    if not actual_duration == requested_duration:
        print(
            "\033[93m"
            + "WARNING"
            + "\033[0m"
            + f": actual duration of data = {actual_duration} seconds,"
        )
        print(
            f"         but requested duration via averages, bandwidth, and overlap is {requested_duration} seconds."
        )

        if requested_duration > actual_duration:
            print(f"         Using level of data available: {actual_duration} seconds.")
            duration = actual_duration

        else:
            print(f"         Truncating data to fulfill the user request.")
            duration = requested_duration
    else:
        duration = actual_duration

    return duration


# Decimate the data, if necessary for a CSD or TF
def decimate_data(data, starting_fs: int, final_fs: int, ftype="iir"):
    """
    Runs scipy.signal.decimate() on the provided data.
    For ease of use, use sampling rates which are factors of 2**n

    Inputs:
    -------
    data: array of floats
        data to be decimated
    starting_fs: int
        starting sampling frequency of the data
    final_fs: int
        final sampling frequency to decimate to

    Output:
    -------
    decimated_data: array of floats
        data decimated to final_fs sampling frequency
    """
    decimation_ratio = int(starting_fs // final_fs)

    if decimation_ratio < 1:
        print(f"Cannot decimate from {starting_fs} down to {final_fs}")
        return

    # Following the scipy.signal docs recommedations
    # if we have a large decimation ratio, break up the decimations into parts
    elif decimation_ratio > 8:
        temp_ratio = 1
        temp_data = data
        while not temp_ratio >= decimation_ratio:
            temp_data = sig.decimate(temp_data, 2, ftype=ftype)
            temp_ratio *= 2

        decimated_data = temp_data

    else:
        decimated_data = sig.decimate(data, decimation_ratio, ftype=ftype)

    return decimated_data


# Calculate the PSDs, CSDs, TFs, and coherences of the data_dict data
def calc_psd(
    data_dict, chan, averages, bandwidth, overlap, averaging="mean", window="hann"
):
    """
    Take PSD of single channel in data_dict.
    Returns a new data_dict, similar to the one provided.
    """
    # Run some check functions
    bandwidth = check_sampling_frequency_vs_bandwidth(data_dict, bandwidth)
    new_duration = check_duration(data_dict, averages, bandwidth, overlap)

    # Take PSDs
    # channels = data_dict.keys()
    # for chan in channels:
    data = data_dict[chan]["data"]
    fs = data_dict[chan]["fs"]
    duration = data_dict[chan]["duration"]

    # Some code dealing with bad duration requests from the user
    if not new_duration == duration:
        fraction_time = new_duration / duration
        cutoff_index = int(fraction_time * len(data))

        data = data[:cutoff_index]
        duration = new_duration

    # expanding the data according to the overlap value
    duration_effective = duration * averages / (1 + (averages - 1) * (1 - overlap))
    fft_time = duration_effective / averages
    nperseg = int(np.ceil(fft_time * fs))

    ff, Pxx = sig.welch(
        data, fs=fs, window=window, nperseg=nperseg, noverlap=overlap, average=averaging
    )
    data_dict[chan]["ff"] = ff
    data_dict[chan]["PSD"] = Pxx

    try:
        ff[1] - ff[0]
    except IndexError:
        print("IndexError, channel was likely all zeros, no sensible PSD taken")

    data_dict[chan]["df"] = ff[1] - ff[0]

    data_dict[chan]["averages"] = averages
    data_dict[chan]["binwidth"] = bandwidth
    data_dict[chan]["overlap"] = overlap
    data_dict[chan]["duration"] = duration
    data_dict[chan]["fft_time"] = fft_time
    data_dict[chan]["nperseg"] = nperseg

    return data_dict


def calc_psds(data_dict, averages, bandwidth, overlap, averaging="mean", window="hann"):
    """
    Take PSDs of all channels in data_dict.
    Returns them in the data_dict provided.
    """
    # Run some check functions
    bandwidth = check_sampling_frequency_vs_bandwidth(data_dict, bandwidth)
    new_duration = check_duration(data_dict, averages, bandwidth, overlap)

    # Take PSDs
    channels = data_dict.keys()
    for chan in channels:
        data = data_dict[chan]["data"]
        fs = data_dict[chan]["fs"]
        duration = data_dict[chan]["duration"]

        # Some code dealing with bad duration requests from the user
        if not new_duration == duration:
            fraction_time = new_duration / duration
            cutoff_index = int(fraction_time * len(data))

            data = data[:cutoff_index]
            duration = new_duration

        # expanding the data according to the overlap value
        duration_effective = duration * averages / (1 + (averages - 1) * (1 - overlap))
        fft_time = duration_effective / averages
        nperseg = int(np.ceil(fft_time * fs))

        ff, Pxx = sig.welch(
            data,
            fs=fs,
            window=window,
            nperseg=nperseg,
            noverlap=overlap,
            average=averaging,
        )
        data_dict[chan]["ff"] = ff
        data_dict[chan]["PSD"] = Pxx

        try:
            ff[1] - ff[0]
        except IndexError:
            print("IndexError, channel was likely all zeros, no sensible PSD taken")
            continue

        data_dict[chan]["df"] = ff[1] - ff[0]

        data_dict[chan]["averages"] = averages
        data_dict[chan]["binwidth"] = bandwidth
        data_dict[chan]["overlap"] = overlap
        data_dict[chan]["duration"] = duration
        data_dict[chan]["fft_time"] = fft_time
        data_dict[chan]["nperseg"] = nperseg

    return data_dict


def calc_csd(
    data_dict,
    chan_a,
    chan_b,
    averages,
    bandwidth,
    overlap,
    averaging="mean",
    window="hann",
    make_tfs=True,
    verbose=False,
):
    """
    Takes CSD between chan_a and chan_b with each other.
    If PSDs not taken, takes them automatically.
    If make_tfs=True, creates the TFs of all channels with one another.
    Returns everything in the data_dict provided.
    """
    channels = np.array([chan_a, chan_b])
    # Check if PSDs exist, if not make them.
    for chan in channels:
        if "PSD" not in data_dict[chan].keys():
            if verbose:
                print(f"Running calc_psd() for {chan}!")
            data_dict = calc_psd(
                data_dict,
                chan,
                averages,
                bandwidth,
                overlap,
                averaging=averaging,
                window=window,
            )
            if verbose:
                print(f"Got PSD for {chan}!")

    data_b = data_dict[chan_b]["data"]
    fs_b = data_dict[chan_b]["fs"]

    duration = dtt_time(averages, bandwidth, overlap)
    duration_effective = duration * averages / (1 + (averages - 1) * (1 - overlap))
    fft_time = duration_effective / averages
    # nperseg = int( np.ceil( fft_time * fs ) )

    data_a = data_dict[chan_a]["data"]
    fs_a = data_dict[chan_a]["fs"]
    if not fs_b == fs_a:
        if fs_b < fs_a:
            small_fs = fs_b
            large_fs = fs_a
            large_data = data_a
            large_chan = chan_a
        else:
            small_fs = fs_a
            large_fs = fs_b
            large_data = data_b
            large_chan = chan_b

        # decimate the data
        decimated_data = decimate_data(large_data, large_fs, small_fs)
        # ensure samples per segment is correct now
        nperseg = int(np.ceil(fft_time * small_fs))

        ff, Pxx = sig.welch(
            decimated_data,
            fs=small_fs,
            window=window,
            nperseg=nperseg,
            noverlap=overlap,
            average=averaging,
        )

        # don't overwrite previous ASDs
        large_chan_key_list = np.array(list(data_dict[large_chan].keys()))
        if "decimation" not in large_chan_key_list:
            data_dict[large_chan]["decimation"] = {}
        data_dict[large_chan]["decimation"][small_fs] = {}
        data_dict[large_chan]["decimation"][small_fs]["fs"] = small_fs
        data_dict[large_chan]["decimation"][small_fs]["ff"] = ff
        data_dict[large_chan]["decimation"][small_fs]["PSD"] = Pxx
        data_dict[large_chan]["decimation"][small_fs]["df"] = ff[1] - ff[0]

        if fs_b < fs_a:
            small_data = data_b
            small_data2 = decimated_data
        else:
            small_data = decimated_data
            small_data2 = data_a

    else:
        small_data = data_b
        small_data2 = data_a
        small_fs = fs_b
        nperseg = int(np.ceil(fft_time * fs_b))

    ff, Cxy = sig.csd(
        small_data,
        small_data2,
        fs=small_fs,
        window=window,
        nperseg=nperseg,
        noverlap=overlap,
        average=averaging,
    )

    data_dict[chan_b][chan_a] = {}
    data_dict[chan_b][chan_a]["ff"] = ff
    data_dict[chan_b][chan_a]["CSD"] = Cxy

    conj_Cxy = np.conj(Cxy)
    data_dict[chan_a][chan_b] = {}
    data_dict[chan_a][chan_b]["ff"] = ff
    data_dict[chan_a][chan_b]["CSD"] = conj_Cxy

    if make_tfs:
        data_dict = calc_tf(data_dict, chan_a, chan_b)

    return data_dict


def calc_csds(
    data_dict,
    averages,
    bandwidth,
    overlap,
    averaging="mean",
    window="hann",
    make_tfs=True,
    verbose=False,
):
    """
    Takes CSDs of all channels with each other.
    If PSDs not taken, takes them automatically.
    If make_tfs=True, creates the TFs of all channels with one another.
    Returns everything in the data_dict provided.
    """
    channels = np.array(list(data_dict.keys()))
    # Check if PSDs exist, if not make them.
    if "PSD" not in data_dict[channels[0]].keys():
        if verbose:
            print("Running calc_psds!")
        data_dict = calc_psds(
            data_dict,
            averages,
            bandwidth,
            overlap,
            averaging=averaging,
            window=window,
        )
        if verbose:
            print("Got PSDs!")

    for chan in channels:
        data = data_dict[chan]["data"]
        fs = data_dict[chan]["fs"]

        duration = dtt_time(averages, bandwidth, overlap)
        duration_effective = duration * averages / (1 + (averages - 1) * (1 - overlap))
        fft_time = duration_effective / averages
        # nperseg = int( np.ceil( fft_time * fs ) )

        for chan2 in channels:
            if chan == chan2:
                continue

            data2 = data_dict[chan2]["data"]
            fs2 = data_dict[chan2]["fs"]
            if not fs == fs2:
                if fs < fs2:
                    small_fs = fs
                    large_fs = fs2
                    large_data = data2
                    large_chan = chan2
                else:
                    small_fs = fs2
                    large_fs = fs
                    large_data = data
                    large_chan = chan

                decimation_ratio = int(large_fs / small_fs)
                # applied antialiasing automatically
                decimated_data = decimate_data(large_data, large_fs, small_fs)
                # ensure samples per segment is correct now
                nperseg = int(np.ceil(fft_time * small_fs))

                ff, Pxx = sig.welch(
                    decimated_data,
                    fs=small_fs,
                    window=window,
                    nperseg=nperseg,
                    noverlap=overlap,
                    average=averaging,
                )

                # don't overwrite previous ASDs
                large_chan_key_list = np.array(list(data_dict[large_chan].keys()))
                if "decimation" not in large_chan_key_list:
                    data_dict[large_chan]["decimation"] = {}
                data_dict[large_chan]["decimation"][small_fs] = {}
                data_dict[large_chan]["decimation"][small_fs]["fs"] = small_fs
                data_dict[large_chan]["decimation"][small_fs]["ff"] = ff
                data_dict[large_chan]["decimation"][small_fs]["PSD"] = Pxx
                data_dict[large_chan]["decimation"][small_fs]["df"] = ff[1] - ff[0]

                if fs < fs2:
                    small_data = data
                    small_data2 = decimated_data
                else:
                    small_data = decimated_data
                    small_data2 = data2

            else:
                small_data = data
                small_data2 = data2
                small_fs = fs
                nperseg = int(np.ceil(fft_time * fs))

            ff, Cxy = sig.csd(
                small_data,
                small_data2,
                fs=small_fs,
                window=window,
                nperseg=nperseg,
                noverlap=overlap,
                average=averaging,
            )

            data_dict[chan][chan2] = {}
            data_dict[chan][chan2]["ff"] = ff
            data_dict[chan][chan2]["CSD"] = Cxy

    if make_tfs:
        data_dict = calc_tfs(data_dict)

    return data_dict


def calc_tf(data_dict, chan_a, chan_b):
    """
    Takes TF and coherence of chan_a and chan_b in the data_dict with each other.
    Returns them in a new data_dict, a copy of the old data_dict with the new TFs and coherences.
    """

    if "CSD" not in data_dict[chan_b][chan_a]:
        print(f"You must run calc_csd() for {chan_a} and {chan_b} first!")
        print("Exiting")
        return

    fs_b = data_dict[chan_b]["fs"]
    fs_a = data_dict[chan_a]["fs"]

    if not fs_b == fs_a:
        if fs_b < fs_a:
            small_fs = fs_b
            large_fs = fs_a
            asd1 = np.sqrt(data_dict[chan_b]["PSD"])
            asd2 = np.sqrt(data_dict[chan_a]["decimation"][small_fs]["PSD"])
            psd = data_dict[chan_a]["decimation"][small_fs]["PSD"]
            csd = data_dict[chan_a][chan_b]["CSD"]
        else:
            small_fs = fs_a
            large_fs = fs_b
            asd1 = np.sqrt(data_dict[chan_b]["decimation"][small_fs]["PSD"])
            asd2 = np.sqrt(data_dict[chan_a]["PSD"])
            psd = data_dict[chan_a]["PSD"]
            csd = data_dict[chan_a][chan_b]["CSD"]
    else:
        asd1 = np.sqrt(data_dict[chan_b]["PSD"])
        asd2 = np.sqrt(data_dict[chan_a]["PSD"])
        psd = data_dict[chan_a]["PSD"]
        csd = data_dict[chan_a][chan_b]["CSD"]

    tf = csd / psd
    # return a power coherence, but use asds to avoid really small numbers
    coh = (np.abs(csd) / (asd1 * asd2)) ** 2

    # Store TF as chan_b/chan_a
    data_dict[chan_b][chan_a]["TF"] = tf
    data_dict[chan_b][chan_a]["coh"] = coh

    data_dict[chan_a][chan_b]["TF"] = 1 / tf
    data_dict[chan_a][chan_b]["coh"] = coh

    return data_dict


def calc_tfs(data_dict):
    """
    Takes TFs and coherences of all channels in the data_dict with each other.
    Returns them in the data_dict provided.
    """
    channels = np.array(list(data_dict.keys()))
    if "CSD" not in data_dict[channels[0]][channels[1]]:
        print("You must run calc_csds() first!")
        print("Exiting")
        return

    for chan in channels:
        for chan2 in channels:
            if chan == chan2:
                continue
            if chan not in data_dict[chan2].keys():
                continue

            fs = data_dict[chan]["fs"]
            fs2 = data_dict[chan2]["fs"]

            if not fs == fs2:
                if fs < fs2:
                    small_fs = fs
                    large_fs = fs2
                    asd1 = np.sqrt(data_dict[chan]["PSD"])
                    asd2 = np.sqrt(data_dict[chan2]["decimation"][small_fs]["PSD"])
                    psd = data_dict[chan2]["decimation"][small_fs]["PSD"]
                    csd = data_dict[chan2][chan]["CSD"]
                else:
                    small_fs = fs2
                    large_fs = fs
                    asd1 = np.sqrt(data_dict[chan]["decimation"][small_fs]["PSD"])
                    asd2 = np.sqrt(data_dict[chan2]["PSD"])
                    psd = data_dict[chan2]["PSD"]
                    csd = data_dict[chan2][chan]["CSD"]
            else:
                asd1 = np.sqrt(data_dict[chan]["PSD"])
                asd2 = np.sqrt(data_dict[chan2]["PSD"])
                psd = data_dict[chan2]["PSD"]
                csd = data_dict[chan2][chan]["CSD"]

            tf = csd / psd
            # return a power coherence, but use asds to avoid really small numbers
            coh = (np.abs(csd) / (asd1 * asd2)) ** 2

            # Store TF as chan_b/chan_a
            data_dict[chan][chan2]["TF"] = tf
            data_dict[chan][chan2]["coh"] = coh

    return data_dict


def calc_decimated_psd(
    data_dict,
    chan,
    decimated_fs,
    averages,
    bandwidth,
    overlap,
    averaging="mean",
    window="hann",
):
    """
    Take PSDs of all channels in data_dict at a decimated sampling frequency.
    Returns them in the data_dict provided.
    """

    fs = data_dict[chan]["fs"]
    if fs == decimated_fs:
        print(f"{chan} sampling frequency = {fs} Hz")
        print(f"same as user requested sampling frequency = {decimated_fs} Hz")
        if not "PSD" in data_dict[chan].keys():
            print("Running calc_psds()!")
            data_dict = calc_psds(data_dict, averages, bandwidth, overlap)
        else:
            print("PSDs already calculated.")
            print(f"Doing nothing")
        return data_dict

    data = data_dict[chan]["data"]

    duration = dtt_time(averages, bandwidth, overlap)
    duration_effective = duration * averages / (1 + (averages - 1) * (1 - overlap))
    fft_time = duration_effective / averages

    decimated_data = decimate_data(data, fs, decimated_fs)
    nperseg = int(np.ceil(fft_time * decimated_fs))

    ff, Pxx = sig.welch(
        decimated_data,
        fs=decimated_fs,
        window=window,
        nperseg=nperseg,
        noverlap=overlap,
        average=averaging,
    )

    # don't overwrite previous ASDs
    chan_key_list = np.array(list(data_dict[chan].keys()))
    if "decimation" not in chan_key_list:
        data_dict[chan]["decimation"] = {}
    data_dict[chan]["decimation"][decimated_fs] = {}
    data_dict[chan]["decimation"][decimated_fs]["fs"] = decimated_fs
    data_dict[chan]["decimation"][decimated_fs]["ff"] = ff
    data_dict[chan]["decimation"][decimated_fs]["PSD"] = Pxx
    data_dict[chan]["decimation"][decimated_fs]["df"] = ff[1] - ff[0]
    data_dict[chan]["decimation"][decimated_fs]["averages"] = averages
    data_dict[chan]["decimation"][decimated_fs]["binwidth"] = bandwidth
    data_dict[chan]["decimation"][decimated_fs]["overlap"] = overlap
    data_dict[chan]["decimation"][decimated_fs]["duration"] = duration
    data_dict[chan]["decimation"][decimated_fs]["fft_time"] = fft_time
    data_dict[chan]["decimation"][decimated_fs]["nperseg"] = nperseg

    return data_dict


def calc_decimated_csd(
    data_dict,
    chan_a,
    chan_b,
    decimated_fs,
    averages,
    bandwidth,
    overlap,
    averaging="mean",
    window="hann",
    make_tfs=True,
):
    """Calculate the decimated CSD between two channels chan_a and chan_b.
    Good for if the excitation channel has a different sampling frequency than the others.
    """
    fs_a = data_dict[chan_a]["fs"]
    fs_b = data_dict[chan_b]["fs"]

    if (
        fs_a > decimated_fs
        and not "PSD" in data_dict[chan_a]["decimation"][decimated_fs].keys()
    ):
        calc_decimated_psd(
            data_dict, chan_a, decimated_fs, averages, bandwidth, overlap
        )
    elif fs_a == decimated_fs and not "PSD" in data_dict[chan_a].keys():
        calc_psds(data_dict, averages, bandwidth, overlap)

    if (
        fs_b > decimated_fs
        and not "PSD" in data_dict[chan_b]["decimation"][decimated_fs].keys()
    ):
        calc_decimated_psd(
            data_dict, chan_b, decimated_fs, averages, bandwidth, overlap
        )
    elif fs_b == decimated_fs and not "PSD" in data_dict[chan_b].keys():
        calc_psds(data_dict, averages, bandwidth, overlap)

    if chan_a == chan_b:
        print(f"chan_a = {chan_a}")
        print(f"chan_b = {chan_b}")
        print("Doing nothing")
        return data_dict

    data_a = data_dict[chan_a]["data"]
    data_b = data_dict[chan_b]["data"]

    duration = dtt_time(averages, bandwidth, overlap)
    duration_effective = duration * averages / (1 + (averages - 1) * (1 - overlap))
    fft_time = duration_effective / averages
    nperseg = int(np.ceil(fft_time * decimated_fs))

    # Check the sampling frequencies to see if the data must be decimated
    if fs_a == decimated_fs and fs_b == decimated_fs:
        print(f"The sampling frequency of chan_a {chan_a} = {fs_a} Hz")
        print(f"The sampling frequency of chan_b {chan_b} = {fs_b} Hz")
        print(f"The decimated sampling frequency = {decimated_fs} Hz")
        print(f"Use calc_csds() instead")
        return data_dict

    if fs_a > decimated_fs:
        small_data_a = decimate_data(data_a, fs_a, decimated_fs)

    else:
        small_data_a = data_a

    if fs_b > decimated_fs:
        small_data_b = decimate_data(data_b, fs_b, decimated_fs)
    else:
        small_data_b = data_b

    # Calculate the CSD
    ff, Cxy = sig.csd(
        small_data_a,
        small_data_b,
        fs=decimated_fs,
        window=window,
        nperseg=nperseg,
        noverlap=overlap,
        average=averaging,
    )

    data_dict[chan_a][chan_b]["decimation"][decimated_fs] = {}
    data_dict[chan_a][chan_b]["decimation"][decimated_fs]["ff"] = ff
    data_dict[chan_a][chan_b]["decimation"][decimated_fs]["CSD"] = Cxy
    data_dict[chan_a][chan_b]["decimation"][decimated_fs]["fs"] = decimated_fs
    data_dict[chan_a][chan_b]["decimation"][decimated_fs]["df"] = ff[1] - ff[0]
    data_dict[chan_a][chan_b]["decimation"][decimated_fs]["averages"] = averages
    data_dict[chan_a][chan_b]["decimation"][decimated_fs]["binwidth"] = bandwidth
    data_dict[chan_a][chan_b]["decimation"][decimated_fs]["overlap"] = overlap
    data_dict[chan_a][chan_b]["decimation"][decimated_fs]["duration"] = duration
    data_dict[chan_a][chan_b]["decimation"][decimated_fs]["fft_time"] = fft_time
    data_dict[chan_a][chan_b]["decimation"][decimated_fs]["nperseg"] = nperseg

    # record the complex conjugate as well
    data_dict[chan_b][chan_a]["decimation"][decimated_fs] = {}
    data_dict[chan_b][chan_a]["decimation"][decimated_fs]["ff"] = ff
    data_dict[chan_b][chan_a]["decimation"][decimated_fs]["CSD"] = np.conjugate(Cxy)
    data_dict[chan_b][chan_a]["decimation"][decimated_fs]["fs"] = decimated_fs
    data_dict[chan_b][chan_a]["decimation"][decimated_fs]["df"] = ff[1] - ff[0]
    data_dict[chan_b][chan_a]["decimation"][decimated_fs]["averages"] = averages
    data_dict[chan_b][chan_a]["decimation"][decimated_fs]["binwidth"] = bandwidth
    data_dict[chan_b][chan_a]["decimation"][decimated_fs]["overlap"] = overlap
    data_dict[chan_b][chan_a]["decimation"][decimated_fs]["duration"] = duration
    data_dict[chan_b][chan_a]["decimation"][decimated_fs]["fft_time"] = fft_time
    data_dict[chan_b][chan_a]["decimation"][decimated_fs]["nperseg"] = nperseg

    if make_tfs:
        data_dict = calc_decimated_tf(data_dict, chan_a, chan_b, decimated_fs)

    return data_dict


def calc_decimated_tf(data_dict, chan_a, chan_b, decimated_fs):
    """
    Takes TFs and coherences using decimated spectra
    between specified channels in the data_dict with each other.
    Returns them in the data_dict provided.
    """
    fs_a = data_dict[chan_a]["fs"]
    fs_b = data_dict[chan_b]["fs"]

    if "CSD" not in data_dict[chan_a][chan_b]["decimation"][decimated_fs]:
        print("You must run calc_decimated_csd() first!")
        print("Exiting")
        return

    if chan_a == chan_b:
        print(f"chan_a = {chan_a}")
        print(f"chan_b = {chan_b}")
        print("Doing nothing")
        return data_dict

    if fs_a == decimated_fs and fs_b == decimated_fs:
        print(f"The sampling frequency of chan_a {chan_a} = {fs_a} Hz")
        print(f"The sampling frequency of chan_b {chan_b} = {fs_b} Hz")
        print(f"The decimated sampling frequency = {decimated_fs} Hz")
        print(f"Use calc_tfs() instead")
        return data_dict

    if fs_a > decimated_fs:
        psd_a = data_dict[chan_a]["decimation"][decimated_fs]["PSD"]
    else:
        psd_a = data_dict[chan_a]["PSD"]

    if fs_b > decimated_fs:
        psd_b = data_dict[chan_b]["decimation"][decimated_fs]["PSD"]
    else:
        psd_b = data_dict[chan_b]["PSD"]

    csd_ab = data_dict[chan_a][chan_b]["decimation"][decimated_fs]["CSD"]

    tf = csd_ab / psd_a
    coh = calculate_coherence(psd_a, psd_b, csd_ab)

    # Store TF as chan_b/chan_a
    data_dict[chan_a][chan_b]["decimation"][decimated_fs]["TF"] = tf
    data_dict[chan_a][chan_b]["decimation"][decimated_fs]["coh"] = coh

    # store the complex conjugate
    data_dict[chan_b][chan_a]["decimation"][decimated_fs]["TF"] = np.conjugate(tf)
    data_dict[chan_b][chan_a]["decimation"][decimated_fs]["coh"] = coh

    return data_dict


def calc_decimated_psds(
    data_dict,
    decimated_fs,
    averages,
    bandwidth,
    overlap,
    averaging="mean",
    window="hann",
):
    """
    Take PSDs of all channels in data_dict at a decimated sampling frequency.
    Returns them in the data_dict provided.
    """
    channels = np.array(list(data_dict.keys()))
    for chan in channels:
        fs = data_dict[chan]["fs"]
        if fs == decimated_fs:
            continue

        data = data_dict[chan]["data"]

        duration = dtt_time(averages, bandwidth, overlap)
        duration_effective = duration * averages / (1 + (averages - 1) * (1 - overlap))
        fft_time = duration_effective / averages

        # applied antialiasing automatically
        decimated_data = decimate_data(data, fs, decimated_fs)
        # ensure samples per segment is correct now
        nperseg = int(np.ceil(fft_time * decimated_fs))

        ff, Pxx = sig.welch(
            decimated_data,
            fs=decimated_fs,
            window=window,
            nperseg=nperseg,
            noverlap=overlap,
            average=averaging,
        )

        # don't overwrite previous ASDs
        chan_key_list = np.array(list(data_dict[chan].keys()))
        if "decimation" not in chan_key_list:
            data_dict[chan]["decimation"] = {}
        data_dict[chan]["decimation"][decimated_fs] = {}
        data_dict[chan]["decimation"][decimated_fs]["fs"] = decimated_fs
        data_dict[chan]["decimation"][decimated_fs]["ff"] = ff
        data_dict[chan]["decimation"][decimated_fs]["PSD"] = Pxx
        data_dict[chan]["decimation"][decimated_fs]["df"] = ff[1] - ff[0]

        try:
            ff[1] - ff[0]
        except IndexError:
            print("IndexError, channel was likely all zeros, no sensible PSD taken")
            continue

        data_dict[chan]["decimation"][decimated_fs]["averages"] = averages
        data_dict[chan]["decimation"][decimated_fs]["binwidth"] = bandwidth
        data_dict[chan]["decimation"][decimated_fs]["overlap"] = overlap
        data_dict[chan]["decimation"][decimated_fs]["duration"] = duration
        data_dict[chan]["decimation"][decimated_fs]["fft_time"] = fft_time
        data_dict[chan]["decimation"][decimated_fs]["nperseg"] = nperseg

    return data_dict


# Coming soon
# def calc_decimated_csds()


def get_psds(
    channels,
    gps_start: int,
    gps_stop: int,
    binwidth: float,
    overlap: float,
    averaging: str = "mean",
    window: str = "hann",
    host_server: str = "nds.ligo-wa.caltech.edu",
    port_number: int = 31200,
    allow_data_on_tape: str = "False",
    gap_handler: str = "STATIC_HANDLER_NAN",
    is_minute_trend: bool = False,
    verbose: bool = True,
):
    """
    Use nds2 to get LIGO data, and automatically calculate some power spectral densities (PSDs) from the data.
    Should be slightly faster than get_csds(), especially for large numbers of channels.

    Valid Host Sever:Port Number combos:
    h1nds1:8088 # only good on LHO CDS computers
    h1nds0:8088 # only good on LHO CDS computers
    nds.ligo-wa.caltech.edu:31200
    nds.ligo-la.caltech.edu:31200
    nds.ligo.caltech.edu:31200

    If you request minute trends of a channel by ending a channel name with ,m-trend
    this script will automatically adjust your gps_start and gps_stop times to align
    with the minute trend boundaries (basically the gpstimes must be divisible by 60)

    Inputs:
    -------
    channels           = array of strs. Valid LIGO channels from which to fetch data
    gps_start          = int. Valid GPS time at which to start acquiring data
    gps_stop           = int. Valid GPS time at which to stop acquiring data
    binwidth           = float.  Frequency bin spacing for PSDs
    overlap            = float.  Overlap of the time series for the PSD calculations
    averaging          = str.  Either 'mean' or 'median' averaging for the PSD calculations. Default is 'mean'.
    host_server        = str. Valid nds2 server.  Default is `nds.ligo-wa.caltech.edu`
    port_number        = int. Valid port from which to access the server.  Default is 31200
    allow_data_on_tape = str. String should be `True` or `False`.  Set to `True` if need really old data, is slower.
    gap_handler        = str.  Defines how gaps in the data should be handled by nds2.  String default is 'STATIC_HANDLER_NAN'.
                         Usual nds2 default is 'ABORT_HANDLER', which kills your request if there's any unavailable data.
                         More info at https://www.lsc-group.phys.uwm.edu/daswg/projects/nds-client/doc/manual/ch04s02.html.
    is_minute_trend    = bool.  If true, will adjust gps_times to align with minute trend boundaries.  Default is False.
    verbose            = bool. Default true.  If set will print to terminal all input arguments.

    Output:
    -------
    Returns a dictionary with channel names as keys, and values which are also dictionaries containing the time-series data, sampling rate,
    and PSDs calculated.

    ### Example ###
    import numpy as np
    from dataUtils import *
    channels = np.array(['H1:CAL-DELTAL_EXTERNAL_DQ', 'H1:PSL-ISS_SECONDLOOP_RIN_OUTER_OUT_DQ', 'H1:LSC-REFL_SERVO_ERR_OUT_DQ'])
    gps_stop_23 = 1256771546
    duration = 150
    gps_start_23 = gps_stop_23 - duration
    overlap = 0.75
    binwidth = 1.0
    data_dict_23 = get_psds(channels, gps_start_23, gps_stop_23, binwidth, overlap)
    """
    duration = int(gps_stop - gps_start)
    averages = dtt_averages(duration, binwidth, overlap)

    if allow_data_on_tape == True:
        allow_data_on_tape = "True"
    elif allow_data_on_tape == False:
        allow_data_on_tape = "False"

    if verbose:
        print("Getting PSDs:")
        print("Channels = {}".format(channels))
        print("gps_start = {}".format(gps_start))
        print("gps_stop  = {}".format(gps_stop))
        print("duration = {} s".format(duration))
        print("averages = {}".format(averages))
        print("binwidth = {} Hz".format(binwidth))
        print("overlap = {}".format(overlap))
        print("averaging = {}".format(averaging))
        print("window = {}".format(window))
        print("host_server = {}".format(host_server))
        print("port_number = {}".format(port_number))
        print("allow_data_on_tape = {}".format(allow_data_on_tape))
        print("gap_handler = {}".format(gap_handler))
        print("is_minute_trend = {}".format(is_minute_trend))
        print("verbose = {}".format(verbose))

    data_dict = acquire_data(
        channels,
        gps_start,
        gps_stop,
        host_server=host_server,
        port_number=port_number,
        allow_data_on_tape=allow_data_on_tape,
        gap_handler=gap_handler,
        is_minute_trend=is_minute_trend,
    )
    data_dict = calc_psds(
        data_dict, averages, binwidth, overlap, averaging=averaging, window=window
    )
    return data_dict


def get_csds(
    channels,
    gps_start: int,
    gps_stop: int,
    binwidth: float,
    overlap: float,
    averaging: str = "mean",
    window: str = "hann",
    host_server: str = "nds.ligo-wa.caltech.edu",
    port_number: int = 31200,
    allow_data_on_tape: str = "False",
    gap_handler: str = "STATIC_HANDLER_NAN",
    is_minute_trend: bool = False,
    make_tfs: bool = True,
    verbose: bool = True,
):
    """
    Use nds2 to get LIGO data, and automatically calculate some PSDs, CSDs and TFs from the data.

    Valid Host Sever:Port Number combos:
    h1nds1:8088 # only good on LHO CDS computers
    h1nds0:8088
    nds.ligo-wa.caltech.edu:31200
    nds.ligo-la.caltech.edu:31200
    nds.ligo.caltech.edu:31200

    If you request minute trends of a channel by ending a channel name with ,m-trend
    this script will automatically adjust your gps_start and gps_stop times to align
    with the minute trend boundaries (basically the gpstimes must be divisible by 60)

    Inputs:
    channels           = array of strs. Valid LIGO channels from which to fetch data
    gps_start          = int. Valid GPS time at which to start acquiring data
    gps_stop           = int. Valid GPS time at which to stop acquiring data
    binwidth           = float.  Frequency bin spacing for PSDs
    overlap            = float.  Overlap of the time series for the PSD calculations
    averaging          = str.  Either 'mean' or 'median' averaging for the PSD calculations. Default is 'mean'.
    host_server        = str. Valid nds2 server.  Default is `nds.ligo-wa.caltech.edu`
    port_number        = int. Valid port from which to access the server.  Default is 31200
    allow_data_on_tape = str. String should be `True` or `False`.  Set to `True` if need really old data, is slower.
    gap_handler        = str.  Defines how gaps in the data should be handled by nds2.  String default is 'STATIC_HANDLER_NAN'.
                         Usual nds2 default is 'ABORT_HANDLER', which kills your request if there's any unavailable data.
                         More info at https://www.lsc-group.phys.uwm.edu/daswg/projects/nds-client/doc/manual/ch04s02.html.
    is_minute_trend    = bool.  If true, will adjust gps_times to align with minute trend boundaries.  Default is False.
    make_tfs           = bool.  If true, will calculate transfer functions and power coherence from all calculated CSDs.  Default is True.
    verbose            = bool. Default true.  If set will print to terminal all input arguments.

    Output:
    Returns a dictionary with channel names as keys,
    and values which are also dictionaries containing the time-series data, sampling rate,
    and PSDs, CSDs, and TFs calculated.

    ### Example ###
    import numpy as np
    from dataUtils import *
    channels = np.array(['H1:CAL-DELTAL_EXTERNAL_DQ', 'H1:PSL-ISS_SECONDLOOP_RIN_OUTER_OUT_DQ', 'H1:LSC-REFL_SERVO_ERR_OUT_DQ'])
    gps_stop_23 = 1256771546
    duration = 150
    gps_start_23 = gps_stop_23 - duration
    overlap = 0.75
    binwidth = 1.0
    data_dict_23 = get_csds(channels, gps_start_23, gps_stop_23, binwidth, overlap)

    """
    duration = int(gps_stop - gps_start)
    averages = dtt_averages(duration, binwidth, overlap)

    if allow_data_on_tape == True:
        allow_data_on_tape = "True"
    elif allow_data_on_tape == False:
        allow_data_on_tape = "False"

    if verbose:
        print("Getting CSDs:")
        print("Channels = {}".format(channels))
        print("gps_start = {}".format(gps_start))
        print("gps_stop  = {}".format(gps_stop))
        print("duration = {} s".format(duration))
        print("averages = {}".format(averages))
        print("binwidth = {} Hz".format(binwidth))
        print("overlap = {}".format(overlap))
        print("averaging = {}".format(averaging))
        print("window = {}".format(window))
        print("host_server = {}".format(host_server))
        print("port_number = {}".format(port_number))
        print("allow_data_on_tape = {}".format(allow_data_on_tape))
        print("gap_handler = {}".format(gap_handler))
        print("is_minute_trend = {}".format(is_minute_trend))
        print("make_tfs = {}".format(make_tfs))
        print("verbose = {}".format(verbose))

    data_dict = acquire_data(
        channels,
        gps_start,
        gps_stop,
        host_server=host_server,
        port_number=port_number,
        allow_data_on_tape=allow_data_on_tape,
        gap_handler=gap_handler,
        is_minute_trend=is_minute_trend,
    )
    data_dict = calc_csds(
        data_dict,
        averages,
        binwidth,
        overlap,
        averaging=averaging,
        window=window,
        make_tfs=make_tfs,
    )
    return data_dict


### get_all spectral density functions
# returns every psd, csd used in calculating the average psd, csd via Welch's method
def get_all_psds(
    x,
    fs=1.0,
    window="hann",
    nperseg=None,
    noverlap=None,
    nfft=None,
    detrend="constant",
    return_onesided=True,
    scaling="density",
    axis=-1,
):
    """Abuses the function scipy.signal.spectrogram()
    to return all power spectral densities which make up a PSD estimate.
    Should be equivalent exactly to scipy.signal.spectrogram(mode='psd'),
    but we want to use this method for get_all_csds() as well.
    Included for consistency.

    Parameters
    ----------
    x : array_like
        Time series of measurement values
    fs : float, optional
        Sampling frequency of the `x` time series. Defaults to 1.0.
    window : str or tuple or array_like, optional
        Desired window to use. If `window` is a string or tuple, it is
        passed to `get_window` to generate the window values, which are
        DFT-even by default. See `get_window` for a list of windows and
        required parameters. If `window` is array_like it will be used
        directly as the window and its length must be nperseg.
        Defaults to a Tukey window with shape parameter of 0.25.
    nperseg : int, optional
        Length of each segment. Defaults to None, but if window is str or
        tuple, is set to 256, and if window is array_like, is set to the
        length of the window.
    noverlap : int, optional
        Number of points to overlap between segments. If `None`,
        ``noverlap = nperseg // 8``. Defaults to `None`.
    nfft : int, optional
        Length of the FFT used, if a zero padded FFT is desired. If
        `None`, the FFT length is `nperseg`. Defaults to `None`.
    detrend : str or function or `False`, optional
        Specifies how to detrend each segment. If `detrend` is a
        string, it is passed as the `type` argument to the `detrend`
        function. If it is a function, it takes a segment and returns a
        detrended segment. If `detrend` is `False`, no detrending is
        done. Defaults to 'constant'.
    return_onesided : bool, optional
        If `True`, return a one-sided spectrum for real data. If
        `False` return a two-sided spectrum. Defaults to `True`, but for
        complex data, a two-sided spectrum is always returned.
    scaling : { 'density', 'spectrum' }, optional
        Selects between computing the power spectral density ('density')
        where `Sxx` has units of V**2/Hz and computing the power
        spectrum ('spectrum') where `Sxx` has units of V**2, if `x`
        is measured in V and `fs` is measured in Hz. Defaults to
        'density'.
    axis : int, optional
        Axis along which the spectrogram is computed; the default is over
        the last axis (i.e. ``axis=-1``).
    mode : str, optional
        Defines what kind of return values are expected. Options are
        ['psd', 'complex', 'magnitude', 'angle', 'phase']. 'complex' is
        equivalent to the output of `stft` with no padding or boundary
        extension. 'magnitude' returns the absolute magnitude of the
        STFT. 'angle' and 'phase' return the complex angle of the STFT,
        with and without unwrapping, respectively.

    Returns
    -------
    f : ndarray
        Array of sample frequencies.
    t : ndarray
        Array of segment times.
    Sxxs : ndarray
        Power spectral densities of x. By default, the last axis of Sxx corresponds
        to the segment times.

    """
    freqs, time, Fxx = sig.spectrogram(
        x,
        fs=fs,
        window=window,
        nperseg=nperseg,
        noverlap=noverlap,
        nfft=nfft,
        detrend=detrend,
        return_onesided=return_onesided,
        scaling=scaling,
        axis=axis,
        mode="complex",
    )
    Sxxs = np.abs(2 * np.conjugate(Fxx) * Fxx)

    return freqs, time, Sxxs


def get_all_csds(
    x,
    y,
    fs=1.0,
    window="hann",
    nperseg=None,
    noverlap=None,
    nfft=None,
    detrend="constant",
    return_onesided=True,
    scaling="density",
    axis=-1,
):
    """Abuses the function scipy.signal.spectrogram()
    to return all cross spectral densities which make up a CSD estimate.

    Parameters
    ----------
    x : array_like
        Time series of measurement values
    y : array_like
        Time series of measurement values
    fs : float, optional
        Sampling frequency of the `x` time series. Defaults to 1.0.
    window : str or tuple or array_like, optional
        Desired window to use. If `window` is a string or tuple, it is
        passed to `get_window` to generate the window values, which are
        DFT-even by default. See `get_window` for a list of windows and
        required parameters. If `window` is array_like it will be used
        directly as the window and its length must be nperseg.
        Defaults to a Tukey window with shape parameter of 0.25.
    nperseg : int, optional
        Length of each segment. Defaults to None, but if window is str or
        tuple, is set to 256, and if window is array_like, is set to the
        length of the window.
    noverlap : int, optional
        Number of points to overlap between segments. If `None`,
        ``noverlap = nperseg // 8``. Defaults to `None`.
    nfft : int, optional
        Length of the FFT used, if a zero padded FFT is desired. If
        `None`, the FFT length is `nperseg`. Defaults to `None`.
    detrend : str or function or `False`, optional
        Specifies how to detrend each segment. If `detrend` is a
        string, it is passed as the `type` argument to the `detrend`
        function. If it is a function, it takes a segment and returns a
        detrended segment. If `detrend` is `False`, no detrending is
        done. Defaults to 'constant'.
    return_onesided : bool, optional
        If `True`, return a one-sided spectrum for real data. If
        `False` return a two-sided spectrum. Defaults to `True`, but for
        complex data, a two-sided spectrum is always returned.
    scaling : { 'density', 'spectrum' }, optional
        Selects between computing the power spectral density ('density')
        where `Sxx` has units of V**2/Hz and computing the power
        spectrum ('spectrum') where `Sxx` has units of V**2, if `x`
        is measured in V and `fs` is measured in Hz. Defaults to
        'density'.
    axis : int, optional
        Axis along which the spectrogram is computed; the default is over
        the last axis (i.e. ``axis=-1``).
    mode : str, optional
        Defines what kind of return values are expected. Options are
        ['psd', 'complex', 'magnitude', 'angle', 'phase']. 'complex' is
        equivalent to the output of `stft` with no padding or boundary
        extension. 'magnitude' returns the absolute magnitude of the
        STFT. 'angle' and 'phase' return the complex angle of the STFT,
        with and without unwrapping, respectively.

    Returns
    -------
    f : ndarray
        Array of sample frequencies.
    t : ndarray
        Array of segment times.
    Sxys : ndarray
        Cross spectral densities of x and y. By default, the last axis of Sxys corresponds
        to the segment times.

    """
    freqs, time, Fxx = sig.spectrogram(
        x,
        fs=fs,
        window=window,
        nperseg=nperseg,
        noverlap=noverlap,
        nfft=nfft,
        detrend=detrend,
        return_onesided=return_onesided,
        scaling=scaling,
        axis=axis,
        mode="complex",
    )
    freqs, time, Fyy = sig.spectrogram(
        y,
        fs=fs,
        window=window,
        nperseg=nperseg,
        noverlap=noverlap,
        nfft=nfft,
        detrend=detrend,
        return_onesided=return_onesided,
        scaling=scaling,
        axis=axis,
        mode="complex",
    )
    Sxys = 2 * np.conjugate(Fxx) * Fyy

    return freqs, time, Sxys


### Convenience functions for returning median-averaged psds and csds from get_all functions
def get_median_psd(Saas):
    """Calculate the median PSD from a bunch of PSDs.  No bias is applied.
    Example:
    Sxxs = get_all_psds(x)
    Sxx_med = get_median_psd(Sxxs)
    """
    Saa_med = np.median(Saas, axis=1)
    return Saa_med


def get_median_csd(Sabs):
    """Calculate the median CSD from a bunch of CSDs.  No bias is applied.
    Example:
    Sxys = get_all_csds(x, y)
    Sxy_med = get_median_csd(Sxys)
    """
    Sab_med = np.median(np.real(Sabs), axis=1) + 1j * np.median(np.imag(Sabs), axis=1)
    return Sab_med


def get_coherence(Saa_med, Sbb_med, Sab_med):
    """Calculate the coherence from given PSDs and CSDs.
    Example:
    Sxxs = get_all_psds(x)
    Syys = get_all_psds(y)
    Sxys = get_all_csds(x, y)

    Sxx_med = get_median_psd(Sxxs)
    Syy_med = get_median_psd(Syys)
    Sxy_med = get_median_csd(Sxys)

    cohs_med = get_coherence(Sxx_med, Syy_med, Sxy_med)
    """
    coherence_med = np.abs(Sab_med) ** 2 / (Saa_med * Sbb_med)
    return coherence_med


### Equivalent convenience functions for mean-averaged psds and csds.
def get_mean_psd(Saas):
    """Calculate the mean PSD from a bunch of PSDs.  No bias is applied.
    Example:
    Sxxs = get_all_psds(x)
    Sxx_mean = get_mean_psd(Sxxs)
    """
    Saa_mean = np.mean(Saas, axis=1)
    return Saa_mean


def get_mean_csd(Sabs):
    """Calculate the mean CSD from a bunch of CSDs.  No bias is applied.
    Example:
    Sxys = get_all_csds(x, y)
    Sxy_mean = get_mean_csd(Sxys)
    """
    Sab_mean = np.mean(np.real(Sabs), axis=1) + 1j * np.mean(np.imag(Sabs), axis=1)
    return Sab_mean


### Mean-to-median bias functions for cross spectral densities
# Outward-facing function is biases_from_coherences()
def median_coherence_from_power_ratio(power_ratio):
    """Given a power_ratio of uncorrelated noise over correlated noise,
    power_ratio = sigma_uncorr^2 / sigma_corr^2,
    returns the power coherence gamma^2 that would result from median-averaged PSDs and CSDs.
    """
    med_coh = (power_ratio**2 * np.log(1 + 1 / np.sqrt(1 + power_ratio)) ** 2) / (
        4
        * np.log(2) ** 2
        * (1 + power_ratio)
        * (2 + power_ratio - 2 * np.sqrt(1 + power_ratio))
    )
    return med_coh


def residual_median_coherence(input_array, median_coherence_desired):
    """Finds the residual between the coherence desired and the numerically attempt from fsolve().
    For use as the function input to fsolve() in bias_from_median_coherence().
    Inputs:
    input_array = array of length one, required by fsolve to find the power ratio numerically
    median_coherence_desired = median coherence estimated from the CSD signals.
    Output:
    residual = array of length one with residual from median_coherence() function
    """
    func_results = median_coherence_from_power_ratio(input_array[0])
    residual = [func_results - median_coherence_desired]
    return residual


def bias_from_median_coherence_and_power_ratio(median_coherence, power_ratio):
    """Calculates the mean-to-median bias factor from the median_coherence = gamma^2
    and the power_ratio = epsilon.
    """
    bias = np.log(2) * np.sqrt((1 + power_ratio) * median_coherence)
    return bias


def bias_from_median_coherence(median_coherence_estimated, initial_power_ratio=0.1):
    """Estimates the median/mean bias = b given some median_coherence = gamma^2.

    Numerically solves for the uncorrelated/correated power_ratio = epsilon,
    using the median_coherence.
    Uses scipy.optimize.fsolve() to find the root of residual_median_coherence().
    fsolve() seems to work for gamma^2 between (0.999 and 1e-6)

    This function requires bias_from_median_coherence_and_power_ratio(),
    residual_median_coherence(), median_coherence(), and fsolve() functions.

    Inputs:
    median_coherence_estimated  =   median coherence estimated from |<x,z>|^2/(<x,x> <z,z>)
                                    where all spectral densities are median-averaged
    initial_power_ratio         =   initial guess of the power_ratio, default is 1.0
    Output:
    bias    =   median/mean bias factor.  Divide median-averaged cross spectral density <x,z>
                by bias to recover the mean-avearged cross spectral density.
    """
    # Numerically estimate the power ratio epsilon from the median coherence
    fsolve_array = fsolve(
        residual_median_coherence,
        [initial_power_ratio],
        args=(median_coherence_estimated),
    )
    power_ratio = fsolve_array[0]

    # Find the bias factor
    bias = bias_from_median_coherence_and_power_ratio(
        median_coherence_estimated, power_ratio
    )
    return bias


def biases_from_median_coherences(median_coherences, initial_power_ratios=None):
    """Returns array of CSD mean-to-median biases from an array of median_coherences.
    Inputs:
    median_coherences =    median-averaged coherences
    initial_power_ratios =  power ratios to start estimation with.
                            If None, uses 0.1 for all.  Default is None.
    Outputs:
    biases =    array of biases calculated from the coherences

    Example:
    Sxxs = get_all_psds(x)
    Syys = get_all_psds(y)
    Sxys = get_all_csds(x, y)

    Sxx_med = get_median_psd(Sxxs)
    Syy_med = get_median_psd(Syys)
    Sxy_med = get_median_csd(Sxys)

    cohs_med = get_coherence(Sxx_med, Syy_med, Sxy_med)
    biases = biases_from_coherences(cohs_med)

    Sxy_med_bias_corrected = Sxy_med / biases
    """
    if initial_power_ratios is None:
        initial_power_ratios = 0.1 * np.ones_like(median_coherences)
    biases = np.array([])
    for coherence, initial_power_ratio in zip(median_coherences, initial_power_ratios):
        bias = bias_from_median_coherence(
            coherence, initial_power_ratio=initial_power_ratio
        )
        biases = np.append(biases, bias)
    return biases


### Modify data based on thresholds
def coherence_threshold_applier(coherences, coherence_threshold=0.9):
    """Apply a coherence threshold to a vector.
    Returns all indicies of the vector above the threshold
    """
    good_indices = np.argwhere(coherences > coherence_threshold)[:, 0]
    return good_indices


def bandlimit_applier(fff, bandlimit_low, bandlimit_high):
    """Cut off the low and high frequencies from a fff.
    Returns the valid indices.
    """
    good_high_indices = np.argwhere(fff > bandlimit_low)[:, 0]
    good_low_indices = np.argwhere(fff < bandlimit_high)[:, 0]
    good_indices = np.intersect1d(good_high_indices, good_low_indices)
    return good_indices


# ZPK frequency responses
def zpk_freq_resp(ff, z, p, k):
    """Takes in a frequency vector, and a zpk.
    Returns the frequency response.
    Use tf_zpk instead, works for old python scipy.signal libraries."""
    ww = 2 * np.pi * ff
    z *= -2 * np.pi
    p *= -2 * np.pi
    k *= np.abs(np.prod(p) / np.prod(z))
    ww, hh = sig.freqs_zpk(z, p, k, worN=ww)
    return hh


def tf_zpk(freq, f_zeros, f_poles, gain=1.0, absval=False, input_units="n"):
    """Compute frequency response of ZPK filter

    inputUnits is the type of TF we want to implement based on foton options:
    'n' is default, and stands for normalized.  This means the gain is
    normalized by the product of the poles over the product of zeros.
    'f' is the Hz interpretation, the poles and zeros are multiplied by -1 and
    the gain is not normalized.
    's' is the rad/s interpretation, the poles and zeros are multiplied by -2*pi
    and the gain is not normalized.

    """
    f_zeros = np.array(f_zeros)
    f_poles = np.array(f_poles)

    if input_units == "n":
        z = -2 * np.pi * f_zeros
        p = -2 * np.pi * f_poles

        k = (
            np.abs(np.prod(p[p != 0]) / np.prod(z[z != 0]))
            * ((2 * np.pi) ** p[p == 0].size)
            / ((2 * np.pi) ** z[z == 0].size)
            * gain
        )
    elif input_units == "f":
        z = 2 * np.pi * f_zeros
        p = 2 * np.pi * f_poles
        k = gain
    elif input_units == "s":
        z = f_zeros
        p = f_poles
        k = gain
    else:
        # don't allow any case to go uncaught
        assert False

    w = 2 * np.pi * freq
    # tf = scipy.signal.freqs_zpk(z, p, k, worN=w)[1]
    b, a = sig.zpk2tf(z, p, k)
    tf = sig.freqs(b, a, worN=w)[1]
    if absval:
        tf = np.abs(tf)

    return tf


def get_complex_interp(x2, x1, y1, **kwargs):
    """Interpolates a complex vector y1 from x1 to x2.
    Courtesy of Evan Hall."""
    re2 = np.interp(x2, x1, np.real(y1), **kwargs)
    im2 = np.interp(x2, x1, np.imag(y1), **kwargs)
    return re2 + 1j * im2


def RMS(freq, spec):
    """Takes in frequency vector and ASD, returns the RMS from high to low freq"""
    return cummulative_rms(freq, spec**2, reversed=True)


def cummulative_rms(ff, psd, reversed=True):
    """Cummulative root mean squared from a power spectral density.

    Inputs:
    -------
    ff: array
        frequency vector
    psd: array
        measured power spectral density in V**2/Hz
    reversed: boolean
        which way to cummulatively sum over the frequency vector

    Output:
    -------
    rms: array
        cummulative root mean squared vector in the order specified,
        with results in units of V
    """
    if reversed:
        psd = np.flip(psd)

    mean_squared = sciint.cumtrapz(psd, x=ff, initial=0)
    cummulative_rms = np.sqrt(mean_squared)

    if reversed:
        cummulative_rms = np.flip(cummulative_rms)

    return cummulative_rms


def simple_OLG(fff, UGF):
    """Given a frequency vector and unity gain frequency, returns a simple 1/f OLG"""
    return UGF / fff


# Logbinning
def resampling_matrix_nonuniform(lorig, lresam, extrap=False):
    """
    Logbinning stolen from some astro people: https://pypi.org/project/PySTARLIGHT/

    Compute resampling matrix R_o2r, useful to convert a spectrum sampled at
    wavelengths lorig to a new grid lresamp. Here, there is no necessity to have constant gris as on :py:func:`ReSamplingMatrix`.
    Input arrays lorig and lresamp are the bin centres of the original and final lambda-grids.
    ResampMat is a Nlresamp x Nlorig matrix, which applied to a vector F_o (with Nlorig entries) returns
    a Nlresamp elements long vector F_r (the resampled spectrum):

        [[ResampMat]] [F_o] = [F_r]

    Warning! lorig and lresam MUST be on ascending order!


    Parameters
    ----------
    lorig : array_like
            Original spectrum lambda array.

    lresam : array_like
             Spectrum lambda array in which the spectrum should be sampled.

    extrap : boolean, optional
           Extrapolate values, i.e., values for lresam < lorig[0]  are set to match lorig[0] and
                                     values for lresam > lorig[-1] are set to match lorig[-1].


    Returns
    -------
    ResampMat : array_like
                Resample matrix.

    Examples
    --------
    >>> lorig = np.linspace(3400, 8900, 9000) * 1.001
    >>> lresam = np.linspace(3400, 8900, 5000)
    >>> forig = np.random.normal(size=len(lorig))**2
    >>> matrix = slut.resampling_matrix_nonuniform(lorig, lresam)
    >>> fresam = np.dot(matrix, forig)
    >>> print np.trapz(forig, lorig), np.trapz(fresam, lresam)
    """

    # Init ResampMatrix
    matrix = np.zeros((len(lresam), len(lorig)))

    # Define lambda ranges (low, upp) for original and resampled.
    lo_low = np.zeros(len(lorig))
    lo_low[1:] = (lorig[1:] + lorig[:-1]) / 2
    lo_low[0] = lorig[0] - (lorig[1] - lorig[0]) / 2

    lo_upp = np.zeros(len(lorig))
    lo_upp[:-1] = lo_low[1:]
    lo_upp[-1] = lorig[-1] + (lorig[-1] - lorig[-2]) / 2

    lr_low = np.zeros(len(lresam))
    lr_low[1:] = (lresam[1:] + lresam[:-1]) / 2
    lr_low[0] = lresam[0] - (lresam[1] - lresam[0]) / 2

    lr_upp = np.zeros(len(lresam))
    lr_upp[:-1] = lr_low[1:]
    lr_upp[-1] = lresam[-1] + (lresam[-1] - lresam[-2]) / 2

    # Iterate over resampled lresam vector
    for i_r in range(len(lresam)):

        # Find in which bins lresam bin within lorig bin
        bins_resam = np.where((lr_low[i_r] < lo_upp) & (lr_upp[i_r] > lo_low))[0]

        # On these bins, eval fraction of resamled bin is within original bin.
        for i_o in bins_resam:

            aux = 0

            d_lr = lr_upp[i_r] - lr_low[i_r]
            d_lo = lo_upp[i_o] - lo_low[i_o]
            d_ir = lo_upp[i_o] - lr_low[i_r]  # common section on the right
            d_il = lr_upp[i_r] - lo_low[i_o]  # common section on the left

            # Case 1: resampling window is smaller than or equal to the original window.
            # This is where the bug was: if an original bin is all inside the resampled bin, then
            # all flux should go into it, not then d_lr/d_lo fraction. --Natalia@IoA - 21/12/2012
            if (lr_low[i_r] > lo_low[i_o]) & (lr_upp[i_r] < lo_upp[i_o]):
                aux += 1.0

            # Case 2: resampling window is larger than the original window.
            if (lr_low[i_r] < lo_low[i_o]) & (lr_upp[i_r] > lo_upp[i_o]):
                aux += d_lo / d_lr

            # Case 3: resampling window is on the right of the original window.
            if (lr_low[i_r] > lo_low[i_o]) & (lr_upp[i_r] > lo_upp[i_o]):
                aux += d_ir / d_lr

            # Case 4: resampling window is on the left of the original window.
            if (lr_low[i_r] < lo_low[i_o]) & (lr_upp[i_r] < lo_upp[i_o]):
                aux += d_il / d_lr

            matrix[i_r, i_o] += aux

    # Fix matrix to be exactly = 1 ==> TO THINK
    # print np.sum(matrix), np.sum(lo_upp - lo_low), (lr_upp - lr_low).shape

    # Fix extremes: extrapolate if needed
    if extrap:

        bins_extrapl = np.where((lr_low < lo_low[0]))[0]
        bins_extrapr = np.where((lr_upp > lo_upp[-1]))[0]

        if (len(bins_extrapl) > 0) & (len(bins_extrapr) > 0):
            io_extrapl = np.where((lo_low >= lr_low[bins_extrapl[0]]))[0][0]
            io_extrapr = np.where((lo_upp <= lr_upp[bins_extrapr[0]]))[0][-1]

            matrix[bins_extrapl, io_extrapl] = 1.0
            matrix[bins_extrapr, io_extrapr] = 1.0

    return matrix


def logbin_psd(log_ff, linear_ff, linear_psd):
    """Logbins a power spectral density given some log spaced frequency vector.
    Inputs:
    -------
    log_ff is the final vector we want the PSD to be spaced at
    linear_ff is the original frequency vector
    linear_psd is the linear power spectral density to logbin
    """
    matrix = resampling_matrix_nonuniform(linear_ff, log_ff)
    log_psd = np.dot(matrix, linear_psd)
    return log_psd


def linear_log_psd(log_ff, linear_ff, linear_psd):
    """
    Creates a linear- and log-binned power spectral density vector from overlapping linear and log frequency vectors,
    such that the coarsest frequency vector is used.
    This avoids the problem of logbinning where the low frequency points have too
    much resolution, i.e. the FFT binwidth > log_ff[1] - log_ff[0].

    Inputs:
    -------
    linear_ff  = linear frequency vector. Will be used for low frequency points.
    log_ff     = log frequency vector.  Will be used for high frequency points.
    linear_psd = linear power spectral density. Should be the same length as linear_ff, usual output of scipy.signal.welch().

    Outputs:
    --------
    fff = stitched frequency vector of linear and log points
    linlog_psd = stitched PSD of linear and log points
    """
    df = linear_ff[1] - linear_ff[0]
    dfflog = np.diff(log_ff)
    log_index = np.argwhere(dfflog > df)[0][
        0
    ]  # first point where fflog has less resolution than the normal freq vector
    cutoff = log_ff[log_index]  # cutoff frequency
    high_fff = log_ff[log_index + 1 :]

    # find where the cutoff frequency is first less than the linear frequency vector
    linear_index = np.argwhere(cutoff < linear_ff)[0][0]
    low_fff = linear_ff[:linear_index]
    low_psd = linear_psd[:linear_index]

    fff = np.concatenate((low_fff, high_fff))  # make the full frequency vector

    matrix = resampling_matrix_nonuniform(linear_ff, high_fff)
    high_psd = np.dot(matrix, linear_psd)  # get HF part of spectrum

    linlog_psd = np.concatenate((low_psd, high_psd))

    return fff, linlog_psd


### Conditioned spectra calculations
def calculate_coherence(psd_a, psd_b, csd_ab):
    """Calculates the power coherence gamma^2(f) between two signals a, b.

    Inputs:
    -------
    psd_a: array
        power spectral density of input signal of interest a <a, a>
    psd_b: array
        power spectral density of output signal of interest b <b, b>
    csd_ab: array
        cross spectral density between signals a and b <a, b>

    Output:
    -------
    coh: array
        power coherence gamma^2 between a and b, |<a,b>|^2 / (<a,a> * <b,b>)
    """
    coh = (np.abs(csd_ab) / (np.sqrt(psd_a) * np.sqrt(psd_b))) ** 2
    return coh


def calculate_conditioned_psd(psd, coh):
    """Calculates the conditioned power spectral density of the signal producing psd,
    while removing the influence of another signal coherent with the psd signal.

    Inputs:
    -------
    psd: array
        power spectral density we want to remove another signal from
    coh: array
        power coherence between the psd signal and the signal we want to remove

    Outputs:
    --------
    conditioned_psd: array
        power spectral density of the psd signal without the (linear) influence of the coherent signal
    """
    conditioned_psd = psd * (1 - coh)
    return conditioned_psd


def calculate_conditioned_csd(csd_ab, csd_ae, csd_be, psd_e):
    """Calculates the conditioned cross spectral density between two signals of interest a and b,
    while removing the influence of another signal, e, coherent with both signals.

    Inputs:
    -------
    csd_ab: array
        cross spectral density between signals a and b <a, b>
    csd_ae: array
        cross spectral density between signals a and e <a, e>
    csd_be: array
        cross spectral density between signals b and e <b, e>
    psd_e: array
        power spectral density of signal to be removed e <e, e>

    Outputs:
    --------
    conditioned_csd_ab: array
        cross spectral density between signals a and b <a, b> without the influence of the signal e
    """
    conditioned_csd_ab = csd_ab - csd_ae * np.conj(csd_be) / psd_e
    return conditioned_csd_ab


def calculate_conditioned_tf(csd_ab, csd_ae, csd_be, psd_e, psd_a):
    """Calculates the conditioned transfer function b/a between two signals of interest a and b,
    while removing the influence of another signal, e, coherent with both signals.

    Inputs:
    -------
    csd_ab: array
        cross spectral density between signals a and b <a, b>
    csd_ae: array
        cross spectral density between signals a and e <a, e>
    csd_be: array
        cross spectral density between signals b and e <b, e>
    psd_e: array
        power spectral density of signal to be removed e <e, e>
    psd_a: array
        power spectral density of input signal of interest a <a, a>

    Outputs:
    --------
    conditioned_tf: array
        transfer function between signals a and b <a, b> without the influence of the signal e
    """
    coh_ae = calculate_coherence(psd_a, psd_e, csd_ae)
    conditioned_psd_a = calculate_conditioned_psd(psd_a, coh_ae)
    conditioned_csd_ab = calculate_conditioned_csd(csd_ab, csd_ae, csd_be, psd_e)

    conditioned_tf = conditioned_csd_ab / conditioned_psd_a
    return conditioned_tf


def calculate_partial_coherence(csd_ab, csd_ae, csd_be, psd_e, psd_a, psd_b):
    """Calculates the conditioned transfer function b/a between two signals of interest a and b,
    while removing the influence of another signal, e, coherent with both signals.

    Inputs:
    -------
    csd_ab: array
        cross spectral density between signals a and b <a, b>
    csd_ae: array
        cross spectral density between signals a and e <a, e>
    csd_be: array
        cross spectral density between signals b and e <b, e>
    psd_e: array
        power spectral density of signal to be removed e <e, e>
    psd_a: array
        power spectral density of input signal of interest a <a, a>
    psd_b: array
        power spectral density of output signal of interest a <b, b>

    Outputs:
    --------
    partial_coherence: array
        partial coherence between signals a and b without the influence of the signal e
    """
    coh_ae = calculate_coherence(psd_a, psd_e, csd_ae)
    coh_be = calculate_coherence(psd_b, psd_e, csd_be)

    conditioned_psd_a = calculate_conditioned_psd(psd_a, coh_ae)
    conditioned_psd_b = calculate_conditioned_psd(psd_b, coh_be)
    conditioned_csd_ab = calculate_conditioned_csd(csd_ab, csd_ae, csd_be, psd_e)

    partial_coherence = calculate_coherence(
        conditioned_psd_a, conditioned_psd_b, conditioned_csd_ab
    )
    return partial_coherence


def get_conditioned_psd(data_dict, psd_chan, exc_chan):
    """
    Gets a conditioned power spectral density from the data_dict structure.
    The linear influence of exc_chan will be removed from the PSD of psd_chan.

    Inputs:
    -------
    data_dict: nds2 data dictionary struture
        dict with channel names as keys and channel info and data as values
    psd_chan: string
        channel name (key in data_dict) from which we want to subtract the influence of exc_chan
    exc_chan: string
        channel name (key in data_dict) whose linear influence we seek to remove from psd_chan's PSD

    Output:
    -------
    conditioned_psd: array
        power spectral density of psd_chan without the (linear) influence of exc_chan
    """
    if not "coh" in data_dict[psd_chan][exc_chan].keys():
        print(f"Coherence between {psd_chan} and {exc_chan} not yet calculated")
        print(
            f"Make sure coherence is calculated for data_dict[{psd_chan}][{exc_chan}]"
        )
        return data_dict

    # Get the sampling frequencies
    fs = data_dict[exc_chan]["fs"]
    fs2 = data_dict[psd_chan]["fs"]

    # If the sampling frequencies are not the same we may have to use the decimated PSD
    if fs < fs2:
        decimated_fs = fs
        psd = data_dict[psd_chan]["decimation"][decimated_fs]["PSD"]
        if not "coh" in data_dict[psd_chan][exc_chan]["decimation"][decimated_fs]:
            averages = data_dict[psd_chan]["averages"]
            bandwidth = data_dict[psd_chan]["binwidth"]
            overlap = data_dict[psd_chan]["overlap"]
            data_dict = calc_decimated_tf(
                data_dict,
                psd_chan,
                exc_chan,
                decimated_fs,
                averages,
                bandwidth,
                overlap,
            )

        coh = data_dict[psd_chan][exc_chan]["decimation"][decimated_fs]["coh"]

    else:
        psd = data_dict[psd_chan]["PSD"]
        coh = data_dict[psd_chan][exc_chan]["coh"]

    conditioned_psd = calculate_conditioned_psd(psd, coh)
    return conditioned_psd


def get_conditioned_csd(data_dict, chan_a, chan_b, exc_chan):
    """
    Calculates a conditioned cross spectral density from the data_dict structure.
    The linear influence of exc_chan will be removed from the CSD of chan_a and chan_b.

    Inputs:
    -------
    data_dict: nds2 data dictionary struture
        dict with channel names as keys and channel info and data as values
    chan_a: string
        channel name (key in data_dict) from whose CSD with chan_b we want to subtract the influence of exc_chan
    chan_b: string
        channel name (key in data_dict) from whose CSD with chan_a we want to subtract the influence of exc_chan
    exc_chan: string
        channel name (key in data_dict) whose linear influence we seek to remove from psd_chan's PSD

    Output:
    -------
    conditioned_csd: array
        cross spectral density of chan_a and chan_b without the (linear) influence of exc_chan
    """
    if not "coh" in data_dict[chan_b][chan_a].keys():
        print(f"Coherence between {chan_b} and {chan_a} not yet calculated")
        print(f"Make sure coherence is calculated for data_dict[{chan_b}][{chan_a}]")
        return data_dict

    # Get the sampling frequencies
    fs_a = data_dict[chan_a]["fs"]
    fs_b = data_dict[chan_b]["fs"]
    fs_e = data_dict[exc_chan]["fs"]

    # If all sampling frequencies are not equal
    if fs_a != fs_b or fs_a != fs_e or fs_b != fs_e:
        averages = data_dict[exc_chan]["averages"]
        bandwidth = data_dict[exc_chan]["binwidth"]
        overlap = data_dict[exc_chan]["overlap"]
        decimated_fs = min([fs_a, fs_b, fs_e])

    if fs_e != decimated_fs and check_if_decimated_psd_taken(
        data_dict, exc_chan, decimated_fs
    ):
        data_dict = calc_decimated_psd(
            data_dict, exc_chan, decimated_fs, averages, bandwidth, overlap
        )

    else:
        psd_e = data_dict[exc_chan]["PSD"]

    csd_ab = data_dict[chan_b][chan_a]["CSD"]  # S_ab
    csd_ae = data_dict[exc_chan][chan_a]["CSD"]  # S_ae
    csd_be = data_dict[exc_chan][chan_b]["CSD"]  # S_be

    conditioned_csd = calculate_conditioned_csd(csd_ab, csd_ae, csd_be, psd_e)
    return conditioned_csd


def get_conditioned_tf(data_dict, chan_a, chan_b, exc_chan):
    """
    Calculates a conditioned transfer function from the data_dict structure.
    The linear influence of exc_chan will be removed from the TF from chan_a to chan_b.

    Inputs:
    -------
    data_dict: nds2 data dictionary struture
        dict with channel names as keys and channel info and data as values
    chan_a: string
        channel name (key in data_dict) from whose CSD with chan_b we want to subtract the influence of exc_chan
    chan_b: string
        channel name (key in data_dict) from whose CSD with chan_a we want to subtract the influence of exc_chan
    exc_chan: string
        channel name (key in data_dict) whose linear influence we seek to remove from psd_chan's PSD

    Output:
    -------
    conditioned_tf: array
        transfer function from chan_a to chan_b without the (linear) influence of exc_chan
    """
    if not "CSD" in data_dict[psd_chan][exc_chan].keys():
        print("Cross spectral densities not yet calculated")
        print(
            f"Make sure CSDs and PSDs are calculated for data_dict[{psd_chan}] and data_dict[{exc_chan}]"
        )
        return data_dict

    # Gather spectra
    psd_a = data_dict[chan_a]["PSD"]
    psd_e = data_dict[exc_chan]["PSD"]

    csd_ab = data_dict[chan_b][chan_a]["CSD"]  # S_ab
    csd_ae = data_dict[exc_chan][chan_a]["CSD"]  # S_ae
    csd_be = data_dict[exc_chan][chan_b]["CSD"]  # S_be

    conditioned_tf = calculate_conditioned_tf(csd_ab, csd_ae, csd_be, psd_e, psd_a)
    return conditioned_tf


def get_partial_coherence(data_dict, chan_a, chan_b, exc_chan):
    """
    Calculates a partial coherence from the data_dict structure.
    The linear influence of exc_chan will be removed from the CSD of chan_a and chan_b to reproduce the coherence estimate.

    Inputs:
    -------
    data_dict: nds2 data dictionary struture
        dict with channel names as keys and channel info and data as values
    chan_a: string
        channel name (key in data_dict) from whose CSD with chan_b we want to subtract the influence of exc_chan
    chan_b: string
        channel name (key in data_dict) from whose CSD with chan_a we want to subtract the influence of exc_chan
    exc_chan: string
        channel name (key in data_dict) whose linear influence we seek to remove from psd_chan's PSD

    Output:
    -------
    partial_coherence: array
        partial coherence between chan_a and chan_b without the (linear) influence of exc_chan
    """
    if not "CSD" in data_dict[psd_chan][exc_chan].keys():
        print("Cross spectral densities not yet calculated")
        print(
            f"Make sure CSDs and PSDs are calculated for data_dict[{psd_chan}] and data_dict[{exc_chan}]"
        )
        return data_dict

    # Gather spectra
    psd_a = data_dict[chan_a]["PSD"]
    psd_b = data_dict[chan_b]["PSD"]
    psd_e = data_dict[exc_chan]["PSD"]

    csd_ab = data_dict[chan_b][chan_a]["CSD"]  # S_ab
    csd_ae = data_dict[exc_chan][chan_a]["CSD"]  # S_ae
    csd_be = data_dict[exc_chan][chan_b]["CSD"]  # S_be

    partial_coherence = calculate_partial_coherence(
        csd_ab, csd_ae, csd_be, psd_e, psd_a, psd_b
    )
    return partial_coherence


def check_if_decimated_psd_taken(data_dict, chan, decimated_fs):
    """
    Checks to ensure the decimated sampling frequency PSD for a channel
    has been taken already.
    Returns "True" if data_dict[chan]["decimation"][decimated_fs]["PSD"] exists,
    or if the main data_dict[chan]["PSD"] is already the correct frequency.

    Inputs:
    -------
    data_dict: nds2 data dictionary struture
        dict with channel names as keys and channel info and data as values
    chan: string
        channel name (key in data_dict) from whose CSD with chan_b we want to subtract the influence of exc_chan
    decimated_fs: int
        sampling frequency to decimate to in Hertz

    Output:
    -------
    decimated_psd_taken: boolean
        Returns True if the psd has been taken, False if not
    """
    decimated_psd_taken = True

    # First, check if decimation is even necessary
    fs = data_dict[chan]["fs"]
    if fs == decimated_fs:
        if "PSD" in data_dict[chan_a][chan_b].keys():
            return decimated_psd_taken

    # If no decimation has happened
    if not "decimation" in data_dict[chan].keys():
        decimated_psd_taken = False
    # if some decimation has happened, but not at the right frequency
    elif not decimated_fs in data_dict[chan]["decimation"].keys():
        decimated_psd_taken = False
    # if the psd is taken
    elif not "PSD" in data_dict[chan]["decimation"][decimated_fs].keys():
        decimated_psd_taken = False

    return decimated_psd_taken


def check_if_decimated_csd_taken(data_dict, chan_a, chan_b, decimated_fs):
    """
    Checks to ensure the decimated sampling frequency CSD for a channel
    has been taken already.
    Returns "True" if data_dict[chan_a][chan_b]["decimation"][decimated_fs]["CSD"] exists,
    or if the main data_dict[chan_a][chan_b]["CSD"] is already the correct frequency.

    Inputs:
    -------
    data_dict: nds2 data dictionary struture
        dict with channel names as keys and channel info and data as values
    chan_a: string
        channel name (key in data_dict) from whose CSD with chan_b we want to subtract the influence of exc_chan
    chan_b: string
        channel name (key in data_dict) from whose CSD with chan_a we want to subtract the influence of exc_chan
    decimated_fs: int
        sampling frequency to decimate to in Hertz

    Output:
    -------
    decimated_csd_taken: boolean
        Returns True if the psd has been taken, False if not
    """
    decimated_csd_taken = True

    # First, check if decimation is even necessary
    fs_a = data_dict[chan_a]["fs"]
    fs_b = data_dict[chan_b]["fs"]
    if fs_a == decimated_fs and fs_b == decimated_fs:
        if "CSD" in data_dict[chan_a][chan_b].keys():
            return decimated_psd_taken

    # If no decimation has happened
    if not "decimation" in data_dict[chan_a][chan_b].keys():
        decimated_csd_taken = False
    # if some decimation has happened, but not at the right frequency
    elif not decimated_fs in data_dict[chan_a][chan_b]["decimation"].keys():
        decimated_csd_taken = False
    # if the csd is taken
    elif not "CSD" in data_dict[chan_a][chan_b]["decimation"][decimated_fs].keys():
        decimated_csd_taken = False

    return decimated_csd_taken


def get_decimated_psd(
    data_dict, chan, decimated_fs, averages=None, bandwidth=1.0, overlap=0.0
):
    """
    Gets the decimated sampling frequency PSD for a channel
    has been taken already.
    Returns the PSD at the decimated frequency specified.

    If you specify the averages, you should also specify the bandwidth and overlap.
    If you aren't careful, the decimated PSDs will have different bandwidths, making comparisons fail.
    By default this function will try to keep bandwidths consistent.

    Inputs:
    -------
    data_dict: nds2 data dictionary struture
        dict with channel names as keys and channel info and data as values
    chan: string
        channel name (key in data_dict) from whose CSD with chan_b we want to subtract the influence of exc_chan
    decimated_fs: int
        sampling frequency to decimate to in Hertz
    averages: int
        number of power spectral densities to average together using Welch's method.
        Default is None, which will use number of averages in the data_dict already if possible,
        or else assume some number based on the time length of the data and default FFT bandwidth.
    bandwidth: float
        width of the FFT frequency bins in Hertz.
        Default is 1.0 Hz, only used if no PSDs have been calculated yet.
    overlap: float
        amount of overlap used with each FFT window.
        Default is 0.0, only used if no PSDs have been calculated yet.

    Output:
    -------
    decimated_psd: array
        power spectral density of the decimated data
    """
    fs = data_dict[chan]["fs"]
    if fs < decimated_fs:
        print(f"channel {chan} sampling frequency is {fs} Hz")
        print(f"requested decimation sampling frequency is {decimated_fs} Hz")
        print(f"Returning None")
        return

    decimated_psd_taken = check_if_decimated_psd_taken(data_dict, chan, decimated_fs)
    if not decimated_psd_taken:
        print(f"Decimated PSD for {chan} at {decimated_fs} Hz is not taken")
        print(f"Taking now")
        # If averages are None
        if not averages:
            if "averages" in data_dict[chan].keys():
                averages = data_dict[chan]["averages"]
                bandwidth = data_dict[chan]["binwidth"]
                overlap = data_dict[chan]["overlap"]
            else:
                time = len(data_dict[chan]["data"]) / fs
                averages = dtt_averages(time, bandwidth, overlap)
                print(
                    f"No PSDs in data_dict yet to use as reference for number of averages"
                )
                print(f"Using the following:")
                print(f"--------------------")
                print(f"averages = {averages}")
                print(f"bandwidth = {bandwidth} Hz")
                print(f"overlap = {overlap}")
                print()

        # Calculate the decimated PSD
        data_dict = calc_decimated_psd(
            data_dict, chan, decimated_fs, averages, bandwidth, overlap
        )

    # Grab the correct decimated (or regular) PSD
    if fs == decimated_fs:
        decimated_psd = data_dict[chan]["PSD"]
    elif fs > decimated_fs:
        decimated_psd = data_dict[chan]["decimation"][decimated_fs]["PSD"]

    return decimated_psd
