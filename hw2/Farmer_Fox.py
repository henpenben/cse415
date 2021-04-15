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
PROBLEM_NAME = "Farmer-Fox-Chicken-Grain"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['H. Hough']
PROBLEM_CREATION_DATE = "14-APR-2021"
PROBLEM_DESC = "A basic formulation of the Ffcg problem using native Python3.9"

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
      a = self.copy()
      b = other.copy()
      for direction in [L, R]:
        a.s[direction].sort()
        b.s[direction].sort()
        if a.s[direction] != b.s[direction]:
          return False
      return True

    # returns a string representation of current state
    def __str__(self):
      output = "\n"
      output += "Left side:\n"
      for entity in self.s[L]:
        output += entity + "\n"
      output += "\n            Right side:\n"
      for entity in self.s[R]:
        output += "            " + entity + "\n"
      return output

    # returns a hash of the current state
    def __hash__(self):
      return (self.__str__()).__hash__()

    # returns a copy of current state
    def copy(self):
      copy = State({})
      for direction in [L, R]:
        copy.s[direction] = self.s[direction].copy()
      return copy

    # returns whether a move is legal
    def can_move(self, move):
      mvC = move.copy()
      #1 Farmer must be on every boat trip
      if F not in mvC: return False

      # Determine what side the farmer is moving from
      side = ''
      if F in self.s[L]: side = L
      else: side = R

      #2 Only zero or one item(s) per trip
      mvC.remove(F)
      if len(mvC) != 1: return False

      #2 Farmer can only take things from the side he is currently on
      passenger = ''
      afterMove = self.s[side].copy()
      if mvC[0] is not None:
        passenger = mvC[0]
        if passenger not in self.s[side]: return False
        afterMove.remove(passenger) # Remove the passenger for next tests

      #4 Fox cannot be left alone with chicken
      if X in afterMove and C in afterMove: return False
      #5 Chicken cannot be left alone with grain
      if C in afterMove and G in afterMove: return False

      return True

    def move(self, move):
      mvC = move.copy()
      side = ['',''] # side[0] is the side being moved towards
      if F in self.s[L]:
        side = [L,R]
      else:
        side = [R,L]

      mvC.remove(F)

      # move the farmer
      new = self.copy()
      new.s[side[0]].remove(F)
      new.s[side[1]].append(F)

      # move the passenger, if applicable
      if mvC[0] is not None:
        new.s[side[1]].append(mvC[0])
        new.s[side[0]].remove(mvC[0])
      return new

def goal_test(state):
  return len(state.s[L]) == 0

def goal_message(s):
  return "Congratulations! You got everything across the river without things eating eachother!"

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)

combinations = [[F,None], [X,F], [F,C], [F,G]]

OPERATORS = [
  Operator(
  "Cross river with " + str(mv[0]) + " and the " + str(mv[1]),
  lambda s, mv=mv: s.can_move(mv),
  lambda s, mv=mv: s.move(mv))
  for mv in combinations]

CREATE_INITIAL_STATE = lambda: State()

GOAL_TEST = lambda s: goal_test(s)

GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)