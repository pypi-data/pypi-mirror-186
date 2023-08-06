import os.path
from unittest import TestCase
from .wavefile import WaveFile
from pathlib import Path
from datetime import datetime
from tqdm import tqdm
import numpy as np


class Test_WaveFile(TestCase):
    @staticmethod
    def test_40_byte_fmt_fact_chunks():
        return str(Path(__file__).parents[1]) + "/Test Data/waveformdata/files/canonical wave " \
                                                "file/40byte fmt and fact waveform.wav"

    @staticmethod
    def test_SITH_Calibration():
        return str(Path(__file__).parents[1]) + "/Test Data/waveformdata/files/canonical wave " \
                                                "file/sithxx_calibration.wav"

    @staticmethod
    def test_canonical_wave_sin_440Hz_int():
        return str(Path(__file__).parents[1]) + "/Test Data/waveformdata/files/canonical wave " \
                                                "file/sine 440 hz int.wav"

    @staticmethod
    def test_canonical_wave_sin_440Hz_short():
        return str(Path(__file__).parents[1]) + "/Test Data/waveformdata/files/canonical wave " \
                                                "file/sine 440 hz short.wav"

    @staticmethod
    def test_canonical_wave_sin_440Hz_byte():
        return str(Path(__file__).parents[1]) + "/Test Data/waveformdata/files/canonical wave " \
                                                "file/sine 440 hz char.wav"

    @staticmethod
    def test_canonical_wave_sin_440Hz_float_stereo():
        return str(Path(__file__).parents[1]) + "/Test Data/waveformdata/files/canonical wave " \
                                                "file/stereo sine 440 hz ieee float.wav"

    @staticmethod
    def test_canonical_wave_pink_44100_32_id3():
        return str(Path(__file__).parents[1]) + "/Test Data/waveformdata/files/canonical wave " \
                                                "file/pink_44100Hz_32bit_float_id3.wav"

    @staticmethod
    def test_canonical_wave_sin_440Hz_float():
        return str(Path(__file__).parents[1]) + "/Test Data/waveformdata/files/canonical wave " \
                                                "file/sine 440 hz ieee float.wav"

    @staticmethod
    def test_canonical_wave_pink_44100_32():
        return str(Path(__file__).parents[1]) + "/Test Data/waveformdata/files/canonical wave " \
                                                "file/pink_44100Hz_32bit.wav"

    @staticmethod
    def test_canonical_wave_pink_44100_16():
        return str(Path(__file__).parents[1]) + "/Test Data/waveformdata/files/canonical wave " \
                                                "file/pink_44100Hz_16bit.wav"

    @staticmethod
    def stereo_inflight_file():
        return str(Path(__file__).parents[1]) + "/Test Data/waveformdata/files/canonical wave " \
                                                "file/stereo inflight recording.wav"

    def test_constructor_40byte_fmt_chunk(self):
        wfm = WaveFile(self.test_40_byte_fmt_fact_chunks())

        self.assertEqual(40, wfm.format_chunk.chunk_size)
        self.assertEqual(131070, wfm.fact_chunk.sample_count)

    def test_constructor_24bit(self):
        wfm = WaveFile(self.test_SITH_Calibration())

        self.assertEqual(96000, wfm.sample_rate)
        self.assertEqual(24, wfm.bits_per_sample)
        self.assertEqual(2011, wfm.start_time.year)
        self.assertEqual(1, wfm.start_time.month)
        self.assertEqual(1, wfm.start_time.day)
        self.assertEqual(0, wfm.start_time.hour)
        self.assertEqual(0, wfm.start_time.minute)
        self.assertEqual(39, wfm.start_time.second)
        self.assertEqual(1825826, len(wfm.samples))

    def test_constructor_float_stereo_s0_s1(self):
        cwf_all = WaveFile(self.test_canonical_wave_sin_440Hz_float_stereo())

        cwf_s0 = WaveFile(self.test_canonical_wave_sin_440Hz_float_stereo(), 100)

        for i in range(1000):
            self.assertAlmostEqual(cwf_s0.samples[i, 0], cwf_s0.samples[i, 1], delta=1e-6)
            self.assertAlmostEqual(cwf_all.samples[i + 100, 0], cwf_s0.samples[i, 1], delta=1e-6)

        cwf_s1 = WaveFile(self.test_canonical_wave_sin_440Hz_float_stereo(), s1=10000)

        self.assertEqual(10000, cwf_s1.samples.shape[0])

        for i in range(1000):
            self.assertAlmostEqual(cwf_s1.samples[i, 0], cwf_s1.samples[i, 1], delta=1e-6)
            self.assertAlmostEqual(cwf_all.samples[i, 0], cwf_s1.samples[i, 1], delta=5e-3)

        cwf_s0_s1 = WaveFile(self.test_canonical_wave_sin_440Hz_float_stereo(), s0=100,
                              s1=10000)

        self.assertEqual(10000 - 100, cwf_s0_s1.samples.shape[0])

        for i in range(1000):
            self.assertAlmostEqual(cwf_s0_s1.samples[i, 0], cwf_s0_s1.samples[i, 1], delta=1e-6)
            self.assertAlmostEqual(cwf_all.samples[i + 100, 0], cwf_s0_s1.samples[i, 1], delta=5e-3)

    def test_constructor_float_stereo(self):
        cwf = WaveFile(self.test_canonical_wave_sin_440Hz_float_stereo())

        self.assertEqual(1323000, cwf.samples.shape[0])
        self.assertEqual(2, cwf.samples.shape[1])

        for i in range(1000):
            t = (2 * np.pi * 440 * i) / cwf.sample_rate

            self.assertAlmostEqual(0.8 * np.sin(t), cwf.samples[i, 0], delta=1e-6, msg="Error at index {}".format(i))

            self.assertAlmostEqual(cwf.samples[i, 0], cwf.samples[i, 1], delta=1e-6)

    def test_constructor_float(self):
        path = self.test_canonical_wave_sin_440Hz_float()

        cwf = WaveFile(path)

        self.assertEqual(1323000, cwf.samples.shape[0])

        for i in range(1000):
            t = (2 * np.pi * 440 * i) / cwf.sample_rate

            self.assertAlmostEqual(0.8 * np.sin(t), cwf.samples[i], delta=1e-6, msg="Error at index {}".format(i))

    def test_constructor_int(self):
        path = self.test_canonical_wave_sin_440Hz_int()

        cwf = WaveFile(path)

        self.assertEqual(1323000, cwf.samples.shape[0])

        for i in range(1000):
            t = (2 * np.pi * 440 * i) / cwf.sample_rate

            self.assertAlmostEqual(0.8 * np.sin(t), cwf.samples[i], delta=1e-0, msg="Error at index {}".format(i))

    def test_constructor_short(self):
        path = self.test_canonical_wave_sin_440Hz_short()

        cwf = WaveFile(path)

        self.assertEqual(1323000, cwf.samples.shape[0])

        for i in range(1000):
            t = (2 * np.pi * 440 * i) / cwf.sample_rate

            self.assertAlmostEqual(0.8 * np.sin(t), cwf.samples[i], delta=1e-0, msg="Error at index {}".format(i))

    def test_constructor_char(self):
        path = self.test_canonical_wave_sin_440Hz_byte()

        cwf = WaveFile(path)

        self.assertEqual(1323000, cwf.samples.shape[0])

        for i in range(1000):
            t = (2 * np.pi * 440 * i) / cwf.sample_rate

            self.assertAlmostEqual(0.8 * np.sin(t), cwf.samples[i], delta=1, msg="Error at index {}".format(i))

    def test_constructor(self):
        path = "C:/Temp/Example.wav"

        try:
            cwf = WaveFile(path)
            self.assertTrue(False, "The ValueError was not raised")
        except ValueError:
            self.assertTrue(True)

        try:
            cwf = WaveFile(1000)
            self.assertTrue(False, "The ValueError was not raised")
        except ValueError:
            self.assertTrue(True)

        cwf = WaveFile(self.test_canonical_wave_pink_44100_32())

        self.assertEqual(self.test_canonical_wave_pink_44100_32(), cwf.filename)

        self.assertEqual(44100, cwf.sample_rate)
        self.assertEqual(32, cwf.bits_per_sample)
        self.assertEqual(4, cwf.block_align)
        self.assertEqual(1, cwf.channel_count)
        self.assertEqual(1323000, len(cwf.samples))

        cwf = WaveFile(self.test_canonical_wave_pink_44100_16())

        self.assertEqual(self.test_canonical_wave_pink_44100_16(), cwf.filename)

        self.assertEqual(44100, cwf.sample_rate)
        self.assertEqual(16, cwf.bits_per_sample)
        self.assertEqual(2, cwf.block_align)
        self.assertEqual(1, cwf.channel_count)
        self.assertEqual(1323000, len(cwf.samples))
        self.assertIsNone(cwf.track_number)

        cwf.track_number = 100

        self.assertIsNotNone(cwf.track_number)
        self.assertEqual(100, cwf.track_number)

    def test_save(self):
        cwf = WaveFile(self.test_canonical_wave_pink_44100_32())

        filename = "C:/TEMP/canonical Wave/test output.wav"
        if os.path.exists(filename):
            os.remove(filename)

        if not os.path.exists(os.path.basename(filename)):
            os.makedirs(os.path.basename(filename))

        cwf.save(filename)

        self.assertTrue(os.path.exists(filename))

        cwf2 = WaveFile(filename)

        self.assertEqual(len(cwf.samples), len(cwf2.samples))
        self.assertAlmostEqual(cwf.peak_value, cwf2.peak_value[0], delta=1e-3)

        self.assertIsNotNone(cwf.peak_chunk)
        self.assertIsNotNone(cwf2.peak_chunk)

        with tqdm(total=15000) as t:
            for i in range(15000):
                self.assertAlmostEqual(cwf.samples[i], cwf2.samples[i], delta=5e-2)
                t.update()

        cwf3 = WaveFile(filename, 100)

        self.assertEqual(len(cwf.samples) - 100, len(cwf3.samples))
        self.assertAlmostEqual(cwf.peak_value, cwf3.peak_value[0], delta=5e-2)

        self.assertIsNotNone(cwf.peak_chunk)
        self.assertIsNotNone(cwf3.peak_chunk)

        for i in range(len(cwf3.samples)):
            self.assertAlmostEqual(cwf.samples[i + 100], cwf3.samples[i], delta=5e-2)

    def test_properties(self):
        cwf = WaveFile(self.test_canonical_wave_pink_44100_32())

        self.assertEqual(self.test_canonical_wave_pink_44100_32(), cwf.full_path)

        cwf.archival_location = "WPAFB"
        cwf.artist = "Frank Mobley"
        cwf.commissioned_organization = "AFRL"
        cwf.general_comments = "THIS IS WHERE THE HEADER DATA WILL GO"
        cwf.copyright = "Copyright 2021, 711 HPW"
        cwf.creation_date = datetime(1970, 1, 1, 0, 0, 0)
        cwf.cropping_information = "None"
        cwf.originating_object_dimensions = "None"
        # cwf.dots_per_inch = None
        cwf.engineer_name = "Frank Mobley, Ph.D."
        cwf.subject_genre = "Test case audio files"
        cwf.key_words = "AFRL, Testcase, Audio"
        # cwf.lightness_settings = None
        cwf.originating_object_medium = "Wav file"
        cwf.title = "Testcase for LIST chunk Generation"
        # cwf.color_palette_count = None
        cwf.subject_name = "Testing"
        cwf.description = "This is a file for the testing of the addition of LIST chunk to wav files"
        cwf.creation_software = "Python, AFRL_Physical_Acoustics "
        cwf.data_source = "711 Human Performance Wing/RHWS"
        cwf.original_form = "Canonical Wav File"
        cwf.digitizing_engineer = "Dr. Frank Mobley"
        cwf.track_number = 10

        filename = "C:/TEMP/canonical Wave/test output.wav"
        if os.path.exists(filename):
            os.remove(filename)

        if not os.path.exists(os.path.basename(filename)):
            os.makedirs(os.path.basename(filename))

        cwf.save(filename)

        self.assertTrue(os.path.exists(filename))

        cwf2 = WaveFile(filename)

        self.assertEqual(cwf2.archival_location, "WPAFB")
        self.assertEqual(cwf2.artist, "Frank Mobley")
        self.assertEqual(cwf2.commissioned_organization, "AFRL")
        # self.assertEqual(cwf2.general_comments, "THIS IS WHERE THE HEADER DATA WILL GO")
        self.assertEqual(cwf2.copyright, "Copyright 2021, 711 HPW")
        self.assertEqual(cwf.creation_date, datetime(1970, 1, 1, 0, 0, 0))
        self.assertEqual(cwf2.cropping_information, "None")
        self.assertEqual(cwf2.originating_object_dimensions, "None")
        # cwf.dots_per_inch, None
        self.assertEqual(cwf2.engineer_name, "Frank Mobley, Ph.D.")
        self.assertEqual(cwf2.subject_genre, "Test case audio files")
        self.assertEqual(cwf2.key_words, "AFRL, Testcase, Audio")
        # cwf.lightness_settings, None
        self.assertEqual(cwf2.originating_object_medium, "Wav file")
        self.assertEqual(cwf2.title, "Testcase for LIST chunk Generation")
        # cwf.color_palette_count, None
        self.assertEqual(cwf2.subject_name, "Testing")
        self.assertEqual(cwf2.description, "This is a file for the testing of the addition of LIST chunk to wav files")
        self.assertEqual(cwf2.creation_software, "Python, AFRL_Physical_Acoustics ")
        self.assertEqual(cwf2.data_source, "711 Human Performance Wing/RHWS")
        self.assertEqual(cwf2.original_form, "Canonical Wav File")
        self.assertEqual(cwf2.digitizing_engineer, "Dr. Frank Mobley")
        self.assertEqual(cwf2.track_number, 10)

        self.assertEqual(datetime(1970, 1, 1, 0, 0, 0), cwf2.list_chunk.time0)

    def test_read_list_constructor(self):
        wav = WaveFile(self.test_canonical_wave_pink_44100_32_id3())

        self.assertEqual(self.test_canonical_wave_pink_44100_32_id3(), wav.filename)

        self.assertEqual(44100, wav.sample_rate)
        self.assertEqual(32, wav.bits_per_sample)
        self.assertEqual(4, wav.block_align)
        self.assertEqual(1, wav.channel_count)
        self.assertEqual(1323000, len(wav.samples))

        self.assertEqual("Pink Noise", wav.meta_data['title'])
        self.assertEqual(1, wav.meta_data['track_no'])

    def test_multi_track(self):
        wav = WaveFile(self.stereo_inflight_file())

        self.assertEqual(2, wav.channel_count)
        self.assertEqual(2, wav.samples.shape[1])

    def test_trim_stereo_file(self):
        wav = WaveFile(self.stereo_inflight_file(), s0=100, s1=10000)

        wav.artist = 'Dr. Frank S. Mobley'
        wav.commissioned_organization = 'F-16 SPO/Lockheed Martin'
        wav.track_number = 1
        wav.original_form = "Wave file"
        wav.digitizing_engineer = "Frank Mobley or Ken Johnson"
        wav.description = "This is a test of writting a "
        wav.data_source = "F-16, Block 40"
        wav.archival_location = "WPAFB, Oh"
        wav.creation_date = datetime.now()
        wav.title = "Stereo trimming example"

        filename = "C:\Temp\wav file\example trimmed with LIST.wav"

        if os.path.exists(filename):
            os.remove(filename)

        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        wav.save(filename)

        self.assertTrue(os.path.exists(filename))

        trimmed = WaveFile(filename)

        self.assertEqual(wav.sample_rate, trimmed.sample_rate)
        self.assertEqual(wav.channel_count, trimmed.channel_count)
        self.assertEqual(wav.title, trimmed.title)
        self.assertEqual(wav.track_number, trimmed.track_number)
        self.assertEqual(wav.description, trimmed.description)
        # self.assertEqual(wav.creation_date, trimmed.creation_date)
        self.assertEqual(wav.archival_location, trimmed.archival_location)
        self.assertEqual(wav.artist, trimmed.artist)
        self.assertEqual(wav.samples.shape[0], trimmed.samples.shape[0])

        for i in range(wav.samples.shape[0]):
            for j in range(wav.channel_count):
                self.assertAlmostEqual(wav.samples[i, j], trimmed.samples[i, j], delta=1e-6)
