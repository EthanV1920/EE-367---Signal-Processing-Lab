"""
File: EE367-Lab1-3.py
Author: Ethan Vosburg
Date: 01-25-24
Description: This file contains the code for part 1 of Lab 1 for EE367. This 
file creates a 2 second long modulated wave with a 2000 Hz cosine wave and a
500 Hz cosine wave.
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


def wavgenmod(dur,
              freq1, 
              freq2, 
              rate, 
              channels, 
              amp1, 
              amp2,
              phase1, 
              phase2, 
              delay, 
              fpath_wave_out):
    """This function generates a WAV file

    Arguments:
        dur :               Duration of the wave in seconds
        freq1 :             Frequency of the wave in Hz
        freq2 :             Frequency of the wave in Hz
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
    w1 = 2 * math.pi * freq1 / rate
    w2 = 2 * math.pi * freq2 / rate
    
    # Generate the samples and write them to the wav file
    for i in range(sample_count):
        wave1 = amp1 * math.cos(w1 * (i - delay * rate) + (phase1/360 * 2 * math.pi))
        wave2 = amp2 * math.cos(w2 * (i - delay * rate) + (phase2/360 * 2 * math.pi))
        working_sample = wave1 * wave2
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
        fpath_wav_out = 'Lab1-3.wav'
        wavgenmod(2, 2000, 500, 16000, 1, 128, 128, 45, -45, 0.00025, fpath_wav_out)
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
