# PyTimbre

## PyTimbre is a Python conversion of the Matlab package Timbre Toolbox, found here (https://github.com/VincentPerreault0/timbretoolbox).

This package was created in association with work conducted at the United States Air Force Research Laboratory on human 
perception of sound. Generally, models of perception have focused on sound pressure level spectra, and time histories of 
sound pressure. But auditory detection, identification/classification, and localization may be described better by 
attributes of the sound that are more based on perceptual studies of signals.

The concept of Timbre has been used in music perception research for many years. In 2011, Geoffroy Peeters compiled a 
collection of spectro-temporal attributes (features calculated on a frequency spectrum, that varies with time), and 
temporal attributes (features calculated on the waveform, or waveform's envelop). This paper forms the basis for the 
Matlab toolbox referenced above.

Though the Matlab coding functioned, it was cumbersome as Matlab is not a true object-oriented language. This conversion
has sought to integrate the calculation of the various timbre auditory features with the structure of classes and 
provides a more robust method for extension of these ideas and concepts than was available within the Matlab version.

In addition, a generic time waveform object (Waveform) was provided to represent the time signal. From this class, a 
child class is derived to read wave files. This derived class permits the reading of multiple types of wav files (
canonical, and non-canonical) with bit rates from 8-, 16-, 24-, and 32-bit. Also included are interface methods for
reading and adding meta-data that is similar to the MP3 tagging and assists in organizing the audio files by more than 
name or date.

Over the course of research at the United States Air Force Research Laboratory a number of other features were 
determined to be of interest for the use of the PyTimbre toolbox. In effort to unify these different extraction methods
with the data that PyTimbre represents, the tool kits were added to the requirements list and added as properties of the
various classes. These represent the sound quality metrics extracted from the Mosqito project (https://github.com/Eomys/MoSQITo)
and the speech feature extraction ()

# Usage Example
## 1. Defining a waveform from an array of values

from pytimbre2.audio_files.waveform import Waveform

fs = 48000
w = 2 * np.pi * f
t = np.arange(0, 10, 1/fs)

wfm = Waveform(0.75 * np.sin(w*t), fs, 0.0)

## 2. Define a waveform from a wav file

from pytimbre2.audio_files.wavefile import WaveFile

wfm = wave_file(filename)

## 3. Obtain global temporal attributes

from pytimbre2.audio_files.wavefile import WaveFile

wfm = wave_file(filename)

print(wfm.amplitude_modulation)

## 4. Create single spectrogram and get a feature

from pytimbre2.audio_files.wavefile import WaveFile
from pytimbre2.spectrogram import Spectrogram

wfm = wave_file(filename)
spectrum = PowerSpectralDensity_Spectrum(wfm)

print(spectrum.spectral_roll_off)

# Clearance review and publication permission

This software was developed in conjunction with research into the human perception of sound at the 711th Human 
Performance Wing, Airman Systems Directorate.  

It is approved for Distribution A, 88ABW-2020-2147.

A series of audio files employed in classification research within the wing are provided for testing and examples of how 
.to use the interface.