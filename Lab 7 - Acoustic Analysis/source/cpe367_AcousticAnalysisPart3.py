#!/usr/bin/python

import sys
import time
import math
import numpy as np
import matplotlib.pyplot as plt

from cpe367_wav import cpe367_wav
from my_fifo import my_fifo
from tqdm import tqdm

def process_wav(fpath_wav_in):
    wav_in = cpe367_wav('wav_in', fpath_wav_in)

    ostat = wav_in.open_wav_in()
    if ostat == False:
        print('Can\'t open wav file for reading')
        return False

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
    
    # Calculate frequency bins for the DFT
    N = len(sampleValues)
    sample_rate = 8000
    frequencies = np.arange(N) * sample_rate / N
    
    # Create a numpy array of the DFT (helps with calculations)
    dfts = np.array(dftList)
    
    # Get the Raw Max frequency
    max_frequency = np.argmax(dfts)
    maxMagnitude = dftList[max_frequency]
    
    # Debugging print statements
    print(f"The max frequency is: {frequencies[max_frequency]} Hz")
    print(f"The max magnitude is: {maxMagnitude}")

    # Print length of frequency array and dfT array
    print(f"Length of frequency array: {len(frequencies[max_frequency//2:N//4])}")
    print(f"Length of DFT array: {len(dftList[max_frequency//2:int(max_frequency * 3)])}")

    minimumIndex = max_frequency // 2
    maximumIndex = int(max_frequency * 3)


    # Compute the magnitudes of the DFT (only need half of them due to symmetry)
    magnitudes = np.abs(dftList[minimumIndex : maximumIndex])

    # Compute the weighted frequencies (only for the first half due to symmetry)
    weighted_frequencies = frequencies[minimumIndex : maximumIndex] * magnitudes

    workingMagnitudes = []
    workingFrequencies = []

    for i in range(len(weighted_frequencies)):
        if (magnitudes[i] >= maxMagnitude/2):
            workingMagnitudes.append(magnitudes[i])
            workingFrequencies.append(weighted_frequencies[i])
            
    # Calculate the sum of weighted frequencies and the sum of magnitudes
    sum_weighted_frequencies = np.sum(workingFrequencies)
    sum_magnitudes = np.sum(workingMagnitudes)

    # Calculate the weighted average
    peak_frequency = sum_weighted_frequencies / sum_magnitudes

    # Print the peak frequency
    print(f"The peak frequency is: {peak_frequency} Hz")

    xList = np.arange(len(sampleValues)//4)

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
    # plt.suptitle(f'Weighted Peak Frequency: {round(peak_frequency, 2)} Hz and Air Gap: {round(air_gap, 2)} in')
    plt.title(f'Magnitude of DFT {fpath_wav_in.split("/")[-1]}')
    plt.text(max_frequency + 10 , maxMagnitude, f'Raw Peak: {round(max_frequency, 2)} Hz', fontsize=12, ha='left')
    # plt.show()
    plt.savefig(f'Lab 7 - Acoustic Analysis/source/wav/output/{fpath_wav_in.split("/")[-1].split(".")[0]}_DFT.png')
    # plt.savefig(f'wav/output/{fpath_wav_in.split("/")[-1].split(".")[0]}_DFT.png')

    wav_in.close_wav()
    # wav_out.close_wav()

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
            #  'Lab 7 - Acoustic Analysis/source/wav/tile2a.wav',
            #  'Lab 7 - Acoustic Analysis/source/wav/tile2b.wav',
            #  'Lab 7 - Acoustic Analysis/source/wav/tile2c.wav',
            #  'Lab 7 - Acoustic Analysis/source/wav/tile2d.wav',
            #  'Lab 7 - Acoustic Analysis/source/wav/tile2e.wav',
             'Lab 7 - Acoustic Analysis/source/wav/output/Part2SampleDelay.wav',
             'Lab 7 - Acoustic Analysis/source/wav/output/Part2Sample.wav'
             ]
             
    clifiles = [
             'wav/tile1a.wav',
             'wav/tile1b.wav',
             'wav/tile1c.wav',
             'wav/tile1d.wav',
             'wav/tile1e.wav',
             'wav/tile2a.wav',
             'wav/tile2b.wav',
             'wav/tile2c.wav',
             'wav/tile2d.wav',
             'wav/tile2e.wav']
             
    # fpath_wav_in = 'Lab 7 - Acoustic Analysis/source/wav/tile1a.wav'
    # fpath_wav_in = 'Lab 7 - Acoustic Analysis/source/wav/cos_1khz_pulse_20msec.wav'
    # fpath_wav_in = 'Lab 7 - Acoustic Analysis/source/wav/output/Part2Sample.wav' 

    for f in files:
        process_wav(f)
    
    return True

if __name__ == '__main__':
    main()
