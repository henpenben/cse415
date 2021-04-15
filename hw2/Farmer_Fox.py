'''Farmer_Fox.py
by Henry Hough
UWNetID: henryhow
Student number: 1866071

Assignment 2, in CSE 415, Spring 2021.

This file contains my problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.
'''

# Put your formulation of the Farmer-Fox-Chicken-and-Grain problem here.
# Be sure your name, uwnetid, and 7-digit student number are given above in
# the format shown.
PROBLEM_NAME = "Farmer-Fox-Chicken-and-Grain"

#<COMMON_CODE>
L = 'left'
R = 'right'
F = 'farmer'
X = 'fox'
C = 'chicken'
G = 'grain'

class State:
    def __init__(self, s=None):
      if s==None:
        s = {L: [F, X, C, G], R: []}
      self.s = s

    # returns whether a given state is equal to current state
    def __eq__(self, other):
      for direction in [L, R]:
        if self.s[direction] != other.s[direction]:
          return False
      return True

    # returns a string representation of current state
    def __str__(self):
      output = ""
      output += "Left side:\n"
      for entity in self.s[L]:
        output += entity + "\n"
      output += "\nRight side:\n"
      for entity in self.s[R]:
        output += entity + "\n"
      return output

    # returns a hash of the current state
    def __hash__(self):
      return (self.__str__()).__hash__()

    # returns a copy of current state
    def copy(self):
      copy = State({})
      copy.s[L].clear()
      for entity in self.s[L]:
        copy.s[L].append(entity)
      for entity in self.s[R]:
        copy.s[R].append(entity)
      return copy