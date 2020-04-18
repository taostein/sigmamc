
# import sys

note_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
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

