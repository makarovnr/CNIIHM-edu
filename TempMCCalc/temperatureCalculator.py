#!/usr/bin/env python3

import numpy


class TemperatureProblem:
    """
    Given temperatures in four walls of 2-dimensional rectangle calculates temperature in specified point.

    Workflow:

    Class is called with conventional __init__:
    temp_calc = TemperatureProblem(x_length, y_length, bottom_wall_temp, right_wall_temp, left_wall_temp, upper_wall_temp)
    Rectangle walls layout:
       _______
      |   3   |
     2|_______|1
          0
    """
    def __init__(self, xdim, ydim, temp):
        self.xDim, self.yDim, self.borderTemps = xdim, ydim, temp
        self.xPOI, self.yPOI = None, None

    @property
    def poi_is_outside(self):
        return True if 0 < self.xPOI > self.xDim or 0 < self.yPOI > self.yDim else False

    def get_poi_temp(self, x, y):
        self.xPOI, self.yPOI = x, y
        if self.poi_is_outside:
            raise Exception("POI must be inside initial rectangle!")
        pass
