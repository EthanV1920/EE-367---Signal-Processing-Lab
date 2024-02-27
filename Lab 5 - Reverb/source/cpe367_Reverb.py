#!/usr/bin/python

import sys
import time

import base64
import random as random

import datetime
import time

from cpe367_wav import cpe367_wav
from my_fifo import my_fifo


	
def process_wav(fpath_wav_in,fpath_wav_out):
	"""
	: this example does not implement an echo!
	: input and output is accomplished via WAV files
	: return: True or False 
	"""
	
	# construct objects for reading/writing WAV files
	#  assign each object a name, to facilitate status and error reporting
	wav_in = cpe367_wav('wav_in',fpath_wav_in)
	wav_out = cpe367_wav('wav_out',fpath_wav_out)
	
	# open wave input file
	ostat = wav_in.open_wav_in()
	if ostat == False:
		print('Cant open wav file for reading')
		return False
		
	# setup configuration for output WAV
	num_channels = 2
	sample_width_8_16_bits = 16
	sample_rate_hz = 16000
	wav_out.set_wav_out_configuration(num_channels,sample_width_8_16_bits,sample_rate_hz)

	# open WAV output file
	ostat = wav_out.open_wav_out()
	if ostat == False:
		print('Cant open wav file for writing')
		return False
	

	# students - well done!
	###############################################################
	###############################################################
	# students - allocate your fifo, with an appropriate length (M)

	# Creating a 0.125 second echo
	M1i = int(0.030 * 16000)
	M1o = int(0.030 * 16000)
	M2i = int(0.035 * 16000)
	M2o = int(0.035 * 16000)
	M3i = int(0.040 * 16000)
	M3o = int(0.040 * 16000)
	M4i = int(0.045 * 16000)
	M4o = int(0.045 * 16000)
	fifo_array_1i = [my_fifo(M1i), my_fifo(M2i), my_fifo(M3i), my_fifo(M4i)]
	fifo_array_1o = [my_fifo(M1o), my_fifo(M2o), my_fifo(M3o), my_fifo(M4o)]

	M5i = int(0.005 * 16000)
	M5o = int(0.005 * 16000)
	M6i = int(0.0017 * 16000)
	M6o = int(0.0017 * 16000)
	fifo_array_2i = [my_fifo(M5i), my_fifo(M6i)]
	fifo_array_2o = [my_fifo(M5o), my_fifo(M6o)]

	stageGain = 0.7
	finalGain = 0.5
	# students - well done!
	###############################################################
	###############################################################

	# process entire input signal
	xin = 0
	while xin != None:
	
		# read next sample (assumes mono WAV file)
		#  returns None when file is exhausted
		xin = wav_in.read_wav()
		if xin == None: break
		

		###############################################################
		###############################################################
		# students - there is work to be done here!
		
		runningSum = 0

		# Filter 1-4 delay and summation
		for filter in range (4):
			fifo_array_1i[filter].update(xin)
			fifo_array_1o[filter].update(stageGain * fifo_array_1i[filter].get_last())
			runningSum = runningSum + fifo_array_1i[filter].get_last() + fifo_array_1o[filter].get_last()

		# Filter 5 and 6
		fifo_array_2i[0].update(runningSum)
		fifo_array_2o[0].update(stageGain * fifo_array_2i[0].get_last())
		w = fifo_array_2i[0].get_last() + stageGain * fifo_array_2o[0].get_last()
		runningSum = -stageGain * fifo_array_2i[0].get_last() + w - stageGain ** 2 * w
		 
		# fifo_array_2i[1].update(runningSum)
		# fifo_array_2o[1].update(stageGain * fifo_array_2i[1].get_last())
		# w = fifo_array_2i[1].get_last() + stageGain * fifo_array_2o[1].get_last()
		# runningSum = -stageGain * fifo_array_2i[1].get_last() + w - stageGain ** 2 * w

			# runningSum = -stageGain * runningSum + fifo.get(fifo.get_size - 1) + stageGain * fifo.get(fifo.get_size - 2) - stageGain ** 2 * fifo.get(fifo.get_size - 1)  - stageGain ** 3 * fifo.get(fifo.get_size - 2)
			

		# Update history with most recent input
		yout_right = finalGain * runningSum + xin
		yout_left = finalGain * runningSum + xin
		

		
		# students - well done!
		###############################################################
		###############################################################


		# convert to signed int
		yout_left = int(yout_left)
		yout_right = int(yout_right)
		
		# output current sample
		ostat = wav_out.write_wav_stereo(yout_left,yout_right)
		if ostat == False: break
	
	# close input and output files
	#  important to close output file - header is updated (with proper file size)
	wav_in.close_wav()
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
	fpath_wav_in = 'Lab 5 - Reverb/source/wav/joy.wav'
	fpath_wav_out = 'Lab 5 - Reverb/source/wav/outputs/roy_reverb.wav'
	
	
	
	############################################
	############################################
	# test signal history
	#  feel free to comment this out, after verifying
		
	# allocate history
	M = 3
	fifo = my_fifo(M)

	# add some values to history
	fifo.update(1)
	fifo.update(2)
	fifo.update(3)
	fifo.update(4)
	
	# print out history in order from most recent to oldest
	print('signal history - test')
	for k in range(M):
		print('hist['+str(k)+']='+str(fifo.get(k)))

	############################################
	############################################
	


	# let's do it!
	return process_wav(fpath_wav_in,fpath_wav_out)
	
			
	
	
	
############################################
############################################
# call main function
if __name__ == '__main__':
	
	main()
	quit()
