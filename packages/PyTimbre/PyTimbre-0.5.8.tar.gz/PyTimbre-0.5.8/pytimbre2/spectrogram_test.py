import unittest
import numpy as np
import pandas as pd
import pathlib
from .spectrogram import Spectrogram
from .audio_files.waveform import Waveform


class Test_Spectrogram(unittest.TestCase):
    @staticmethod
    def make_spectrogram():
        """
        Generate the test spectrogram data for comparison of data between the Matlab and Python implementation of the
        code

        Returns
        -------
        tuple of time, frequency, distribution
        """

        t = np.arange(0, 10, 0.0058)
        f = np.arange(0, 0.5, 1 / 4096)

        distribution_filename = str(pathlib.Path(__file__).parents[0]) + "/Test Data/distribution.csv"
        distribution = np.loadtxt(distribution_filename, delimiter=',')

        return t, f, distribution

    @staticmethod
    def make_waveform():
        """
        Generate the acoustic waveform that was created in Matlab to make the various spectral features

        Parameters
        ----------
        None

        Returns
        -------
        Waveform of a 1000 Hz signal 10s in duration.
        """
        fs = 48000
        f = 1000
        w = 2 * np.pi * f
        t = np.arange(0, 10, 1/fs)
        signal = 0.75 * np.sin(w * t)

        return Waveform(signal, fs, 0)

    def test_spectral_centroid(self):
        t, f, level = Test_Spectrogram.make_spectrogram()
        s = Spectrogram.from_data(level, f, t)

        dataset = pd.read_csv(str(pathlib.Path(__file__).parents[0]) + "/Test Data/spectral_features.csv",
                              index_col=False)

        self.assertEqual(dataset.shape[0], len(s.spectral_centroid))

        for i in range(dataset.shape[0]):
            self.assertAlmostEqual(dataset.iloc[i, 0], s.spectral_centroid[i], delta=1e-8)

    def test_spectral_spread(self):
        t, f, level = Test_Spectrogram.make_spectrogram()
        s = Spectrogram.from_data(level, f, t)

        dataset = pd.read_csv(str(pathlib.Path(__file__).parents[0]) + "/Test Data/spectral_features.csv",
                              index_col=False)

        self.assertEqual(dataset.shape[0], len(s.spectral_spread))

        for i in range(dataset.shape[0]):
            self.assertAlmostEqual(dataset.iloc[i, 1], s.spectral_spread[i], delta=1e-8)

    def test_spectral_skewness(self):
        t, f, level = Test_Spectrogram.make_spectrogram()
        s = Spectrogram.from_data(level, f, t)

        dataset = pd.read_csv(str(pathlib.Path(__file__).parents[0]) + "/Test Data/spectral_features.csv",
                              index_col=False)
        data = dataset['Skew'].values

        self.assertEqual(dataset.shape[0], len(s.spectral_skewness))

        for i in range(dataset.shape[0]):
            self.assertAlmostEqual(data[i], s.spectral_skewness[i], delta=1e-8)

    def test_spectral_kurtosis(self):
        t, f, level = Test_Spectrogram.make_spectrogram()
        s = Spectrogram.from_data(level, f, t)

        dataset = pd.read_csv(str(pathlib.Path(__file__).parents[0]) + "/Test Data/spectral_features.csv",
                              index_col=False)
        data = dataset['Kurtosis'].values

        self.assertEqual(dataset.shape[0], len(s.spectral_kurtosis))

        for i in range(dataset.shape[0]):
            self.assertAlmostEqual(data[i], s.spectral_kurtosis[i], delta=1e-8)

    def test_spectral_slope(self):
        t, f, level = Test_Spectrogram.make_spectrogram()
        s = Spectrogram.from_data(level, f, t)

        dataset = pd.read_csv(str(pathlib.Path(__file__).parents[0]) + "/Test Data/spectral_features.csv",
                              index_col=False)
        data = dataset['Slope'].values

        self.assertEqual(dataset.shape[0], len(s.spectral_slope))

        for i in range(dataset.shape[0]):
            self.assertAlmostEqual(data[i], s.spectral_slope[i], delta=1e-8)

    def test_spectral_decrease(self):
        t, f, level = Test_Spectrogram.make_spectrogram()
        s = Spectrogram.from_data(level, f, t)

        dataset = pd.read_csv(str(pathlib.Path(__file__).parents[0]) + "/Test Data/spectral_features.csv",
                              index_col=False)
        data = dataset['Decrease'].values

        self.assertEqual(dataset.shape[0], len(s.spectral_decrease))

        for i in range(dataset.shape[0]):
            self.assertAlmostEqual(data[i], s.spectral_decrease[i], delta=1e-8)

    def test_spectral_roll_off(self):
        t, f, level = Test_Spectrogram.make_spectrogram()
        s = Spectrogram.from_data(level, f, t)

        dataset = pd.read_csv(str(pathlib.Path(__file__).parents[0]) + "/Test Data/spectral_features.csv",
                              index_col=False)
        data = dataset['Rolloff'].values

        self.assertEqual(dataset.shape[0], len(s.spectral_roll_off))

        for i in range(dataset.shape[0]):
            self.assertTrue(s.spectral_roll_off[i] * 48000 >= 1000)

    def test_spectral_energy(self):
        t, f, level = Test_Spectrogram.make_spectrogram()
        s = Spectrogram.from_data(level, f, t)

        dataset = pd.read_csv(str(pathlib.Path(__file__).parents[0]) + "/Test Data/spectral_features.csv",
                              index_col=False)
        data = dataset['Energy'].values

        self.assertEqual(dataset.shape[0], len(s.spectral_energy))

        for i in range(dataset.shape[0]):
            self.assertAlmostEqual(data[i], s.spectral_energy[i], delta=1e-8)

    def test_spectral_flatness(self):
        t, f, level = Test_Spectrogram.make_spectrogram()
        s = Spectrogram.from_data(level, f, t)

        dataset = pd.read_csv(str(pathlib.Path(__file__).parents[0]) + "/Test Data/spectral_features.csv",
                              index_col=False)
        data = dataset['Flatness'].values

        self.assertEqual(dataset.shape[0], len(s.spectral_flatness))

        for i in range(dataset.shape[0]):
            self.assertAlmostEqual(data[i], s.spectral_flatness[i], delta=1e-8)

    def test_spectral_crest(self):
        t, f, level = Test_Spectrogram.make_spectrogram()
        s = Spectrogram.from_data(level, f, t)

        dataset = pd.read_csv(str(pathlib.Path(__file__).parents[0]) + "/Test Data/spectral_features.csv",
                              index_col=False)
        data = dataset['Crest'].values

        self.assertEqual(dataset.shape[0], len(s.spectral_crest))

        for i in range(dataset.shape[0]):
            self.assertAlmostEqual(data[i], s.spectral_crest[i], delta=1e-7)

    def test_calculate_normalized_distribution(self):
        t, f, level = Test_Spectrogram.make_spectrogram()
        s = Spectrogram.from_data(level, f, t)

        s.calculate_normalized_distribution()

        self.assertEqual(s.probability_distribution.shape[0], s.levels.shape[0])
        self.assertEqual(s.probability_distribution.shape[1], s.levels.shape[1])

        data = np.loadtxt(str(pathlib.Path(__file__).parents[0]) + "/Test Data/probability_distribution.csv",
                          delimiter=',')

        self.assertEqual(s.probability_distribution.shape[0], data.shape[0])
        self.assertEqual(s.probability_distribution.shape[1], data.shape[1])

        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                self.assertAlmostEqual(data[i, j], s.probability_distribution[i, j], delta=1e-8)

    def test__calculate_mean_center(self):
        t, f, level = Test_Spectrogram.make_spectrogram()
        s = Spectrogram.from_data(level, f, t)

        s.calculate_normalized_distribution()
        s._calculate_mean_center()

        data = np.loadtxt(str(pathlib.Path(__file__).parents[0]) + "/Test Data/mean_center.csv",
                          delimiter=',')

        self.assertEqual(s.mean_center.shape[0], data.shape[0])
        self.assertEqual(s.mean_center.shape[1], data.shape[1])

        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                self.assertAlmostEqual(data[i, j], s.mean_center[i, j], delta=1e-8)

    def test_calculate_spectrum(self):
        s = Spectrogram(Test_Spectrogram.make_waveform(), )

        self.assertEqual(48000, s.sample_rate)
        self.assertEqual(0, s.time0)

        data = np.loadtxt(str(pathlib.Path(__file__).parents[0]) + "/Test Data/distribution.csv",
                          delimiter=',')

        s.calculate_spectrum()

        for i in range(2):
            self.assertEqual(data.shape[i], s.levels.shape[i])

        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                self.assertAlmostEqual(data[i, j], s.levels[i, j], delta=6e-5)



