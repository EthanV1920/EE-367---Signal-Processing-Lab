#!/usr/bin/python

import sys
import time

import base64
import random as random

import datetime
import time

from cpe367_wav import cpe367_wav
from my_fifo import my_fifo


def process_wav(fpath_wav_in, fpath_wav_out):
    """
    : this example does not implement an echo!
    : input and output is accomplished via WAV files
    : return: True or False
    """

    # construct objects for reading/writing WAV files
    #  assign each object a name, to facilitate status and error reporting
    wav_in = cpe367_wav("wav_in", fpath_wav_in)
    wav_out = cpe367_wav("wav_out", fpath_wav_out)

    # open wave input file
    ostat = wav_in.open_wav_in()
    if ostat == False:
        print("Cant open wav file for reading")
        return False

    # setup configuration for output WAV
    num_channels = 2
    sample_width_8_16_bits = 16
    sample_rate_hz = 16000
    wav_out.set_wav_out_configuration(
        num_channels, sample_width_8_16_bits, sample_rate_hz
    )

    # open WAV output file
    ostat = wav_out.open_wav_out()
    if ostat == False:
        print("Cant open wav file for writing")
        return False

    # students - well done!
    ###############################################################
    ###############################################################
    # students - allocate your fifo, with an appropriate length (M)

    # Creating a 0.125 second echo

    M1 = int(0.030 * 16000) - 1

    M2 = int(0.035 * 16000) - 1

    M3 = int(0.040 * 16000) - 1

    M4 = int(0.045 * 16000) - 1

    fifo_array_1o = [my_fifo(M1 + 1), my_fifo(M2 + 1), my_fifo(M3 + 1), my_fifo(M4 + 1)]
    input = my_fifo(M4 + 1)

    M5 = int(0.005 * 16000) - 1

    M6 = int(0.0017 * 16000) - 1

    f5i = my_fifo(M5 + 1)
    f6i = my_fifo(M6 + 1)
    final = my_fifo(M6 + 1)

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
        if xin == None:
            break

        ###############################################################
        ###############################################################
        # students - there is work to be done here!

        runningSum = 0

        input.update(xin)
        w1 = input.get(M1) + (stageGain * fifo_array_1o[0].get(M1))
        w2 = input.get(M2) + (stageGain * fifo_array_1o[1].get(M2))
        w3 = input.get(M3) + (stageGain * fifo_array_1o[2].get(M3))
        w4 = input.get(M4) + (stageGain * fifo_array_1o[3].get(M4))

        fifo_array_1o[0].update(w1)
        fifo_array_1o[1].update(w2)
        fifo_array_1o[2].update(w3)
        fifo_array_1o[3].update(w4)

        k = w1 + w2 + w3 + w4

        f5i.update(k)

        allin = -stageGain * k + 0.49 * f5i.get(M5) + (0.357 * f5i.get(M5))

        f6i.update(allin)

        out = (-0.7 * allin) + (0.49 * f6i.get(M6)) + (0.357 * final.get(M6))
        final.update(out)

        # Update history with most recent input
        yout_right = int(0.5 * (finalGain * out + xin))
        yout_left = int(0.5 * (finalGain * out + xin))

        # students - well done!
        ###############################################################
        ###############################################################

        # convert to signed int
        yout_left = int(yout_left)
        yout_right = int(yout_right)

        # output current sample
        ostat = wav_out.write_wav_stereo(yout_left, yout_right)
        if ostat == False:
            break

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
        print("Sorry! must be run using python3.")
        print("Current version: ")
        print(sys.version)
        return False

    # grab file names
    fpath_wav_in = "Lab 7 - Acoustic Analysis/source/wav/cos_1khz_pulse_20msec.wav"
    fpath_wav_out = "Lab 7 - Reverb/source/wav/outputs/AcousticAnalysis.wav"

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
    print("signal history - test")
    for k in range(M):
        print("hist[" + str(k) + "]=" + str(fifo.get(k)))

    ############################################
    ############################################

    # let's do it!
    # analysis_files = 
    # analysis_status = []
    # for f in analysis_files:
    #     analysis_status.append(process_wav(f, f))
    #     process_wav(fpath_wav_in, fpath_wav_out)
    
    return process_wav(fpath_wav_in, fpath_wav_out)


############################################
############################################
# call main function
if __name__ == "__main__":

    main()
    quit()
