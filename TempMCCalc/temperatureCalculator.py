#!/usr/bin/env python3

import numpy as np

# Laplacian(T) = 0   ---  Laplace equation

WALL_EPSILON = 0.1
DICE_ROLLS_PER_DOT = 1000


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
        self.CurrentPointArray = []           # array of floats [T_i]

    @property
    def poi_is_inside(self):
        return True if 0 < self.xPOI < self.xDim or 0 < self.yPOI < self.yDim else False

    def point_is_next_to_wall(self, x, y):
        """
        Returns
        :param x:   x point coordinate
        :param y:   y point coordinate
        :return:    number of wall point is next to, False if point is not next to any wall
        """
        if x <= WALL_EPSILON:
            return 2
        elif y <= WALL_EPSILON:
            return 0
        elif self.xDim - x <= WALL_EPSILON:
            return 1
        elif self.yDim - y <= WALL_EPSILON:
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
        # read values of POI and assign to the processing variables
        self.xPOI, self.yPOI = curr_x, curr_y = x, y
        if not self.poi_is_inside:
            # stop execution if POI is not inside rectangle
            raise Exception("POI must be inside initial rectangle!")

        while len(self.CurrentPointArray) < DICE_ROLLS_PER_DOT:
            # rolling random search until generated enough results
            try:
                curr_x, curr_y = self.get_circle_and_rnd_point(curr_x, curr_y)
                wall = self.point_is_next_to_wall(curr_x, curr_y)
                # self.CurrentPointArray = wall if (self.CurrentPointArray is None) else np.append(
                #     self.CurrentPointArray, np.array([curr_x, curr_y])
                # )
                if wall:
                    curr_x, curr_y = self.xPOI, self.yPOI
                    self.CurrentPointArray.append(wall)
            except KeyboardInterrupt:
                # Interrupt execution if needed without stopping the kernel
                print("Calculation manually interrupted through KeyboardInterrupt")
                self.CurrentPointArray = []
                self.xPOI, self.yPOI = None, None
                return None
        return None
