"""
File: EE367-Lab1.py
Author: Ethan Vosburg and Issac Lake
Date: 01-25-24
Description: This file contains the code for Lab 1 of EE367.
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


def wavgen(dur, freq, rate, channels, amp, phase, fpath_wave_out):
    # Create a new wav file
    wav_out  = cpe367_wav('wavOut', fpath_wave_out)
    
    # 
    wav_out.set_wav_out_configuration(
        channels, 
        16,
        rate,
    )
    
    # Open the wav file
    working_file = wav_out.open_wav_out()
    if working_file == False:
        print("Error opening file for writing")
        return False

    sample_count = dur * rate
    w1 = 2 * math.pi * freq / rate
    
    for i in range(sample_count):
        working_sample = amp * math.sin(w1 * i + phase)
        working_sample = int(round(working_sample))
        
        working_file = wav_out.write_wav(working_sample)
        if working_file == False: break
    
    # Close the wav file
    wav_out.close_wav()
    return True

# Run the main function
def main():
    fpath_wav_out = 'cos.wav'
    return wavgen(2, 2000, 16000, 1, 24576, 45, fpath_wav_out)

# Checking if program is run as main
if __name__ == '__main__':
	main()
	quit()
