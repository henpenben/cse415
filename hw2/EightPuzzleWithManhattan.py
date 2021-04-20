from EightPuzzle import *
import re
import math

def h(s):
  void_index = s.find_void_location()
  manhattan = 0
  l = re.findall(r"([0-9])+", str(s))
  l = [int(i) for i in l]
  for i in range(1,9):
    if (i, i % 3) == void_index:
        continue
    if l[i] == i:
        continue

    # of rows away                                      number-row
    desired_row = math.floor(i / 3)                   # 0-0 1-0 2-0
    actual_row  = math.floor(l.index(i) / 3)          # 3-1 4-1 5-1
    delta_rows  = abs(actual_row - desired_row)  # 6-2 7-2 8-2

    # of columns away
    desired_col = i % 3
    actual_col  = l.index(i) % 3
    delta_cols  = abs(actual_col - desired_col)

    manhattan = delta_rows + delta_cols

  return manhattan
