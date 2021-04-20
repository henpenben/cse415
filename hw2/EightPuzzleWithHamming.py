from EightPuzzle import *
import re

def h(s):
  void_index = s.find_void_location()
  hamming = 0
  l = re.findall(r"([0-9])+", str(s))
  for i in range(3):
    for j in range(3):
      if (i, j) == void_index:
        continue
      if (i * 3 + j) != int(l[i * 3 + j]):
        hamming += 1

  return hamming
