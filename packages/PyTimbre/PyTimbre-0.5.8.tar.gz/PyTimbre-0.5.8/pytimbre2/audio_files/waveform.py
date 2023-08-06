import math
import numpy as np
from datetime import datetime, timedelta
from enum import Enum
from scipy.signal.windows import hamming, tukey
import scipy.signal
import statsmodels.api as sm


class windowing_methods(Enum):
    """
    The available windowing methods for the waveform
    """

    hanning = 1
    hamming = 2
    tukey = 3
    rectangular = 4


class trimming_methods(Enum):
    """
    Trimming can be accomplished with either the samples or times. This enumeration defines whether to use the time to
    calculate the sample or just provide the samples.
    """

    samples = 1
    times = 2


class scaling_method(Enum):
    """
    In scaling the waveform we can apply the level changes in either decibels or linear values. This will determine how
    the interface scales the signal when manipulating the sample magnitudes.
    """

    linear = 1
    logarithmic = 2


class Waveform:
    """
    This is a generic base class that contains the start time, samples and sample rate for a waveform.  Some limited
    operations exist within this class for manipulation of the base data within the class.

    Remarks
    2022-05-11 - FSM - added the function to determine whether the waveform is a calibration signal or not.
    """

    def __init__(self, pressures, sample_rate, start_time):
        """
        Default constructor
        :param pressures: float, array-like - the list of pressure values
        :param sample_rate: float - the number of samples per second
        :param start_time: float or datetime - the time of the first sample
        """

        self._samples = pressures
        self._samples -= np.mean(self._samples)
        self.fs = sample_rate
        self.time0 = start_time
        self._forward_coefficients = None
        self._reverse_coefficients = None

        self._coefficient_count = 12
        self._hop_size_seconds = 0.0029
        self._window_size_seconds = 0.0232
        self._cutoff_frequency = 5
        self._centroid_threshold = 0.15
        self._effective_duration_threshold = 0.4

        self._signal_envelope = None
        self._normal_signal_envelope = None
        self._log_attack = None
        self._increase = None
        self._decrease = None
        self._Addresses = None
        self._amplitude_modulation = None
        self._frequency_modulation = None
        self._auto_correlation_coefficients = None
        self._zero_cross_rate = None
        self._temporal_centroid = None
        self._effective_duration = None
        self._temporal_feature_times = None

    # ---------------------- Collection of properties - this is both getters and setters -------------------------------

    @property
    def duration(self):
        """
        Determine the duration of the waveform by examining the number of samples and the sample rate
        :return: float - the total number of seconds within the waveform
        """
        return float(len(self._samples)) / self.fs

    @property
    def end_time(self):
        """
        Determine the end time - if the start time was a datetime, then this returns a datetime.  Otherwise a floating
        point value is returned
        :return: float or datetime - the end of the file
        """
        if isinstance(self.time0, datetime):
            return self.time0 + timedelta(seconds=self.duration)
        else:
            return self.time0 + self.duration

    @property
    def samples(self):
        """
        The actual pressure waveform
        :return: float, array-like - the collection of waveform data
        """
        return self._samples

    @samples.setter
    def samples(self, array):
        self._samples = array

    @property
    def sample_rate(self):
        """
        The number of samples per second to define the waveform.
        :return: float - the number of samples per second
        """
        return self.fs

    @sample_rate.setter
    def sample_rate(self, value):
        self.fs = value

    @property
    def start_time(self):
        """
        The time of the first sample
        :return: float or datetime - the time of the first sample
        """

        return self.time0

    @start_time.setter
    def start_time(self, value):
        self.time0 = value

    @property
    def forward_coefficients(self):
        return self._forward_coefficients

    @property
    def reverse_coefficients(self):
        return self._reverse_coefficients

    @property
    def times(self):
        """
        This determines the time past midnight for the start of the audio and returns a series of times for each sample
        :return: float, array-like - the sample times for each element of the samples array
        """

        if isinstance(self.start_time, datetime):
            t0 = (60 * (60 * self.start_time.hour + self.start_time.minute) + self.start_time.second +
                  self.start_time.microsecond * 1e-6)
        else:
            t0 = self.start_time

        return np.arange(0, len(self.samples)) / self.sample_rate + t0

    @property
    def effective_duration_threshold(self):
        return self._effective_duration_threshold

    @property
    def centroid_threshold(self):
        return self._centroid_threshold

    @property
    def cutoff_frequency(self):
        return self._cutoff_frequency

    @cutoff_frequency.setter
    def cutoff_frequency(self, value):
        self._cutoff_frequency = value

    @property
    def window_size_seconds(self):
        return self._window_size_seconds

    @window_size_seconds.setter
    def window_size_seconds(self, value):
        self._window_size_seconds = value

    @property
    def hop_size_seconds(self):
        return self._hop_size_seconds

    @hop_size_seconds.setter
    def hop_size_seconds(self, value):
        self._hop_size_seconds = value

    @property
    def window_size_samples(self):
        return int(np.round(self.window_size_seconds * self.sample_rate))

    @property
    def hop_size_samples(self):
        return int(round(self.hop_size_seconds * self.sample_rate))

    @property
    def coefficient_count(self):
        """
        The number of coefficients to generate for the available data
        """

        return self._coefficient_count

    @coefficient_count.setter
    def coefficient_count(self, value):
        """
        Set the number of coefficients for the analysis
        """

        self._coefficient_count = value

    @property
    def attack(self):
        if self._Addresses is None:
            self._calculate_signal_envelope()
            self._log_attack, self._increase, self._decrease, self._Addresses = self.calculate_log_attack()

        return self._Addresses[0]

    @property
    def decrease(self):
        if self._Addresses is None:
            self._calculate_signal_envelope()
            self._log_attack, self._increase, self._decrease, self._Addresses = self.calculate_log_attack()

        return self._Addresses[1]

    @property
    def release(self):
        if self._Addresses is None:
            self._calculate_signal_envelope()
            self._log_attack, self._increase, self._decrease, self._Addresses = self.calculate_log_attack()

        return self._Addresses[4]

    @property
    def log_attack(self):
        """
        The log-attack-time is simply defined as LAT = log_10(t[-1]-t[0])
        """
        if self._Addresses is None:
            self._calculate_signal_envelope()
            self._log_attack, self._increase, self._decrease, self._Addresses = self.calculate_log_attack()

        return self._log_attack

    @property
    def attack_slope(self):
        """
        The attack slope is defined as the average temporal slope of the energy during the attack segment. We compute
        the local slopes of the energy corresponding to each effort w_i. We then compute a weighted average of the
        slopes. The weights are chosen in order to emphasize slope values in the middle of the attack (the weights are
        the values of a Gaussian function centered around the threshold = 50% and with a standard-deviation of 0.5).
        """
        if self._Addresses is None:
            self._calculate_signal_envelope()
            self._log_attack, self._increase, self._decrease, self._Addresses = self.calculate_log_attack()

        return self._increase

    @property
    def decrease_slope(self):
        """
        The temporal decrease is a measure of the rate of decrease of the signal energy. It distinguishes non-sustained
        (e.g. percussive, pizzicato) sounds from sustained sounds. Its calculation is based on a decreasing exponential
        model of the energy envelope starting from it maximum.
        """
        if self._Addresses is None:
            self._calculate_signal_envelope()
            self._log_attack, self._increase, self._decrease, self._Addresses = self.calculate_log_attack()

        return self._decrease

    @property
    def temporal_centroid(self):
        """
        The temporal centroid is the center of gravity of the energy envelope. It distinguishes percussive from
        sustained sounds. It has been proven to be a perceptually important descriptor (Peeters et al., 2000).
        """
        if self._temporal_centroid is None:
            self._calculate_signal_envelope()
            self._temporal_centroid = self.calculate_temporal_centroid()

        return self._temporal_centroid

    @property
    def effective_duration(self):
        """
        The effective duration is a measure intended to reflect the perceived duration of the signal. It distinguishes
        percussive sounds from sustained sounds but depends on the event duration. It is approximated by the time the
        energy envelop is above a given threshold. After many empirical tests, we have set this threshold to 40%
        """
        if self._effective_duration is None:
            self._calculate_signal_envelope()
            self._effective_duration = self.calculate_effective_duration()

        return self._effective_duration

    @property
    def amplitude_modulation(self):
        if self._amplitude_modulation is None:
            self._calculate_signal_envelope()
            self._log_attack, self._increase, self._decrease, self._Addresses = self.calculate_log_attack()
            self._frequency_modulation, self._amplitude_modulation = self.calculate_modulation()
        return self._amplitude_modulation

    @property
    def frequency_modulation(self):
        if self._frequency_modulation is None:
            self._calculate_signal_envelope()
            self._log_attack, self._increase, self._decrease, self._Addresses = self.calculate_log_attack()
            self._frequency_modulation, self._amplitude_modulation = self.calculate_modulation()
        return self._frequency_modulation

    @property
    def auto_correlation(self):
        if self._auto_correlation_coefficients is None:
            self._temporal_feature_times, self._auto_correlation_coefficients, self._zero_cross_rate = \
                self.instantaneous_temporal_features()
        return self._auto_correlation_coefficients

    @property
    def zero_crossing_rate(self):
        if self._zero_cross_rate is None:
            self._temporal_feature_times, self._auto_correlation_coefficients, self._zero_cross_rate = \
                self.instantaneous_temporal_features()
        return self._zero_cross_rate

    @property
    def temporal_feature_times(self):
        if self._temporal_feature_times is None:
            self._temporal_feature_times, self._auto_correlation_coefficients, self._zero_cross_rate = \
                self.instantaneous_temporal_features()
        return self._temporal_feature_times

    @property
    def signal_envelope(self):
        if self._signal_envelope is None:
            self._calculate_signal_envelope()

        return self._signal_envelope

    @property
    def normal_signal_envelope(self):
        if self._normal_signal_envelope is None:
            self._calculate_signal_envelope()

        return self._normal_signal_envelope

    @property
    def loudness(self):
        from mosqito.sq_metrics import loudness_zwst_perseg
        return loudness_zwst_perseg(signal=self.samples, fs=self.sample_rate)[0]

    @property
    def roughness(self):
        from mosqito.sq_metrics import roughness_dw

        return roughness_dw(signal=self.samples, fs=self.sample_rate)[0]

    @property
    def sharpness(self):
        from mosqito.sq_metrics import sharpness_din_perseg

        return sharpness_din_perseg(signal=self.samples, fs=self.sample_rate)[0]

    # ------------------ Static functions for the calculation of filter shapes and timbre features ---------------------

    @staticmethod
    def AC_Filter_Design(fs):
        """
        AC_Filter_Design.py

        Created on Mon Oct 18 19:27:36 2021

        @author: Conner Campbell, Ball Aerospace

        Description
        ----------
        Coeff_A, Coeff_C = AC_Filter_Design(fs)

        returns Ba, Aa, and Bc, Ac which are arrays of IRIR filter
        coefficients for A and C-weighting.  fs is the sampling
        rate in Hz.

        This progam is a recreation of adsgn and cdsgn
        by Christophe Couvreur, see	Matlab FEX ID 69.


        Parameters
        ----------
        fs : double
            sampling rate in Hz

        Returns
        -------

        Coeff_A: list
            List of two numpy arrays, feedforward and feedback filter
            coeffecients for A-weighting filter. Form of lits is [Ba,Aa]

        Coeff_c: list
            List of two numpy arrays, feedforward and feedback filter
            coeffecients for C-weighting filter. Form of lits is [Bc,Ac]

        Code Dependencies
        -------
        This program requires the following python packages:
        scipy.signal, numpy

        References
        -------
        IEC/CD 1672: Electroacoustics-Sound Level Meters, Nov. 1996.

        ANSI S1.4: Specifications for Sound Level Meters, 1983.

        ACdsgn.m: Christophe Couvreur, Faculte Polytechnique de Mons (Belgium)
        couvreur@thor.fpms.ac.be
        """

        # Define filter poles for A/C weight IIR filter according to IEC/CD 1672

        f1 = 20.598997
        f2 = 107.65265
        f3 = 737.86223
        f4 = 12194.217
        A1000 = 1.9997
        C1000 = 0.0619
        pi = np.pi

        # Calculate denominator and numerator of filter tranfser functions

        coef1 = (2 * pi * f4) ** 2 * (10 ** (C1000 / 20))
        coef2 = (2 * pi * f4) ** 2 * (10 ** (A1000 / 20))

        Num1 = np.array([coef1, 0.0])
        Den1 = np.array([1, 4 * pi * f4, (2 * pi * f4) ** 2])

        Num2 = np.array([1, 0.0])
        Den2 = np.array([1, 4 * pi * f1, (2 * pi * f1) ** 2])

        Num3 = np.array([coef2 / coef1, 0.0, 0.0])
        Den3 = scipy.signal.convolve(np.array([1, 2 * pi * f2]).T, (np.array([1, 2 * pi * f3])))

        # Use scipy.signal.bilinear function to get numerator and denominator of
        # the transformed digital filter transfer functions.

        B1, A1 = scipy.signal.bilinear(Num1, Den1, fs)
        B2, A2 = scipy.signal.bilinear(Num2, Den2, fs)
        B3, A3 = scipy.signal.bilinear(Num3, Den3, fs)

        Ac = scipy.signal.convolve(A1, A2)
        Aa = scipy.signal.convolve(Ac, A3)

        Bc = scipy.signal.convolve(B1, B2)
        Ba = scipy.signal.convolve(Bc, B3)

        Coeff_A = [Ba, Aa]
        Coeff_C = [Bc, Ac]
        return Coeff_A, Coeff_C

    @staticmethod
    def detect_local_extrema(input_v, lag_n):
        """
        This will detect the local maxima of the vector on the interval [n-lag_n:n+lag_n]

        Parameters
        ----------
        input_v : double array-like
            This is the input vector that we are examining to determine the local maxima
        lag_n : double, integer
            This is the number of samples that we are examining within the input_v to determine the local maximum

        Returns
        -------
        pos_max_v : double, array-like
            The locations of the local maxima
        """

        do_affiche = 0
        lag2_n = 4
        seuil = 0

        L_n = len(input_v)

        pos_cand_v = np.where(np.diff(np.sign(np.diff(input_v))) < 0)[0]
        pos_cand_v += 1

        pos_max_v = np.zeros((len(pos_cand_v),))

        for i in range(len(pos_cand_v)):
            pos = pos_cand_v[i]

            if (pos > lag_n) & (pos <= L_n - lag_n):
                tmp = input_v[pos - lag_n:pos + lag2_n]
                position = np.argmax(tmp)

                position = position + pos - lag_n - 1

                if (pos - lag2_n > 0) & (pos + lag2_n < L_n + 1):
                    tmp2 = input_v[pos - lag2_n:pos + lag2_n]

                    if (position == pos) & (input_v[position] > seuil * np.mean(tmp2)):
                        pos_max_v[i] = pos

        return pos_max_v

    @staticmethod
    def next_pow2(x: int):
        n = np.log2(x)
        return 2 ** (np.floor(n) + 1)

    # ---------------------------- Protected functions for feature calculation -----------------------------------------

    def _calculate_signal_envelope(self):
        #   Calculate the energy envelope of the signal that is required for many of the features

        analytic_signal = scipy.signal.hilbert(self.samples)
        amplitude_modulation = np.abs(analytic_signal)
        normalized_freq = self.cutoff_frequency / (self.sample_rate / 2)
        sos = scipy.signal.butter(3, normalized_freq, btype='low', analog=False, output='sos')
        self._signal_envelope = scipy.signal.sosfilt(sos, amplitude_modulation)

        #   Normalize the envelope

        self._normal_signal_envelope = self.signal_envelope / np.max(self.signal_envelope)

    def _trim_by_samples(self, s0: int = None, s1: int = None):
        """
        This function will trim the waveform and return a subset of the current waveform based on sample indices within
        the 'samples' property within this class.

        Parameters
        __________
        :param s0: int - the start sample of the trimming. If s0 is None, then interface will use the first sample
        :param s1: int - the stop sample of the trimming. If s1 is None, then the interface uses the last sample

        Returns
        _______
        :returns: Waveform - a subset of the waveform samples
        """

        #   Handle the start/stop samples may be passed as None arguments

        if s0 is None:
            s0 = 0

        if s1 is None:
            s1 = self._samples.shape[0]

        #   Determine the new start time of the waveform

        if isinstance(self.start_time, datetime):
            t0 = self.start_time + timedelta(seconds=s0 / self.sample_rate)
        else:
            t0 = self.start_time + s0 / self.sample_rate

        #   Create the waveform based on the new time, and the subset of the samples

        return Waveform(self.samples[np.arange(s0, s1)].copy(),
                        self.sample_rate,
                        t0)

    def _scale_waveform(self, scale_factor: float = 1.0, inplace: bool = False):
        """
        This function applies a scaling factor to the waveform's sample in a linear scale factor.

        Parameters
        __________
        :param scale_factor: float - the linear unit scale factor to change the amplitude of the sample values
        :param inplace: boolean - Whether to modify the samples within the current object, or return a new object

        Returns
        _______
        :returns: If inplace == True a new Waveform object with the sample magnitudes scaled, None otherwise
        """

        if inplace:
            self._samples *= scale_factor

            return None
        else:
            return Waveform(self._samples * scale_factor, self.sample_rate, self.start_time)

    # -------------------- Public functions for operations on the samples within the Waveform --------------------------

    def apply_calibration(self, wfm, level: float = 114, frequency: float = 1000, inplace: bool = False):
        return None

    def scale_signal(self, factor: float = 1.0, inplace: bool = False,
                     scale_type: scaling_method = scaling_method.linear):
        """
        This method will call the sub-function to scale the values of the waveform in linear fashion. If the scale
        factor is provided in logarithmic form, it will be converted to a linear value and sent to the sub-function.

        Parameters
        ----------
        :param factor: float - the scale factor that needs to be passed to the scaling sub-function
        :param inplace: bool - whether to manipulate the data within the current class, or return a new instance
        :param scale_type: scaling_method - how to apply the scaling to the signal

        Returns
        -------

        :returns: output of sub-function
        """

        scale_factor = factor

        if scale_type == scaling_method.logarithmic:
            scale_factor = 10**(scale_factor / 20)

        return self._scale_waveform(scale_factor, inplace)

    def trim(self, s0: float = 0.0, s1: float = None, method: trimming_methods = trimming_methods.samples):
        """
        This function will remove the samples before s0 and after s1 and adjust the start time
        :param s0: float - the sample index or time of the new beginning of the waveform
        :param s1: float - the sample index or time of the end of the new waveform
        :param method: trimming_methods - the method to trim the waveform
        :return: generic_time_waveform object
        """

        #   Determine whether to use the time or sample methods

        if method == trimming_methods.samples:
            return self._trim_by_samples(int(s0), int(s1))
        elif method == trimming_methods.times:
            t0 = s0
            t1 = s1

            s0 = (t0 * self.sample_rate)
            ds = (t1 - t0) * self.sample_rate
            s1 = s0 + ds

            return self._trim_by_samples(int(s0), int(s1))

    def apply_window(self, window: windowing_methods = windowing_methods.hanning, windowing_parameter=None):
        """
        This will apply a window with the specific method that is supplied by the window argument and returns a
        generic_time_waveform with the window applied

        :param window:windowing_methods - the enumeration that identifies what type of window to apply to the waveform
        :param windowing_parameter: int or float - an additional parameter that is required for the window
        :returns: generic_time_waveform - the waveform with the window applied
        """

        W = []

        if window == windowing_methods.tukey:
            W = tukey(len(self.samples), windowing_parameter)

        elif window == windowing_methods.rectangular:
            W = tukey(len(self.samples), 0)

        elif window == windowing_methods.hanning:
            W = tukey(len(self.samples), 1)

        elif window == windowing_methods.hamming:
            W = hamming(len(self.samples))

        return Waveform(self.samples * W, self.fs, self.start_time)

    def apply_iir_filter(self, b, a):
        """
        This function will be able to apply a filter to the samples within the file and return a new
        generic_time_waveform object

        :param b: double, array-like - the forward coefficients of the filter definition
        :param a: double, array-like - the reverse coefficients of the filter definition
        """

        self._forward_coefficients = b
        self._reverse_coefficients = a
        return Waveform(scipy.signal.lfilter(b, a, self.samples), self.sample_rate, self.start_time)

    def apply_a_weight(self):
        """
        This function specifically applies the a-weighting filter to the acoustic data, and returns a new waveform with
        the filter applied.

        :returns: generic_time_waveform - the filtered waveform
        """
        a, c = Waveform.AC_Filter_Design(self.sample_rate)

        return self.apply_iir_filter(a[0], a[1])

    def apply_c_weight(self):
        """
        This function specifically applies the a-weighting filter to the acoustic data, and returns a new waveform with
        the filter applied.

        :returns: generic_time_waveform - the filtered waveform
        """
        a, c = Waveform.AC_Filter_Design(self.sample_rate)

        return self.apply_iir_filter(c[0], c[1])

    def apply_lowpass(self, cutoff: float, order: int = 4):
        """
        This function applies a Butterworth filter to the samples within this class.

        :param cutoff: double - the true frequency in Hz
        :param order: double (default: 4) - the order of the filter that will be created and applied

        :returns: generic_time_waveform - the filtered waveform
        """

        #   Determine the nyquist frequency

        nyquist = self.sample_rate / 2.0

        #   Determine the normalized frequency

        normalized_cutoff = cutoff / nyquist

        #   Design the filter

        b, a = scipy.signal.butter(order, normalized_cutoff, btype='low', analog=False, output='ba')

        #   Filter the data and return the new waveform object

        return self.apply_iir_filter(b, a)

    def is_calibration(self):
        """
        This function examines the samples and determines whether the single contains a single pure tone.  If it does
        the function returns the approximate frequency of the tone.  This will examine every channel and determine
        whether each channel is a calibration tone

        :returns: bool - flag determining whether the signal was pure tone
                  float - the approximate frequency of the pure tone
        """

        calibration = None
        freq = None

        #   Loop through the channels

        #   To remove high frequency transients, we pass the signal through a 2 kHz low pass filter

        wfm = Waveform(self.samples, self.sample_rate, self.start_time)
        wfm.apply_lowpass(2000)

        peaks = scipy.signal.find_peaks(wfm.samples, height=0.8 * np.max(self.samples))[0]

        if len(peaks) >= 2:
            calibration = False
            freq = -1

            #   Determine the distance between any two adjacent peaks

            distance_sample = np.diff(peaks)

            #   Determine the distance between the samples in time

            distance_time = distance_sample / self.sample_rate

            #   Determine the frequencies

            frequencies = 1 / distance_time

            freq = np.mean(frequencies)

            calibration = (abs(freq - 1000) < 0.1 * 1000) or \
                          (abs(freq - 250) < 0.1 * 250)

        return calibration, freq

    def get_features(self, include_sq_metrics: bool = True):
        """
        This function calculates the various features within the global time analysis and stores the results in the
        class object.  At the end, a dictionary of the values is available and returned to the calling function.

        Returns
        -------
        features : dict()
            The dictionary containing the various values calculated within this method.
        """

        #   Create the dictionary that will hold the data for return to the user

        features = {'attack': self.attack,
                    'decrease': self.decrease,
                    'release': self.release,
                    'log_attack': self.log_attack,
                    'attack slope': self.attack_slope,
                    'decrease slope': self.decrease_slope,
                    'temporal centroid': self.temporal_centroid,
                    'effective duration': self.effective_duration,
                    'amplitude modulation': self.amplitude_modulation,
                    'frequency modulation': self.frequency_modulation,
                    'auto-correlation': self.auto_correlation,
                    'zero crossing rate': self.zero_crossing_rate}

        if include_sq_metrics:
            features['loudness'] = self.loudness
            features['roughness'] = self.roughness
            features['sharpness'] = self.sharpness

        return features

    def calculate_temporal_centroid(self):

        env_max_idx = np.argmax(self.signal_envelope)
        over_threshold_idcs = np.where(self.normal_signal_envelope > self.centroid_threshold)[0]

        over_threshold_start_idx = over_threshold_idcs[0]
        if over_threshold_start_idx == env_max_idx:
            over_threshold_start_idx = over_threshold_start_idx - 1

        over_threshold_end_idx = over_threshold_idcs[-1]

        over_threshold_TEE = self.signal_envelope[over_threshold_start_idx - 1:over_threshold_end_idx - 1]
        over_threshold_support = [*range(len(over_threshold_TEE))]
        over_threshold_mean = np.divide(np.sum(np.multiply(over_threshold_support, over_threshold_TEE)),
                                        np.sum(over_threshold_TEE))

        temporal_threshold = ((over_threshold_start_idx + 1 + over_threshold_mean) / self.sample_rate)

        return temporal_threshold

    def calculate_effective_duration(self):

        env_max_idx = np.argmax(self.signal_envelope)
        over_threshold_idcs = np.where(self.normal_signal_envelope > self.effective_duration_threshold)[0]

        over_threshold_start_idx = over_threshold_idcs[0]
        if over_threshold_start_idx == env_max_idx:
            over_threshold_start_idx = over_threshold_start_idx - 1

        over_threshold_end_idx = over_threshold_idcs[-1]

        return (over_threshold_end_idx - over_threshold_start_idx + 1) / self.sample_rate

    def rms_envelope(self):

        win_size = int(round(self._window_size_seconds * self.sample_rate))
        hop_size = int(round(self._hop_size_seconds * self.sample_rate))
        t_support = [*range(0, int(round(hop_size * np.floor((len(self.samples) - win_size) / hop_size))), hop_size)]
        value = []
        for i in range(len(t_support)):
            a = self.samples[np.subtract(np.add(t_support[i], [*range(1, win_size + 1)]), 1).astype(int)]
            value.append(np.sqrt(np.mean(np.power(a, 2))))
        t_support = np.divide(np.add(t_support, np.ceil(np.divide(win_size, 2))),
                              self.sample_rate)
        return value

    def instantaneous_temporal_features(self):
        """
        This function will calculate the instantaneous features within the temporal analysis.  This includes the
        auto-correlation and the zero crossing rate.
        """
        count = 0
        dAS_f_SupX_v_count = 0
        temporal_feature_times = np.zeros(
            (int(np.floor((len(self.samples) - self.window_size_samples) / self.hop_size_samples) + 1),))

        auto_coefficients = np.zeros((len(temporal_feature_times), self.coefficient_count))
        zero_crossing_rate = np.zeros((len(temporal_feature_times),))

        #   Loop through the frames

        for n in range(0, len(temporal_feature_times)):
            #   Get the frame

            frame_length = self.window_size_samples
            start = n * self.hop_size_samples
            frame_index = np.arange(start, frame_length + start)
            f_Frm_v = self.samples[frame_index] * np.hamming(self.window_size_samples)
            temporal_feature_times[n] = n * self.hop_size_seconds

            count += 1

            #   Calculate the auto correlation coefficients

            auto_coefficients[n, :] = sm.tsa.acf(f_Frm_v, nlags=self.coefficient_count, fft=False)[1:]

            #   Now the zero crossing rate

            i_Sign_v = np.sign(f_Frm_v - np.mean(f_Frm_v))
            i_Zcr_v = np.where(np.diff(i_Sign_v))[0]
            i_Num_Zcr = len(i_Zcr_v)
            zero_crossing_rate[n] = i_Num_Zcr / (len(f_Frm_v) / self.sample_rate)

        return temporal_feature_times, auto_coefficients, zero_crossing_rate

    def calculate_modulation(self):
        """
        Calculate the frequency/amplitude modulations of the signal.  This can be accomplished with either a Fourier or
        Hilbert method.

        Returns
        -------

        frequency_modulation : double
            A metric measuring the frequency modulation of the signal
        amplitude_modulation : double
            A metric measuring the amplitude modulation of the signal
        """

        sample_times = np.arange(len(self.signal_envelope) - 1) / self.sample_rate

        sustain_start_time = self._Addresses[1]
        sustain_end_time = self._Addresses[4]

        is_sustained = False

        if (sustain_end_time - sustain_start_time) > 0.02:
            pos_v = np.where((sustain_start_time <= sample_times) & (sample_times <= sustain_end_time))[0]
            if len(pos_v) > 0:
                is_sustained = True

        if not is_sustained:
            amplitude_modulation = 0
            frequency_modulation = 0
        else:
            envelop_v = self.signal_envelope[pos_v]
            temps_sec_v = sample_times[pos_v]
            M = np.mean(envelop_v)

            #   Taking the envelope

            mon_poly = np.polyfit(temps_sec_v, np.log(envelop_v), 1)
            hat_envelope_v = np.exp(np.polyval(mon_poly, temps_sec_v))
            signal_v = envelop_v - hat_envelope_v

            sa_v = scipy.signal.hilbert(signal_v)
            sa_amplitude_v = abs(signal_v)
            sa_phase_v = np.unwrap(np.angle(sa_v))
            sa_instantaneous_frequency = (1 / 2 / np.pi) * sa_phase_v / (len(temps_sec_v) / self.sample_rate)

            amplitude_modulation = np.median(sa_amplitude_v)
            frequency_modulation = np.median(sa_instantaneous_frequency)

        return frequency_modulation, amplitude_modulation

    def calculate_log_attack(self):
        """
        This calculates the various global attributes.

        In some cases the calculation of the attack did not return an array, so
        the error is trapped for when a single values is returned rather than
        an array.

        Returns
        -------
        attack_start : TYPE
            DESCRIPTION.
        log_attack_time : TYPE
            DESCRIPTION.
        attack_slope : TYPE
            DESCRIPTION.
        attack_end : TYPE
            DESCRIPTION.
        release : TYPE
            DESCRIPTION.
        release_slope : TYPE
            DESCRIPTION.

        """

        #   Define some specific constants for this calculation

        method = 3
        noise_threshold = 0.15
        decrease_threshold = 0.4

        #   Calculate the position for each threshold

        percent_step = 0.1
        percent_value_value = np.arange(percent_step, 1 + percent_step, percent_step)
        percent_value_position = np.zeros(percent_value_value.shape)

        for p in range(len(percent_value_value)):
            percent_value_position[p] = np.where(self.normal_signal_envelope >= percent_value_value[p])[0][0]

        #   Detection of the start (start_attack_position) and stop (end_attack_position) of the attack

        position_value = np.where(self.normal_signal_envelope > noise_threshold)[0]

        #   Determine the start and stop positions based on selected method

        if method == 1:  # Equivalent to a value of 80%
            start_attack_position = position_value[0]
            end_attack_position = position_value[int(np.floor(0.8 / percent_step))]
        elif method == 2:  # Equivalent to a value of 100%
            start_attack_position = position_value[0]
            end_attack_position = position_value[int(np.floor(1.0 / percent_step))]
        elif method == 3:
            #   Define parameters for the calculation of the search for the start and stop of the attack

            # The terminations for the mean calculation

            m1 = int(round(0.3 / percent_step)) - 1
            m2 = int(round(0.6 / percent_step))

            #   define the multiplicative factor for the effort

            multiplier = 3

            #   Terminations for the start attack correction

            s1att = int(round(0.1 / percent_step)) - 1
            s2att = int(round(0.3 / percent_step))

            #   Terminations for the end attack correction

            e1att = int(round(0.5 / percent_step)) - 1
            e2att = int(round(0.9 / percent_step))

            #   Calculate the effort as the effective difference in adjacent position values

            dpercent_position_value = np.diff(percent_value_position)

            #   Determine the average effort

            M = np.mean(dpercent_position_value[m1:m2])

            #   Start the start attack calculation
            #   we START JUST AFTER THE EFFORT TO BE MADE (temporal gap between percent) is too large

            position2_value = np.where(dpercent_position_value[s1att:s2att] > multiplier * M)[0]

            if len(position2_value) > 0:
                index = int(np.floor(position2_value[-1] + s1att))
            else:
                index = int(np.floor(s1att))

            start_attack_position = percent_value_position[index]

            #   refinement: we are looking for the local minimum

            delta = int(np.round(0.25 * (percent_value_position[index + 1] - percent_value_position[index]))) - 1
            n = int(np.floor(percent_value_position[index]))

            if n - delta >= 0:
                min_position = np.argmin(self.normal_signal_envelope[n - delta:n + delta])
                start_attack_position = min_position + n - delta - 1

            #   Start the end attack calculation
            #   we STOP JUST BEFORE the effort to be made (temporal gap between percent) is too large

            position2_value = np.where(dpercent_position_value[e1att:e2att] > multiplier * M)[0]

            if len(position2_value) > 0:
                index = int(np.floor(position2_value[0] + e1att))
            else:
                index = int(np.floor(e1att))

            end_attack_position = percent_value_position[index]

            #   refinement: we are looking for the local minimum

            delta = int(np.round(0.25 * (percent_value_position[index] - percent_value_position[index - 1])))
            n = int(np.floor(percent_value_position[index]))

            if n - delta >= 0:
                min_position = np.argmax(self.normal_signal_envelope[n - delta:n + delta + 1])
                end_attack_position = min_position + n - delta

        #   Calculate the Log-attack time

        if start_attack_position == end_attack_position:
            start_attack_position -= 1

        rise_time_n = end_attack_position - start_attack_position
        log_attack_time = np.log10(rise_time_n / self.sample_rate)

        #   Calculate the temporal growth - New 13 Jan 2003
        #   weighted average (Gaussian centered on percent=50%) slopes between satt_posn and eattpos_n

        start_attack_position = int(np.round(start_attack_position))
        end_attack_position = int(np.round(end_attack_position))

        start_attack_value = self.normal_signal_envelope[start_attack_position]
        end_attack_value = self.normal_signal_envelope[end_attack_position]

        threshold_value = np.arange(start_attack_value, end_attack_value, 0.1)
        threshold_position_seconds = np.zeros(np.size(threshold_value))

        for i in range(len(threshold_value)):
            position = \
                np.where(self.normal_signal_envelope[start_attack_position:end_attack_position] >= threshold_value[i])[
                    0][0]
            threshold_position_seconds[i] = position / self.sample_rate

        slopes = np.divide(np.diff(threshold_value), np.diff(threshold_position_seconds))

        #   Calculate the increase

        thresholds = (threshold_value[:-1] + threshold_value[1:]) / 2
        weights = np.exp(-(thresholds - 0.5) ** 2 / (0.5 ** 2))
        increase = np.sum(np.dot(slopes, weights)) / np.sum(weights)

        #   Calculate the time decay

        envelope_max_index = np.where(self.normal_signal_envelope == np.max(self.normal_signal_envelope))[0]
        envelope_max_index = int(np.round(0.5 * (envelope_max_index + end_attack_position)))

        stop_position = np.where(self.normal_signal_envelope > decrease_threshold)[0][-1]

        if envelope_max_index == stop_position:
            if stop_position < len(self.normal_signal_envelope):
                stop_position += 1
            elif envelope_max_index > 1:
                envelope_max_index -= 1

        #   Calculate the decrease

        X = np.arange(envelope_max_index, stop_position + 1) / self.sample_rate
        X_index = np.arange(envelope_max_index, stop_position + 1)
        Y = np.log(self.normal_signal_envelope[X_index])
        polynomial_fit = np.polyfit(X, Y, 1)
        decrease = polynomial_fit[0]

        #   Create the list of addresses that we are interested in storing for later consumption

        addresses = np.array([start_attack_position, envelope_max_index, 0, 0, stop_position]) / self.sample_rate

        return log_attack_time, increase, decrease, addresses

    #   ----------------------------------------------- Operators ------------------------------------------------------

    def __add__(self, other):
        """
        This function will add the contents of one waveform to the other. This feature checks the sample rate to ensure
        that they both possess the same sample times. Also, if the data starts at different times, this function will
        create a new object that is the addition of the samples, with the new sample times.

        Parameters
        ----------
        :param other: Waveform - the new object to add to this class's data

        Returns
        -------
        :returns: - A new Waveform object that is the sum of the two
        """

        if not isinstance(other, Waveform):
            ValueError("You must provide a new Waveform object to add to this object.")

        if self.sample_rate != other.sample_rate:
            ValueError("At this time, the two waveforms must possess the same sample rate to add them together")

        s0 = int(other.start_time * other.sample_rate)
        s1 = s0 + len(other.samples)

        return Waveform(self.samples[s0:s1] + other.samples, self.sample_rate, self.start_time)

    def resample(self, new_sample_rate: int):
        """
        A function to resample the internal data of the waveform to change the number of samples per second.

        Parameters
        ----------
        :param new_sample_rate: float - the new sample rate for the signal
        """

        y = scipy.signal.resample(self.samples, int(self.duration * new_sample_rate))

        self.samples = y
        self.sample_rate = new_sample_rate

