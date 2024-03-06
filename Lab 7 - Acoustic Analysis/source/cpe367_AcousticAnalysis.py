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

    M = 1000
    fifox = my_fifo(M)

    bk_list = [1]

    xin = 0
    i = 0
    N = 4000

    dftList_real = [0] * 4000
    dftList_imag = [0] * 4000
    sampleValues = [0] * 4000

    while xin != None:
        xin = wav_in.read_wav()
        if xin == None:
            break

        sampleValues[i] = xin
        i += 1

    # DFT calculation
    for k in range(4000):
        for n in range(4000):
            real = sampleValues[n] * math.cos(-2 * math.pi * k * (n/4000))
            imag = sampleValues[n] * math.sin(-2 * math.pi * k * (n/4000))
            dftList_real[k] += real
            dftList_imag[k] += imag

    # Output DFT to the WAV file
    for k in range(4000):
        yout_left = int(round(dftList_real[k] / N))
        yout_right = int(round(dftList_imag[k] / N))

        # output current sample
        ostat = wav_out.write_wav_stereo(yout_left, yout_right)
        if ostat == False:
            break

    # Visualization using Matplotlib
    xList = np.arange(4000)
    plt.figure()
    plt.plot(xList, np.abs(dftList_real + 1j * dftList_imag))
    plt.title('Magnitude of DFT')
    plt.xlabel('Frequency Bin')
    plt.ylabel('Magnitude')
    plt.show()

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

    fpath_wav_in = 'cos_1khz_pulse_20msec.wav'
    fpath_wav_out = 'dft.wav'

    return process_wav(fpath_wav_in, fpath_wav_out)

if __name__ == '__main__':
    main()
