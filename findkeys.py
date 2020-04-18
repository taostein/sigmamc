
from mido import MidiFile
import sys
import miditools as mt

# This code analyzes a list of MIDI files and tests for possible major and minor keys
#
# Usage: 
# % python findkeys.py file1.mid file2.mid ... fileN.mid

files = sys.argv[1:]

def in_key(midi, key, tonic):
  midi_nums = mt.numbers_for_key(tonic, key)
  for i, track in enumerate(midi.tracks):
    for msg in track:
      if (msg.type == 'note_on'):
        note, octave = mt.number_to_note(msg.note)
        if (not (msg.note in midi_nums)):
          return False
  return True

# check all the MIDI files
for key in ["major", "minor"]:
  for tonic in mt.note_list:
    match = True
    for f in files:
      mid = MidiFile(f)
      if (not in_key(mid, key, tonic)):
        match = False
        break
    if (match):
      print tonic + " " + key
