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
    n = 0
    dftList = []
    sampleValues = []
    # sampleValues = [0] * 4001

    while xin != None:
        xin = wav_in.read_wav()
        print(f"Sample {n}: {xin}")
        if xin == None:
            break

        sampleValues.append(xin) 

    # DFT calculation
    for sample in range(len(sampleValues)//2):
        dftCalc = 0
        # TODO: Need to fix the DFT calculation
        for k in range(len(sampleValues) - 1) :
            dftCalc = np.sin(-2 * math.pi * k * n / len(sampleValues))
            dftCalc = dftCalc + (np.cos(-2 * math.pi * k * n / len(sampleValues)))
            dftCalc = dftCalc * sampleValues[k]
            dftList.append(dftCalc / (len(sampleValues))//2)
        print(f"Sample {sample}: {dftList[sample]} and {sampleValues[sample]}")
        n+=1
        
    # Output DFT to the WAV file
    for sample in dftList:
        yout_left = int(round(sample))
        yout_right = int(round(sample))

        # output current sample
        ostat = wav_out.write_wav_stereo(yout_left, yout_right)
        if ostat == False:
            break

    # Visualization using Matplotlib
    print(len(dftList))
    print(len(sampleValues)//2)
    xList = np.arange(len(sampleValues)//2)
    plt.figure()
    plt.plot(xList, dftList)
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

    fpath_wav_in = 'Lab 7 - Acoustic Analysis/source/wav/tile1a.wav'
    fpath_wav_out = 'Lab 7 - Acoustic Analysis/source/wav/output/dft.wav'

    return process_wav(fpath_wav_in, fpath_wav_out)

if __name__ == '__main__':
    main()
