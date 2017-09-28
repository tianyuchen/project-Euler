# -*- coding: utf-8 -*-
# The mower can be programmed to mow the entire surface.)
# The position of the mower can be represented by coordinates (x,y) and by a
# letter giving the cardinal direction (N,E,W,S).
# The lawn is divided into a grid to simplify the navigation.
# For example, a mower position can be « 0, 0, N », it means that this mower is
# located at the lower-left corner of the lawn, and it is oriented North.
# The mower is controlled by sending it a sequence of letters.
# Possible letters are « R », « L » and « F ». « R » and « L » make the mower
# rotate of 90° respectively to the left or to the right, without moving.
# « F » means that the mower is moving forward on the cell in front of it,
# without changing its orientation.
# If the position after the move is outside the lawn, then the mower do not move,
# it keeps its orientation and process the next command.
# The cell directly at North of the position (x, y) has for coordinates (x, y+1).
# An input file following these rules is given to program the mower:
# ● The first line is the coordinates of the upper-right corner of the lawn,
# coordinates of lower-left corner are supposed to be (0,0)
# ● Next lines of the file drive all mowers. There are two lines for each mower:
# ● First line give the initial position and orientation of the mower. Position
# and orientation are given by 2 numbers and a letter, separated by a space
# ● Second line is a sequence of instruction driving the mower across the lawn.
# Instructions are a sequence of letters without space.
# Each mower moves sequentially, it means that the second mower moves only after
# the first one execute all its instructions.
# When the mower has executed all its instructions, it outputs its position and orientation.

from collections import OrderedDict

orientations = OrderedDict([('N', [0, 1]), ('E', [1, 0]), ('S', [0, -1]), ('W', [-1, 0])])


class mow_surface:

    def __init__(self, sx, sy):
        self.sx = sx
        self.sy = sy

    def outside_mow(self, x, y):
        if x < 0 or x > self.sx or y < 0 or y > self.sy:
            return True
        else:
            return False


class mower:

    def __init__(self, x, y, orientation, surface):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.surface = surface

    def TurnRight(self):
        if self.orientation in orientations:
            self.orientation = orientations.keys()[(orientations.keys().index(self.orientation) + 1) % 4]

    def TurnLeft(self):
        if self.orientation in orientations:
            self.orientation = orientations.keys()[(orientations.keys().index(self.orientation) - 1) % 4]

    def MoveForward(self):
        x = self.x + orientations[self.orientation][0]
        y = self.y + orientations[self.orientation][1]
        if not self.surface.outside_mow(x, y):
            self.x = x
            self.y = y

    def mower_run(self, instructions):
        for instruction in list(instructions):
            if instruction == 'L':
                self.TurnLeft()
            elif instruction == 'R':
                self.TurnRight()
            elif instruction == 'F':
                self.MoveForward()
        print self.x, self.y, self.orientation


with open('file.txt') as f:
    content = f.readlines()
    content = [x.strip() for x in content]  # strip(): returns the string e.g. '55\n' --> '55'

    surface = mow_surface(list(content[0])[0], list(content[0])[1])

    for i in range(1, len(content), 2):
        newmower = mower(int((content[i])[0]), int(list(content[i])[1]), list(content[i])[2], surface)
        newmower.mower_run(list(content[i + 1]))
