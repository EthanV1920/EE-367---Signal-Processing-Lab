# Import Statments
# Documentation link: https://mido.readthedocs.io/en/latest/
import mido
from mido import MidiFile, MidiTrack

midi = MidiFile('Lab 2 - Music Generation/midi/test.mid')


def getMidiFreq(note):
    """This function returns the frequency of a midi note

    Args:
        note (int): midi defined note

    Returns:
        int: interger value of the frequency of the note
    """
    return int(440 * 2 ** ((note - 49) / 12))

for i, track in enumerate(midi.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if not msg.is_meta:
            print(msg.note)
            print(getMidiFreq(msg.note))
            
        
quit()