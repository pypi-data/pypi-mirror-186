import unittest

import scipy.signal.windows

from .waveform import Waveform
import numpy as np
from pathlib import Path


class Test_Waveform(unittest.TestCase):
    @staticmethod
    def get_wfm(f: float = 1000):
        fs = 48000
        w = 2 * np.pi * f
        t = np.arange(0, 10, 1 / fs)

        wfm = Waveform(0.75 * np.sin(w * t), fs, 0.0)

        return wfm

    @staticmethod
    def get_wfm_2(f: float = 1000):
        f = 100
        w = 2 * np.pi * f
        fs = 48000
        t = np.arange(0, 2, 1 / fs)
        signal = np.cos(w * t)

        wfm = Waveform(signal, fs, 0.0)

        return wfm

    @staticmethod
    def std_bin_file_c130_to_wav():
        return str(Path(__file__).parents[1]) + "/_Test Data/waveformdata/files/after landing_MIP Rack.bin"

    @staticmethod
    def low_pass_filtered_data():
        return str(Path(__file__).parents[1]) + "/_Test Data/waveformdata/100 hz filtered signal.csv"

    def test_constructor(self):
        wfm = Test_Waveform.get_wfm()

        self.assertAlmostEqual(0, wfm.samples[0], delta=1e-10)
        self.assertEqual(480000, len(wfm.samples))
        self.assertEqual(10, wfm.duration)
        self.assertEqual(48000, wfm.sample_rate)
        self.assertEqual(0.0, wfm.time0)
        self.assertEqual(len(wfm.samples), len(wfm.times))
        self.assertIsNone(wfm.forward_coefficients)
        self.assertIsNone(wfm.reverse_coefficients)
        self.assertIsNotNone(wfm.signal_envelope)
        self.assertIsNotNone(wfm.normal_signal_envelope)
        self.assertEqual(12, wfm.coefficient_count)
        self.assertEqual(0.0029, wfm.hop_size_seconds)
        self.assertEqual(0.0232, wfm.window_size_seconds)
        self.assertEqual(5, wfm.cutoff_frequency)
        self.assertEqual(0.15, wfm.centroid_threshold)
        self.assertEqual(0.4, wfm.effective_duration_threshold)

    def test_trim(self):
        wfm = Test_Waveform.get_wfm()

        s0 = 0
        s1 = 1000

        wfm1 = wfm.trim(s0, s1)
        self.assertEqual(1000, len(wfm1.samples))

        self.assertEqual(0, wfm1.time0)
        for i in range(len(wfm1.samples)):
            self.assertEqual(wfm.samples[i], wfm1.samples[i], msg="Error @ {}".format(i))

        wfm2 = wfm.trim(1, s1 + 1)
        self.assertEqual(1000, len(wfm1.samples))
        for i in range(len(wfm1.samples)):
            self.assertEqual(wfm.samples[i + 1], wfm1.samples[i])

    def test_apply_window(self):
        from .waveform import windowing_methods
        import scipy.signal.windows

        wfm = self.get_wfm(1000)

        wfm1 = wfm.apply_window(windowing_methods.tukey, 0.05)
        window = scipy.signal.windows.tukey(len(wfm.samples), 0.05)
        self.assertEqual(len(wfm.samples), len(wfm1.samples))
        for i in range(len(wfm.samples)):
            self.assertAlmostEqual(wfm.samples[i] * window[i], wfm1.samples[i], delta=1e-6)

        wfm1 = wfm.apply_window(windowing_methods.tukey, 0.5)
        window = scipy.signal.windows.tukey(len(wfm.samples), 0.5)
        self.assertEqual(len(wfm.samples), len(wfm1.samples))
        for i in range(len(wfm.samples)):
            self.assertAlmostEqual(wfm.samples[i] * window[i], wfm1.samples[i], delta=1e-6)

        wfm1 = wfm.apply_window(windowing_methods.rectangular)
        window = scipy.signal.windows.tukey(len(wfm.samples), 0.0)
        self.assertEqual(len(wfm.samples), len(wfm1.samples))
        for i in range(len(wfm.samples)):
            self.assertAlmostEqual(wfm.samples[i] * window[i], wfm1.samples[i], delta=1e-6)

        wfm1 = wfm.apply_window(windowing_methods.hanning)
        window = scipy.signal.windows.tukey(len(wfm.samples), 1)
        self.assertEqual(len(wfm.samples), len(wfm1.samples))
        for i in range(len(wfm.samples)):
            self.assertAlmostEqual(wfm.samples[i] * window[i], wfm1.samples[i], delta=1e-6)

        wfm1 = wfm.apply_window(windowing_methods.hamming)
        window = scipy.signal.windows.hamming(len(wfm.samples))
        self.assertEqual(len(wfm.samples), len(wfm1.samples))
        for i in range(len(wfm.samples)):
            self.assertAlmostEqual(wfm.samples[i] * window[i], wfm1.samples[i], delta=1e-6)

    def test_apply_iir_filter(self):
        import scipy.signal

        wfm = self.get_wfm(100)

        b, a = scipy.signal.butter(4, 1000 / wfm.sample_rate / 2, btype='low', analog=False, output='ba')

        wfm1 = wfm.apply_lowpass(1000, 4)

        b = np.array([1.55517217808043e-05, 6.22068871232173e-05, 9.33103306848260e-05, 6.22068871232173e-05,
                      1.55517217808043e-05])

        a = np.array([1, -3.65806030240188, 5.03143353336761, -3.08322830175882, 0.710103898341587])

        self.assertEqual(5, len(wfm.forward_coefficients))
        for i in range(5):
            self.assertAlmostEqual(b[i], wfm.forward_coefficients[i], delta=1e-10)

        self.assertEqual(5, len(wfm.reverse_coefficients))
        for i in range(5):
            self.assertAlmostEqual(a[i], wfm.reverse_coefficients[i], delta=1e-10)

        wfm2 = wfm.apply_iir_filter(b, a)

        b = np.array([1.55517217808043e-05, 6.22068871232173e-05, 9.33103306848260e-05, 6.22068871232173e-05,
                      1.55517217808043e-05])

        a = np.array([1, -3.65806030240188, 5.03143353336761, -3.08322830175882, 0.710103898341587])

        self.assertEqual(5, len(wfm.forward_coefficients))
        for i in range(5):
            self.assertAlmostEqual(b[i], wfm.forward_coefficients[i], delta=1e-10)

        self.assertEqual(5, len(wfm.reverse_coefficients))
        for i in range(5):
            self.assertAlmostEqual(a[i], wfm.reverse_coefficients[i], delta=1e-10)

        self.assertEqual(len(wfm1.samples), len(wfm2.samples))

        for i in range(len(wfm1.samples)):
            self.assertAlmostEqual(wfm1.samples[i], wfm2.samples[i], delta=1e-2)

    def test_AC_Filter_design(self):
        # Check AC_design_filter design against outputs from matlab version
        fs = 2e5

        Ba_matlab = [0.032084206336563, -0.064168412667423, -0.0320842063536748, 0.128336825357664, -0.032084206325157,
                     -0.0641684126902407, 0.0320842063422688]
        Aa_matlab = [1, -5.32939721339437, 11.7682035394565, -13.7759185980543, 9.01251831975431, -3.12310892469402,
                     0.447702876935291]
        Bc_matlab = [0.0260099630889772, 4.62329257443558e-12, -0.0520199261825801, -4.62329257443599e-12,
                     0.0260099630936028]
        Ac_matlab = [1, -3.35568854501294, 4.17126593340454, -2.27533221962382, 0.459754874493225]

        # Call ac_filter_design from python at fs
        coeffA, coeffC = Waveform.AC_Filter_Design(fs)

        # Check all coeffecients across a and c filters
        for i in range(len(Aa_matlab)):
            self.assertAlmostEqual(Ba_matlab[i], coeffA[0][i], delta=1e-8)
            self.assertAlmostEqual(Aa_matlab[i], coeffA[1][i], delta=1e-8)

        for i in range(len(Ac_matlab)):
            self.assertAlmostEqual(Bc_matlab[i], coeffC[0][i], delta=1e-8)
            self.assertAlmostEqual(Ac_matlab[i], coeffC[1][i], delta=1e-8)

    def test_apply_a_weight(self):
        self.assertTrue(False, "Not Implemented")

    def test_apply_c_weight(self):
        self.assertTrue(False, "Not Implemented")

    def test_low_pass(self):
        #   Define a signal

        f = 100
        w = 2 * np.pi * f
        fs = 48000
        t = np.arange(0, 2, 1 / fs)
        signal = np.cos(w * t)

        wfm = Waveform(signal, fs, 0.0)

        wfm.apply_lowpass(1000)

        b = np.array([1.55517217808043e-05, 6.22068871232173e-05, 9.33103306848260e-05, 6.22068871232173e-05,
                      1.55517217808043e-05])

        a = np.array([1, -3.65806030240188, 5.03143353336761, -3.08322830175882, 0.710103898341587])

        self.assertEqual(5, len(wfm.forward_coefficients))
        for i in range(5):
            self.assertAlmostEqual(b[i], wfm.forward_coefficients[i], delta=1e-10)

        self.assertEqual(5, len(wfm.reverse_coefficients))
        for i in range(5):
            self.assertAlmostEqual(a[i], wfm.reverse_coefficients[i], delta=1e-10)

    def test_is_calibration(self):
        wfm0 = Test_Waveform.get_wfm()

        self.assertTrue(wfm0.is_calibration()[0])

        wfm0 = Test_Waveform.get_wfm(250)

        self.assertTrue(wfm0.is_calibration()[0])

        wfm0 = Test_Waveform.get_wfm(200)

        self.assertFalse(wfm0.is_calibration()[0])

    def test_get_features(self):
        wfm = Test_Waveform.get_wfm()

        features = wfm.get_features()
        self.assertAlmostEqual(0.030208333333333, features['attack'], delta=1e-4)
        self.assertAlmostEqual(0.137937500000000, features['decrease'], delta=1e-4)
        self.assertAlmostEqual(10, features['release'], delta=1e-4)
        self.assertAlmostEqual(-1.050813362350563, features['log_attack'], delta=1e-4)
        self.assertAlmostEqual(10.284324504585928, features['attack slope'], delta=1e-2)
        self.assertAlmostEqual(-2.233475973967896e-04, features['decrease slope'], delta=1e-6)
        self.assertAlmostEqual(5.032777294219399, features['temporal centroid'], delta=1e-4)
        self.assertAlmostEqual(9.937354166666667, features['effective duration'], delta=1e-4)
        self.assertAlmostEqual(4.092080415748489e-04, features['amplitude modulation'], delta=1e-6)
        self.assertAlmostEqual(0.065570535881231, features['frequency modulation'], delta=1e-4)
        self.assertEqual(12, features['auto-correlation'].shape[1])
        self.assertEqual(3446, features['auto-correlation'].shape[0])
        self.assertAlmostEqual(0.991427742278755, features['auto-correlation'][0, 0], delta=1e-6)
        self.assertAlmostEqual(-2.94422758033417e-05, features['auto-correlation'][-1, -1], delta=3e-5)
        self.assertEqual(3446, len(features['zero crossing rate']))
        self.assertAlmostEqual(2025.13464991023, features['zero crossing rate'][0], delta=1e-6)
        self.assertAlmostEqual(1982.04667863555, features['zero crossing rate'][-1], delta=1e-6)

    def test_rms_envelope(self):
        self.assertTrue(False, "Not Implemented")

    def test_attack(self):
        wfm = Test_Waveform.get_wfm()

        self.assertAlmostEqual(0.030208333333333, wfm.attack, delta=1e-4)

    def test_decrease(self):
        wfm = Test_Waveform.get_wfm()

        self.assertAlmostEqual(0.137937500000000, wfm.decrease, delta=1e-4)

    def test_release(self):
        wfm = Test_Waveform.get_wfm()

        self.assertAlmostEqual(10, wfm.release, delta=1e-4)

    def test_log_attack(self):
        wfm = Test_Waveform.get_wfm()

        self.assertAlmostEqual(-1.050813362350563, wfm.log_attack, delta=1e-4)

    def test_attack_slope(self):
        wfm = Test_Waveform.get_wfm()

        self.assertAlmostEqual(10.284324504585928, wfm.attack_slope, delta=1e-2)

    def test_decrease_slope(self):
        wfm = Test_Waveform.get_wfm()

        self.assertAlmostEqual(-2.233475973967896e-04, wfm.decrease_slope, delta=1e-6)

    def test_temporal_centroid(self):
        wfm = Test_Waveform.get_wfm()

        self.assertAlmostEqual(5.032777294219399, wfm.temporal_centroid, delta=1e-4)

    def test_effective_duration(self):
        wfm = Test_Waveform.get_wfm()

        self.assertAlmostEqual(9.937354166666667, wfm.effective_duration, delta=1e-4)

    def test_amplitude_modulation(self):
        wfm = Test_Waveform.get_wfm()

        self.assertAlmostEqual(4.092080415748489e-04, wfm.amplitude_modulation, delta=1e-6)

    def test_frequency_modulation(self):
        wfm = Test_Waveform.get_wfm()

        self.assertAlmostEqual(0.065570535881231, wfm.frequency_modulation, delta=1e-4)

    def test_auto_correlation(self):
        wfm = Test_Waveform.get_wfm()

        self.assertEqual(12, wfm.auto_correlation.shape[1])
        self.assertEqual(3446, wfm.auto_correlation.shape[0])

        self.assertAlmostEqual(0.991427742278755, wfm.auto_correlation[0, 0], delta=1e-6)
        self.assertAlmostEqual(-2.94422758033417e-05, wfm.auto_correlation[-1, -1], delta=3e-5)

    def test_zero_crossing(self):
        wfm = Test_Waveform.get_wfm()

        self.assertEqual(3446, len(wfm.zero_crossing_rate))

        self.assertAlmostEqual(2025.13464991023, wfm.zero_crossing_rate[0], delta=1e-6)
        self.assertAlmostEqual(1982.04667863555, wfm.zero_crossing_rate[-1], delta=1e-6)

    def test_if_Waveform_trim_returns_correct_duration(self):

        sample_rate = 2000
        x = np.linspace(0, 2 * np.pi, 1000)
        pressure = np.sqrt(2) * np.sin(x)
        f1 = Waveform(pressure, sample_rate, start_time=0)

        start_sample_trimmed = 0
        end_sample_trimmed = start_sample_trimmed + int(0.1 * f1.sample_rate)
        f2 = f1.trim(start_sample_trimmed, end_sample_trimmed)
        self.assertEqual(f2.duration, 0.1)

    def test_Waveform_time_setter(self):

        sample_rate = 2000
        x = np.linspace(0, 2 * np.pi, 1000)
        pressure = np.sqrt(2) * np.sin(x)

        f1 = Waveform(pressure, sample_rate, start_time=0)
        self.assertEqual(0.0, f1.times[0])
        self.assertEqual(0.0, f1.time0)
        self.assertEqual(0.0, f1.start_time)

        f1.start_time = 1
        self.assertEqual(1.0, f1.times[0])
        self.assertEqual(1.0, f1.time0)
        self.assertEqual(1.0, f1.start_time)

    def test_make_canonical_wav(self):
        from .ansi_standard_formatted_files import StandardBinaryFile
        import os.path
        from .wavefile import WaveFile

        sbf = StandardBinaryFile(self.std_bin_file_c130_to_wav())

        if not (os.path.exists("C:/Temp/afrl_acoustics")):
            os.makedirs("C:/Temp/afrl_acoustics")

        sbf.make_wav_file("C:/Temp/afrl_acoustics/canonical_wav.wav")

        self.assertTrue(os.path.exists("C:/Temp/afrl_acoustics/canonical_wav.wav"))

        wfm = WaveFile("C:/Temp/afrl_acoustics/canonical_wav.wav")

        self.assertEqual(sbf.sample_count, len(wfm.samples))
        self.assertEqual(sbf.sample_rate, wfm.sample_rate)

        #   To compare the data we need to rescale the wav file data

        for i in range(len(wfm.samples)):
            self.assertAlmostEqual(sbf.samples[i], wfm.samples[i], delta=1e-2)

    def test_filtering_coefficients(self):
        #   Define a signal

        wfm = self.get_wfm(100)

        wfm.apply_lowpass(1000)

        b = np.array([1.55517217808043e-05, 6.22068871232173e-05, 9.33103306848260e-05, 6.22068871232173e-05,
                      1.55517217808043e-05])

        a = np.array([1, -3.65806030240188, 5.03143353336761, -3.08322830175882, 0.710103898341587])

        self.assertEqual(5, len(wfm.forward_coefficients))
        for i in range(5):
            self.assertAlmostEqual(b[i], wfm.forward_coefficients[i], delta=1e-10)

        self.assertEqual(5, len(wfm.reverse_coefficients))
        for i in range(5):
            self.assertAlmostEqual(a[i], wfm.reverse_coefficients[i], delta=1e-10)

    def test_filtering(self):
        data = np.loadtxt(self.low_pass_filtered_data(), delimiter=',')

        fs = 48000

        wfm = Waveform(data[:, 0], fs, 0.0)

        lp_wfm = wfm.apply_lowpass(1000)

        b = np.array([1.55517217808043e-05, 6.22068871232173e-05, 9.33103306848260e-05, 6.22068871232173e-05,
                      1.55517217808043e-05])

        a = np.array([1, -3.65806030240188, 5.03143353336761, -3.08322830175882, 0.710103898341587])

        self.assertEqual(5, len(wfm.forward_coefficients))
        for i in range(5):
            self.assertAlmostEqual(b[i], wfm.forward_coefficients[i], delta=1e-10)

        self.assertEqual(5, len(wfm.reverse_coefficients))
        for i in range(5):
            self.assertAlmostEqual(a[i], wfm.reverse_coefficients[i], delta=1e-10)

        self.assertEqual(len(lp_wfm.samples), data.shape[0])

        for i in range(100, len(lp_wfm.samples)):
            self.assertAlmostEqual(data[i, 1], lp_wfm.samples[i], delta=1e-3)
