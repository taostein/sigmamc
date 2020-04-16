
inlets = 1
var tonic = 0  // C
var key = "major"
var debug = false

var note_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
var major_semis = [2, 2, 1, 2, 2, 2, 1]
var minor_semis = [2, 1, 2, 2, 1, 2, 2]

function number_to_note(num) {
    o = Math.floor(num / 12)
    n = note_list[num % 12]
    return [n, o]
}

if (debug) {post("running script\n")}

function note_to_number(note, octave) {
    n = note_list.indexOf(note)
    n += (12 * octave)
    return n
}

function show_state(s) {
  s = s + ": " + note_list[tonic]
  if (debug) {post(s + " " + key + "\n")}
}

function get_notes_for_key(tonic, key) {
  if (key == 'major') {
    scale = major_semis
  } else if (key == 'minor') {
    scale = minor_semis
  } else {
    assert (0, 'bad key')
  }
  start = tonic % 12
  notes = []
  k = 0
  i = start
  while (i <= 127) {
    notes.push(i)
    i = i + scale[k % 7]
    k = k + 1
  }
  return notes
}

var notes_for_key = get_notes_for_key(tonic, key);

function settonic(t) {
  tonic = t
  notes_for_key = get_notes_for_key(t, key)
  show_state("settonic")
}

function setkey(k) {
  key = k
  notes_for_key = get_notes_for_key(tonic, k)
  show_state("setkey")
}

function mididata(data) {
  //post(notes_for_key + "\n")
  show_state("mididata")
  index = notes_for_key.indexOf(data)
  if (index == -1) {
	  [note, octave] = number_to_note(data)
    post("bad note " + note + octave + "\n")
	outlet(0, data)
  } else {
	//[note, octave] = number_to_note(data)
	//post("good note " + note + octave + "\n")
  }
}
