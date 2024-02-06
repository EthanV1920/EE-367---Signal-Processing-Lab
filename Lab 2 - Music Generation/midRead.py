"""
File: EE367-Lab2.py
Author: Ethan Vosburg
Date: 01-25-24
Description: This file contains the code for lab 2 where we are tasked with 
making a music file based off of a given audio track. 
"""


# Import Statements
# Documentation link: https://mido.readthedocs.io/en/latest/
import mido
from mido import MidiFile, MidiTrack

import sys
import time
import base64
import random as random
import datetime
import time
import math

# from cpe367exp1.cpe367_wav import cpe367_wav


def getMidiFreq(note):
    """This function returns the frequency of a midi note

    Args:
        note (int): midi defined note

    Returns:
        int: integer value of the frequency of the note
    """
    # Using the formula that was provided in the lab manual to convert midi note
    # to frequency
    return int(440 * 2 ** ((note - 49) / 12))

def getMidiLength(track, sampleRate):
    """Passing in a track will output the total number of samples that are
    needed to make the whole song
    #TODO: Add Scaling to make sure proper time is made 
    Args:
        track (midiTrack): A midi track object
        sampleRate (int): Samples per second
    
    Returns:
        int: number of samples to make the song
    """
    # Instantiate local variable
    lengthTotal = 0
    
    # The number of midi ticks in a 1/4 second
    ppqr = 240
    # Iterate though messages in a track
    for messageindex in track:
       if not messageindex.is_meta:
            lengthtotal = lengthtotal + messageindex.time 
        
        

    
    # return the total sample count
    return lengthTotal

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


# Enumerate though the notes in the midi track and load an array with notes and 
# durations
midi = MidiFile('Lab 2 - Music Generation/midi/midiSong.mid')
for i, track in enumerate(midi.tracks):
    print('Track {}: {}'.format(i, track.name))
    # print(getMidiLength(track, 16000))
    for msg in track:
        msg_dict = msg.dict()
        # if msg.is_meta:
        #     try:
        #         print(msg_dict['tempo'])
        #     except:
        #         print("Message not found")
        if not msg.is_meta:
            if msg.type == "note_on":

            # print(msg.note)
            # print(msg.type)
            # print(getMidiFreq(msg.note))
            # print(msg.is_realtime)
            
        
quit()