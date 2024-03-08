#!/usr/bin/python

import sys
import time
import math
import numpy as np
import matplotlib.pyplot as plt

from cpe367_wav import cpe367_wav
from my_fifo import my_fifo
from tqdm import tqdm

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
        # print(f"Sample {n}: {xin}")
        if xin == None:
            break

        sampleValues.append(xin) 

    # DFT calculation
    print(f"Working on {fpath_wav_in.split('/')[-1]}")
    for sample in tqdm(range(len(sampleValues)//2), desc="Performing DFT..."):
        dftCalcArray = []
        imag = 0
        real = 0
        for k in range(len(sampleValues) - 1) :
            imag += sampleValues[k] * np.sin(-2 * math.pi * k * n / len(sampleValues))
            real += sampleValues[k] * np.cos(-2 * math.pi * k * n / len(sampleValues))
            # dftCalc = np.sqrt(dftCalc) * sampleValues[k]
            # dftCalcArray.append(dftCalc / (len(sampleValues))//2)
        dftList.append(np.sqrt(imag**2 + real**2) / (len(sampleValues))//2)
        # print(f"Sample {sample}: {dftList[sample]} and {sampleValues[sample]}")
        n+=1
        
    # Output DFT to the WAV file
    for sample in dftList:
        yout_left = int(round(sample))
        yout_right = int(round(sample))

        # output current sample
        ostat = wav_out.write_wav_stereo(yout_left, yout_right)
        if ostat == False:
            break
    
    # Calculate frequency bins for the DFT
    N = len(sampleValues)
    sample_rate = 8000  # or 16000 based on your configuration
    frequencies = np.arange(N) * sample_rate / N
    dfts = np.array(dftList)
    max_frequency = np.argmax(dfts)
    print(f"The max frequency is: {frequencies[max_frequency]} Hz")
    print(f"The max magnitude is: {dftList[max_frequency]}")


    # Compute the magnitudes of the DFT (you only need half of them due to symmetry)
    magnitudes = np.abs(dftList[max_frequency//2:N//4])

    # Compute the weighted frequencies (only for the first half due to symmetry)
    weighted_frequencies = frequencies[max_frequency//2:N//4] * magnitudes

    # Calculate the sum of weighted frequencies and the sum of magnitudes
    sum_weighted_frequencies = np.sum(weighted_frequencies)
    sum_magnitudes = np.sum(magnitudes)

    # Calculate the weighted average, which is the peak frequency
    peak_frequency = sum_weighted_frequencies / sum_magnitudes

    # Print the peak frequency
    print(f"The peak frequency is: {peak_frequency} Hz")

#    # Compute the magnitudes of the DFT
#     magnitudes = np.abs(dftList[:(len(sampleValues)//4)])

    xList = np.arange(len(sampleValues)//4)

#     # Compute the weighted frequencies
#     weighted_frequencies = xList * magnitudes

#     # Calculate the sum of weighted frequencies and the sum of magnitudes
#     sum_weighted_frequencies = np.sum(weighted_frequencies)
#     sum_magnitudes = np.sum(magnitudes)

#     # Calculate the weighted average, which is the peak frequency
#     peak_frequency = sum_weighted_frequencies / sum_magnitudes

#     # Print the peak frequency
#     print(f"The peak frequency is: {peak_frequency} Hz")
    

    # Calculate the air gap
    air_gap = 343 / (2 * peak_frequency)
    # convert from meters to inches
    air_gap = air_gap * 39.3701
    print(f"The air gap is: {air_gap} in")

    # Visualization using Matplotlib
    # print(len(dftList))
    # print(len(sampleValues)//2)
    # xList = np.arange(len(sampleValues)//4)
    plt.figure()
    plt.plot(xList, dftList[:(len(sampleValues)//4)])
    plt.xlabel('Frequency Bin')
    plt.ylabel('Magnitude')
    plt.suptitle(f'Peak Frequency: {round(peak_frequency, 2)} Hz and Air Gap: {round(air_gap, 2)} in')
    plt.title(f'Magnitude of DFT {fpath_wav_in.split("/")[-1]}')
    # plt.show()
    plt.savefig(f'Lab 7 - Acoustic Analysis/source/wav/output/{fpath_wav_in.split("/")[-1].split(".")[0]}_DFT.png')

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

    files = [
            #  'Lab 7 - Acoustic Analysis/source/wav/tile1a.wav',
            #  'Lab 7 - Acoustic Analysis/source/wav/tile1b.wav',
            #  'Lab 7 - Acoustic Analysis/source/wav/tile1c.wav',
            #  'Lab 7 - Acoustic Analysis/source/wav/tile1d.wav',
            #  'Lab 7 - Acoustic Analysis/source/wav/tile1e.wav',
             'Lab 7 - Acoustic Analysis/source/wav/tile2a.wav',
             'Lab 7 - Acoustic Analysis/source/wav/tile2b.wav',
             'Lab 7 - Acoustic Analysis/source/wav/tile2c.wav',
             'Lab 7 - Acoustic Analysis/source/wav/tile2d.wav',
             'Lab 7 - Acoustic Analysis/source/wav/tile2e.wav']
             
    # fpath_wav_in = 'Lab 7 - Acoustic Analysis/source/wav/tile1a.wav'
    # fpath_wav_in = 'Lab 7 - Acoustic Analysis/source/wav/cos_1khz_pulse_20msec.wav'
    # fpath_wav_in = 'Lab 7 - Acoustic Analysis/source/wav/output/Part2Sample.wav' 
    fpath_wav_out = 'Lab 7 - Acoustic Analysis/source/wav/output/dft.wav'
    for f in files:
        process_wav(f, fpath_wav_out)
    
    return True

if __name__ == '__main__':
    main()
