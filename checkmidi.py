
from mido import MidiFile
import sys

# This code checks that a MIDI file is consistent with a key signature
# it outputs every note, and shows if it is OK or not OK.
# Example: 
# % python checkmidi.py tt.mid F# major
# F5 (midi 65) OK
# F#5 (midi 66) OK
# G5 (midi 67) not OK
# A5 (midi 69) not OK
# E5 (midi 64) not OK
# F5 (midi 65) OK
# E5 (midi 64) not OK
# E5 (midi 64) not OK
# F5 (midi 65) OK

mid = MidiFile(sys.argv[1])

note_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
octave_list = list(range(11))

major_semis = [2, 2, 1, 2, 2, 2, 1]
minor_semis = [2, 1, 2, 2, 1, 2, 2]
errors = { 
    'notes': 'out of range',
    'bad key' : 'key of major or minor'
    }

def number_to_note(num):
    o = num // 12 
    n = note_list[num % 12]
    return n, o

def note_to_number(note, octave):
    n = note_list.index(note)
    n += (12 * octave)
    return n

# numbers_for_key('C', 'major')
def numbers_for_key(note, key):
  if (key == 'major'):
    scale = major_semis
  elif (key == 'minor'):
    scale = minor_semis
  else:
    assert 0, errors['bad key']
  start = note_to_number(note, 0)
  notes = []
  k = 0
  i = start
  while i <= 127:
    notes = notes + [i]
    i = i + scale[k % 7]
    k = k + 1
  return notes

tonic = sys.argv[2]
key = sys.argv[3]
midi_nums = numbers_for_key(tonic, key)

for i, track in enumerate(mid.tracks):
    for msg in track:
        if (msg.type == 'note_on'):
          note, octave = number_to_note(msg.note)
          s = str(note) + str(octave) + " (midi " + str(msg.note) + ")"
          if (msg.note in midi_nums):
            print (s + " OK")
          else:
            print (s + " not OK")

