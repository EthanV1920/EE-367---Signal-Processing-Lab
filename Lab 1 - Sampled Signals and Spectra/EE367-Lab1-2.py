"""
File: EE367-Lab1-2.py
Author: Ethan Vosburg
Date: 01-25-24
Description: This file contains the code for part 2 of Lab 1 for EE367. This 
file creates a 2 Second long 2000 Hz cosine wave with a delay of 0.25ms.
"""

# Import Statements
import sys
import time
import base64
import random as random
import datetime
import time
import math

from cpe367exp1.cpe367_wav import cpe367_wav


def wavgen(dur, freq, rate, channels, amp, phase, delay, fpath_wave_out):
    """This function generates a WAV file

    Arguments:
        dur :               Duration of the wave in seconds
        freq :              Frequency of the wave in Hz
        rate :              Sample rate of the wave in Hz
        channels :          Number of channels in the wave
        amp :               Amplitude of the wave
        phase :             Phase of the wave
        delay :             Delay of the wave in seconds
        fpath_wave_out :    File path of the wave
        
    Returns:
        True or False
        
    """
    # Create a new wav file object
    wav_out  = cpe367_wav('wavOut', fpath_wave_out)
    
    # Configure the wav file object
    wav_out.set_wav_out_configuration(
        channels, 
        16,
        rate,
    )
    
    # Check if the wav file object was configured correctly
    if wav_out == False:
        print("Error setting wav configuration")
        return False
    
    # Open the wav file
    working_file = wav_out.open_wav_out()
    if working_file == False:
        print("Error opening file for writing")
        return False

    #  Calculate number of samples needed and the angular frequency
    sample_count = int(dur * rate)
    w1 = 2 * math.pi * freq / rate
    
    # Generate the samples and write them to the wav file
    for i in range(sample_count):
        working_sample = amp * math.cos(w1 * (i - delay * rate) + (phase/360 * 2 * math.pi))
        working_sample = int(round(working_sample))
        
        working_file = wav_out.write_wav(working_sample)
        if working_file == False: break
        if working_file == False: break
    
    # Close the wav file
    wav_out.close_wav()
    return True

# Run the main function
def main():
    try:
        fpath_wav_out = 'Lab1-2.wav'
        wavgen(2, 2000, 16000, 1, 24576, 45, 0.00025, fpath_wav_out)
    except:
        print("Error: ", sys.exc_info()[0])
        return False
        
    return True 

# Checking if program is run as main
if __name__ == '__main__':
    if (main() == True):
        print("Waveform Generated Successfully")

    # Exit the program
    quit()
