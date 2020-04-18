
from mido import MidiFile
import sys

# This code dumps MIDI messages to STDOUT
#
# Usage: 
# % python dumpmidi.py file1.mid file2.mid ... fileN.mid

files = sys.argv[1:]
for f in files:
  midi = MidiFile(f)
  for i, track in enumerate(midi.tracks):
    for msg in track:
      print str(msg)

