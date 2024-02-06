#!/usr/bin/python

import sys
import time

import base64
import random as random

import datetime
import time
import math

from cpe367_wav import cpe367_wav


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

############################################
############################################
# define function to add one note to list
# students - modify this function as needed!

def add_note(xlist,amp,w0,nstart,nlen,harmonics):
	# initializing the decay to zero per sample added to the music
	decay = 0
	# iterate over the samples and harmonics adding each sample to the list
	for n in range(nstart,nstart+nlen):
		# iterate the decay as the samples progress
		decay += 1
		for harmonic in range(harmonics):
			if harmonic == 1:
				xlist[n] +=  (amp / (harmonic + 1)) * math.sin((harmonic + 1) * w0 * n)
			else:
				xlist[n] += (math.exp(-decay/5912)) * (amp / (harmonic + 1)) * math.sin((harmonic + 1) * w0 * n)
	return
	

############################################
############################################
# define routine for generating signal in WAV format
def gen_wav(fpath_wav_out):
	"""
	: this example generates a WAV file
	: output is accomplished via WAV files
	: return: True or False 
	"""
	
	# construct object for writing WAV file
	#  assign object a name, to facilitate status and error reporting
	wav_out = cpe367_wav('wav_out',fpath_wav_out)
		
	# setup configuration for output WAV
	num_channels = 1
	sample_width_8_16_bits = 16
	sample_rate_hz = 16000
	wav_out.set_wav_out_configuration(num_channels,sample_width_8_16_bits,sample_rate_hz)
		
	# open WAV output file
	ostat = wav_out.open_wav_out()
	if ostat == False:
		print('Cant open wav file for writing')
		return False
	
	
	
	###############################################################
	###############################################################
	# students - modify this section here

	# define the total number of samples in relation to the sample rate and
	# beat count for the song
	total_num_samples = int(9 * 0.285 * 16000)
	print("Total Number of Samples:", total_num_samples)
	
	# allocate list of zeros to store an empty signal
	xlist = [0] * total_num_samples

	# define the notes that need to be played
	noteArray = [
		23, 0, 3,
		35, 3, 6,
		32, 6, 9,
		47, 1, 2,
		49, 2, 3,
		51, 3, 4,
		54, 4, 5,
		52, 5, 6,
		52, 6, 7,
		56, 7, 8,
		54, 8, 9
	]
	
	# iterate over the notes and place them in to the song
	for i in range(int(len(noteArray)/3)):
		# define w1 with the midi note and the sample rate
		w1 = 2 * math.pi * getMidiFreq(noteArray[3 * i])/ 16000
		amp = 10000
		n_start = int(noteArray[3 * i + 1] * 0.285 * 16000)
		n_durr = int(noteArray[3 * i + 2] * 0.285 * 16000) - n_start
		
		# add note to the over all array
		add_note(xlist,amp,w1,n_start,n_durr, 6)
	
	
	
	# students - well done!
	###############################################################
	###############################################################



	# write samples to output file one at a time
	for n in range(total_num_samples):
	
		# convert to signed int
		yout = int(round(xlist[n]))
		
		# output current sample 
		ostat = wav_out.write_wav(yout)
		if ostat == False: break
	
	# close input and output files
	#  important to close output file - header is updated (with proper file size)
	wav_out.close_wav()
		
	return True





############################################
############################################
# define main program
def main():

	# check python version!
	major_version = int(sys.version[0])
	if major_version < 3:
		print('Sorry! must be run using python3.')
		print('Current version: ')
		print(sys.version)
		return False
		
	# grab file names
	# fpath_wav_out = sys.argv[1]
	fpath_wav_out = 'music_synth.wav'

	# let's do it!
	return gen_wav(fpath_wav_out)
	
			
	
	
############################################
############################################
# call main function
if __name__ == '__main__':
	
	main()
	quit()
