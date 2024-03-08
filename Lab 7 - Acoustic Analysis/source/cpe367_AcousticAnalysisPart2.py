#!/usr/bin/python

import sys
import time
import math
import numpy as np
import matplotlib.pyplot as plt

from cpe367_wav import cpe367_wav
from my_fifo import my_fifo

def process_wav(fpath_wav_in, fpath_wav_out):
    wav_in = cpe367_wav('wav_in', fpath_wav_in)
    wav_out = cpe367_wav('wav_out', fpath_wav_out)

    ostat = wav_in.open_wav_in()
    if ostat == False:
        print('Can\'t open wav file for reading')
        return False

    num_channels = 2
    sample_width_8_16_bits = 16
    sample_rate_hz = 16000
    wav_out.set_wav_out_configuration(num_channels, sample_width_8_16_bits, sample_rate_hz)

    ostat = wav_out.open_wav_out()
    if ostat == False:
        print('Can\'t open wav file for writing')
        return False

    samples = []
    frequency = 1000
    sample_rate = 8000
    duration = 1
    decay = 0.1
    
    # Create a 1kHz sine wave
    time_values = np.linspace(0, duration, int(sample_rate * duration))
    samples = 10000 * np.sin(2 * np.pi * frequency * time_values) * np.exp(-time_values / decay)
    
    # Output DFT to the WAV file
    for sample in samples:
        yout_left = int(round(sample))
        yout_right = int(round(sample))

        # output current sample
        ostat = wav_out.write_wav_stereo(yout_left, yout_right)
        if ostat == False:
            break

    wav_in.close_wav()
    wav_out.close_wav()

    return True

def main():
    major_version = int(sys.version[0])
    if major_version < 3:
        print('Sorry! Must be run using python3.')
        print('Current version: ')
        print(sys.version)
        return False

    fpath_wav_in = 'Lab 7 - Acoustic Analysis/source/wav/cos_1khz_pulse_20msec.wav'
    fpath_wav_out = 'Lab 7 - Acoustic Analysis/source/wav/output/Part2Sample.wav'

    return process_wav(fpath_wav_in, fpath_wav_out)

if __name__ == '__main__':
    main()
