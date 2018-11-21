#!/usr/bin/env python3

import numpy as np

# Laplacian(T) = 0   ---  Laplace equation

wall_epsilon = 0.1
dice_rolls_per_dot = 100


class TemperatureProblem:
    """
    Given temperatures in four walls of 2-dimensional rectangle calculates temperature in specified point.

    Workflow:
    Description of workflow will appear here soon.

    Usage:
    Class is called with conventional __init__:
    temp_calc = TemperatureProblem(x_len, y_len, bottom_w_temp, right_w_temp, left_w_temp, upper_w_temp)
    Rectangle walls layout:
       _______
      |   3   |
     2|_______|1
          0
    Calculate temperature for the point of interest:
    t = temp_calc.get_poi_temp(x_poi, y_poi)
    """
    def __init__(self, xdim, ydim, temp):
        self.xDim, self.yDim, self.borderTemps = xdim, ydim, temp   # floats x, y, [t1, t2, t3, t4]
        self.xPOI, self.yPOI = None, None       # floats x, y
        self.CalculatedPOIArray = None          # array of floats [x, y, T]
        self.CurrentPointArray = None           # array of floats [x, y]

    @property
    def poi_is_outside(self):
        return True if 0 < self.xPOI > self.xDim or 0 < self.yPOI > self.yDim else False

    def point_is_next_to_wall(self, x, y):
        if x <= wall_epsilon:
            return 2
        elif y <= wall_epsilon:
            return 0
        elif self.xDim - x <= wall_epsilon:
            return 1
        elif self.yDim - y <= wall_epsilon:
            return 3
        else:
            return False

    def get_circle_and_rnd_point(self, x_pr, y_pr):
        # select circle radius and calculate random angle
        cir_rad = min(self.xDim - x_pr, self.yDim - y_pr, x_pr, y_pr)
        angle = np.random.rand() * 2 * np.pi
        # calculate new point coordinates
        return np.array([x_pr, y_pr]) + np.array([cir_rad * np.cos(angle), cir_rad * np.sin(angle)])

    def get_poi_temp(self, x, y):
        res_set = set()
        # read values of POI and assign to the processing variables
        self.xPOI, self.yPOI = curr_x, curr_y = x, y
        if self.poi_is_outside:                                         # stop execution if POI is not inside rectangle
            raise Exception("POI must be inside initial rectangle!")

        while len(res_set) < dice_rolls_per_dot:
            try:
                curr_x, curr_y = self.get_circle_and_rnd_point(curr_x, curr_y)
                wall = self.point_is_next_to_wall(curr_x, curr_y)
                self.CurrentPointArray = wall if (self.CurrentPointArray is None) else np.append(
                    self.CurrentPointArray, np.array([curr_x, curr_y])
                )
                if wall:
                    curr_x, curr_y = self.xPOI, self.yPOI
                    self.CurrentPointArray = np.append(self.CurrentPointArray, np.ndarray([-1, wall]))
                    res_set.add(self.CurrentPointArray)
                    self.CurrentPointArray = None
            except KeyboardInterrupt:
                print("Calculation manually interrupted through KeyboardInterrupt")
                self.CurrentPointArray = None
                self.xPOI, self.yPOI = None, None
                return None
        return res_set
