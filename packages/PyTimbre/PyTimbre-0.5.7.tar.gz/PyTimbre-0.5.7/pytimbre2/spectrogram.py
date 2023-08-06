import operator

import pandas

from .audio_files.waveform import Waveform
import numpy as np


class Spectrogram:
    """
    This class represents the Short Time Fourier Transform method for calculating the spectral variations with time. The
    code calculates the spectrogram using the same methods present in the STFT representation of the original Matlab 
    code.
    """

    def __init__(self, a: Waveform = None, nfft=4096):
        """
        Construct the information within the class from the waveform that is passed into the constructor
        
        :param a: Waveform - the acoustic information that we are interested in using for the timbre analysis.
        :param nfft: int - the resolution of the frequency analysis
        """

        self._waveform = a

        self._levels = None
        self._frequencies = None
        self._times = None
        if a is not None:
            self._sample_rate = self._waveform.sample_rate
        else:
            self._sample_rate = 48000

        self.fft_size = nfft
        self.window_size_seconds = 0.0232
        self._hop_size_seconds = 0.0058
        self._window_size = self.window_size_seconds * self.sample_rate
        self._hop_size = self.hop_size_seconds * self.sample_rate

        self.bin_size = self.sample_rate / self.fft_size
        self.sample_rate_x = self.sample_rate / self.hop_size
        self.sample_rate_y = self.fft_size / self.sample_rate_x
        self.window = np.hamming(self.window_size)
        self.window_overlap = self.window_size - self.hop_size

        #   Define the features

        self.centroid = None
        self.mean_center = None
        self.spread = None
        self.skewness = None
        self.kurtosis = None
        self.slope = None
        self.decrease = None
        self.roll_off = None
        self.energy = None
        self.flatness = None
        self.crest = None
        self.probability_distribution = None
        self.integration_variable = None
        self.geometric_mean = None
        self.arithmetic_mean = None

    # -------------------------------------------- Properties ----------------------------------------------------------

    @property
    def waveform(self):
        return self._waveform

    @property
    def signal(self):
        return self.waveform.samples

    @property
    def sample_rate(self):
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, value):
        self._sample_rate = value

    @property
    def hop_size_seconds(self):
        return self._hop_size_seconds

    @hop_size_seconds.setter
    def hop_size_seconds(self, value: float):
        self._hop_size_seconds = value
        self.hop_size = int(np.floor(self.hop_size_seconds * self.sample_rate))
        self.sample_rate_x = self.sample_rate / self.hop_size
        self.window_overlap = self.window_size - self.hop_size

    @property
    def window_size(self):
        return int(np.floor(self._window_size))

    @window_size.setter
    def window_size(self, value: int):
        self._window_size = value
        self.window_size_seconds = self.window_size / self.sample_rate
        self.window = np.hamming(self.window_size)
        self.window_overlap = self.window_size - self.hop_size

    @property
    def hop_size(self):
        return int(np.floor(self._hop_size))

    @hop_size.setter
    def hop_size(self, value: int):
        self._hop_size = value
        self.hop_size_seconds = self._hop_size / self.sample_rate
        self.sample_rate_x = self.sample_rate / self._hop_size
        self.window_overlap = self.window_size - self._hop_size

    @property
    def frequency_count(self):
        return self.fft_size

    @property
    def spectral_centroid(self):
        """
        Spectral centroid represents the spectral center of gravity.
        """

        if self.centroid is None:
            if self._levels is None and self._frequencies is None:
                self.calculate_spectrum()

            if self.probability_distribution is None or self.integration_variable is None:
                self.calculate_normalized_distribution()

            Y = self.integration_variable.reshape((-1, 1)) * np.ones((1, self.probability_distribution.shape[1]))
            self.centroid = np.sum(Y * self.probability_distribution, axis=0)

        return self.centroid

    @property
    def spectral_spread(self):
        """
        Spectral spread or spectral standard-deviation represents the spread of the spectrum around its mean value.
        """
        if self.mean_center is None:
            self._calculate_mean_center()

        if self.probability_distribution is None or self.integration_variable is None:
            self.calculate_normalized_distribution()

        if self.spread is None:
            self.spread = np.sqrt(np.sum(self.mean_center ** 2 * self.probability_distribution, axis=0))

        return self.spread

    @property
    def spectral_skewness(self):
        """
        Spectral skewness gives a measure of the asymmetry of the spectrum around its mean value. A value of 0 indicates
        a symmetric distribution, a value < 0 more energy at frequencies lower than the mean value, and values > 0 more
        energy at higher frequencies.
        """
        if self.mean_center is None:
            self._calculate_mean_center()

        if self.probability_distribution is None or self.integration_variable is None:
            self.calculate_normalized_distribution()

        if self.skewness is None:
            self.skewness = np.sum(self.mean_center ** 3 * self.probability_distribution, axis=0) / \
                            self.spectral_spread ** 3

        return self.skewness

    @property
    def spectral_kurtosis(self):
        """
        Spectral kurtosis gives a measure of the flatness of the spectrum around its mean value. Values approximately 3
        indicate a normal (Gaussian) distribution, values less than 3 indicate a flatter distributions, and values
        greater than 3 indicate a peakier distribution.
        """
        if self.mean_center is None:
            self._calculate_mean_center()

        if self.probability_distribution is None or self.integration_variable is None:
            self.calculate_normalized_distribution()

        if self.kurtosis is None:
            self.kurtosis = np.sum(self.mean_center ** 4 * self.probability_distribution, axis=0) / \
                            self.spectral_spread ** 4

        return self.kurtosis

    @property
    def spectral_slope(self):
        """
        Spectral slope is computed using a linear regression over the spectral amplitude values. It should be noted that
        the spectral slope is linearly dependent on the spectral centroid.
        """
        if self._levels is None and self._frequencies is None:
            self.calculate_spectrum()

        if self.probability_distribution is None or self.integration_variable is None:
            self.calculate_normalized_distribution()

        if self.slope is None:
            numerator = len(self._frequencies) * (self._frequencies.transpose().dot(self.probability_distribution))
            numerator -= np.sum(self._frequencies) * np.sum(self.probability_distribution, axis=0)
            denominator = len(self._frequencies) * sum(self._frequencies ** 2) - np.sum(self._frequencies) ** 2
            self.slope = numerator / denominator

        return self.slope

    @property
    def spectral_decrease(self):
        """
        Spectral decrease was proposed by Krimphoff (1993) in relation to perceptual studies. It averages the set of
        slopes between frequency f[k] and f[1]. It therefore emphasizes the slopes of the lowest frequencies.
        """
        if self._levels is None and self._frequencies is None:
            self.calculate_spectrum()

        if self.probability_distribution is None or self.integration_variable is None:
            self.calculate_normalized_distribution()

        if self.decrease is None:
            numerator = self._levels[1:, :] - np.ones((self._levels.shape[0] - 1, 1)).dot(
                self._levels[0, :].reshape((-1, 1)).transpose())
            denominator = (1 / np.arange(1, len(self._frequencies))).reshape(-1, 1).transpose()
            self.decrease = (denominator.dot(numerator)).transpose().reshape((-1,))
            self.decrease /= np.sum(self.probability_distribution[1:], axis=0)

        return self.decrease

    @property
    def spectral_roll_off(self):
        """
        Spectral roll-off was proposed by Scheirer and Slaney (1997). It is defined as the frequency below which 95%
        of the signal energy is contained.
        """
        if self._levels is None and self._frequencies is None:
            self.calculate_spectrum()

        if self.roll_off is None:
            threshold = 0.95
            cum_sum = np.cumsum(self._levels, axis=0)
            sum = np.ones((len(self.frequencies),1)).dot(
                (threshold * np.sum(self._levels, axis=0)).reshape((-1, 1)).transpose())

            bin = np.cumsum(1 * (cum_sum > sum), axis=0)
            idx = np.where(bin == 1)[0]

            self.roll_off = self.frequencies[idx]

        return self.roll_off

    @property
    def spectral_energy(self):
        """
        A summation of the energy within the spectrum
        """
        if self._levels is None and self._frequencies is None:
            self.calculate_spectrum()

        if self.energy is None:
            self.energy = np.sum(self._levels, axis=0)

        return self.energy

    @property
    def spectral_flatness(self):
        """
        Spectral flatness is obtained by comparing the geometrical mean and the arithmetical mean of the spectrum. The
        original formulation first splot the spectrum into various frequency bands (Johnston, 1988). However, in the
        context of timbre characterization, we use a single frequency band covering the whole frequency range. For
        tonal signals, the spectral flatness is close to 0( a peaky spectrum), whereas for noisy signals it is close to
        1 (flat spectrum).
        """
        if self._levels is None and self._frequencies is None:
            self.calculate_spectrum()

        if self.flatness is None:
            self.geometric_mean = np.exp((1 / len(self._frequencies)) * np.sum(np.log(self._levels), axis=0))
            self.arithmetic_mean = np.mean(self._levels, axis=0)
            self.flatness = self.geometric_mean / self.arithmetic_mean

        return self.flatness

    @property
    def spectral_crest(self):
        """
        The spectral crest measure is obtained by comparing the maximum value and arithmetical mean of the spectrum.
        """
        if self._levels is None and self._frequencies is None:
            self.calculate_spectrum()

        if self.arithmetic_mean is None:
            self.arithmetic_mean = np.mean(self._levels, axis=0)

        if self.crest is None:
            self.crest = np.max(self._levels, axis=0) / self.arithmetic_mean

        return self.crest

    @property
    def duration(self):
        return self.waveform.duration

    @property
    def time0(self):
        return self.waveform.start_time

    @property
    def times(self):
        return self._times

    @property
    def levels(self):
        return self._levels

    @property
    def frequencies(self):
        return self._frequencies

    @property
    def get_average_features(self):
        import numpy as np
        """
        This will return a dict of the various elements within the spectrum and waveform (if it was used to create the
        spectrogram object) with any time variant elements averaged.
        """

        features = dict()

        if self.waveform is not None:
            features = self.waveform.get_features()
            features['zero_crossing_rate'] = np.mean(features['zero_crossing_rate'])
            features['auto_correlation'] = np.mean(features['auto_correlation'], axis=0)

        features['spectral_centroid'] = np.mean(self.spectral_centroid)
        features['spectral_centroid'] = np.mean(self.spectral_spread)
        features['spectral_centroid'] = np.mean(self.spectral_skewness)
        features['spectral_centroid'] = np.mean(self.spectral_kurtosis)
        features['spectral_centroid'] = np.mean(self.spectral_slope)
        features['spectral_centroid'] = np.mean(self.spectral_decrease)
        features['spectral_centroid'] = np.mean(self.spectral_roll_off)
        features['spectral_centroid'] = np.mean(self.spectral_energy)
        features['spectral_centroid'] = np.mean(self.spectral_flatness)
        features['spectral_centroid'] = np.mean(self.spectral_crest)

        return features

    #   ------------------------------------------------ Methods -------------------------------------------------------

    def calculate_normalized_distribution(self):
        if self.levels is None:
            self.calculate_spectrum()

        self.probability_distribution = self.levels
        self.probability_distribution /= np.ones((self.levels.shape[0], 1)).dot(
            np.sum(self.levels, axis=0).reshape((-1, 1)).transpose())

        self.integration_variable = self.frequencies

    def _calculate_mean_center(self):
        if self._levels is None:
            self.calculate_spectrum()

        if self.probability_distribution is None or self.integration_variable is None:
            self.calculate_normalized_distribution()

        if self.mean_center is None:
            self.mean_center = self.integration_variable.reshape((-1, 1)).dot(np.ones((1, len(self.spectral_centroid))))
            self.mean_center -= np.ones((len(self.integration_variable), 1)).dot(
                self.spectral_centroid.reshape((-1, 1)).transpose())

        return self.mean_center

    def calculate_spectrum(self):
        import scipy.signal
        import scipy.fft

        #   If the window is centered at t, this is the starting index at which to loop up the signal which you want
        #   to multiply by the window.  It is a negative number because (almost) half of the window will be before
        #   time t and half after.  In fact, if the length of the window N is an even number, it is set up so this
        #   number equals -1 * (N / 2 -1).  If the length of the window is od, this number equals -1 * (N - 1) / 2

        left_hand_window_size = int(np.ceil(-(self.window_size - 1) / 2))

        #   This is the last index at which to look up signal values and is equal to (N - 1) / 2 if the length N of
        #   the window is odd and N / 2 if the length of the window is even.  This means that in the even case, the
        #   window has an unequal number of past and future values, i.e., time t is not the center of the window,
        #   but slightly to the left of the center of the window (before it).

        right_hand_window_size = int(np.ceil((self.window_size - 1) / 2))

        #   pre-pad the signal

        signal = np.concatenate((np.zeros((-left_hand_window_size,)), self.signal))

        signal = scipy.signal.hilbert(signal)

        last_index = np.floor((len(self.signal) -
                               (right_hand_window_size + 1)) / self.hop_size) * self.hop_size + 1

        #   Define some support vectors

        index = np.arange(0, last_index, self.hop_size, dtype=int) - left_hand_window_size
        size_x = len(index)
        size_y = self.frequency_count / 2
        self._times = np.arange(0, size_x) / (self.sample_rate / self.hop_size)
        normalized_frequency = np.arange(0, size_y) / size_y / 2

        #   Create the windowed signal

        window = np.hamming(self.window_size + 1)
        distribution_pts = np.zeros((self.frequency_count, size_x), dtype='complex')
        for i in range(size_x):
            rng = np.arange(0, self.window_size + 1, dtype=int) + (index[i] + left_hand_window_size)

            distribution_pts[:int(self.window_size + 1), i] = signal[rng] * window

        #   Calculate the FFT

        distribution_pts = scipy.fft.fft(distribution_pts, n=self.frequency_count, axis=0)

        #   Apply the specific scaling for the analysis

        distribution_pts = abs(distribution_pts)
        distribution_pts /= np.sum(abs(window))

        #   Only keep the first half of the spectrum

        self._levels = distribution_pts[:int(round(self.frequency_count / 2)), :]
        self._frequencies = normalized_frequency

    @staticmethod
    def from_data(levels, frequencies, times):
        """
        This function constructs the Spectrogram object from information obtained from the users and sets up an object
        that can be compared with external data without concern for differences in the methods to calculate the
        spectrogram data.

        :param levels: array-like - the 2-D levels with shape = [len(times), len(frequencies)]
        :param frequencies: array-like - the collection of frequencies that define one dimension of the levels matrix
        :param times: array-like - the collection of times within the spectrogram that define the second dimension
        :returns: Spectrogram object
        """

        s = Spectrogram()
        s._levels = levels
        s._frequencies = frequencies
        s._times = times

        return s
