# -*- coding: UTF-8 -*-
import music21
from music21 import *
import argparse

# argument parse
parser = argparse.ArgumentParser()
parser.add_argument('-i','--input',required=True)
parser.add_argument('-o','--output',required=True)
args = parser.parse_args()

midi_file = args.input
output = args.output


score =  converter.parse(midi_file)
f = open(output,'a')

def write_note(midi_pitch,duration):
    string = str(midi_pitch) + ',' + str(duration)
    f.write(string)
    f.write('\n')

for part in score:
    # each stream is a part 
    # valid input midi should contain only one part. 
    # other wise it would not work.
    for note in part:
        if isinstance(note, music21.note.Note) :
            duration = int(note.duration.quarterLength  * 12)
            midi_pitch = int(note.pitch.midi)
            write_note(midi_pitch,duration)
        elif isinstance(note, music21.note.Rest):
            duration = int(note.duration.quarterLength  * 12)
            midi_pitch = 'None'
            write_note(midi_pitch,duration)

__version__='0.1'
