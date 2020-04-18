
phonemes = {
  "AA" : "V",
  "AE" : "V",
  "AH" : "V",
  "AO" : "V",
  "AW" : "V",
  "AY" : "V",
  "B" : "C",
  "CH" : "C",
  "D" : "C",
  "DH" : "C",
  "EH" : "V",
  "ER" : "V",
  "EY" : "V",
  "F" : "C",
  "G" : "C",
  "HH" : "C",
  "IH" : "V",
  "IY" : "V",
  "JH" : "C",
  "K" : "C",
  "L" : "C",
  "M" : "C",
  "N" : "C",
  "NG" : "C",
  "OW" : "V",
  "OY" : "V",
  "P" : "C",
  "R" : "C",
  "S" : "C",
  "SH" : "C",
  "T" : "C",
  "TH" : "C",
  "UH" : "V",
  "UW" : "V",
  "V" : "C",
  "W" : "C",
  "Y" : "C",
  "Z" : "C",
  "ZH" : "C"
}

import nltk
nltk.download('cmudict')
from nltk.corpus import cmudict
cmudict0 = cmudict.dict()
import re

def getdictval (w):
  try:
    return (cmudict0[w])
  except:
    return ([])

# take a list of phonemes
def isvowel (c):
  if (len(c) > 2) and (phonemes[c[0:2]] == "V"): return 1
  else: return 0
#  for k, v in phonemes.items():
#    if c.startswith(k):
#      if v == "V":
#        return 1
#      else:
#        return 0
#  return 0

# t = map(lambda y: map(lambda x: map(isvowel, x), y), z)
# s = map(lambda y: map(sum, y), t)
# sum(map(max, s))
# s = map(lambda y: map(sum, y), 

def numsyls (x):
  return (sum(map(
    lambda y: max(map(
      lambda x: sum(map(isvowel, x)), y)),
        map(getdictval, (re.sub('[^a-z]', ' ', x.lower())).split()))))

# def findall 
# load "poetry.py"

