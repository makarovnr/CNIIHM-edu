#!/usr/bin/env python3

import numpy as np


class ShuffleGenerator:
    """
    Shuffles values produced by built-in generators to get higher quality generator.

    Work process:
     - Initializes array of random length filled with random numbers
     - Generating random number in range of array's length
     - Getting value on number generated on previous step, it's our result
     - Removing element responding to generated number from our array
     - Generating random number and appending it to the end of our array

    Usage:

     - Initiating generator instance:
     gen = ShuffleGenerator()

     - Getting value
     var = gen.get_next()

    Attributes:
        ShuffleGenerator._Array - array of random numbers

    """

    def __init__(self):
        self._Array = np.random.rand(np.random.random_integers(1000, 5000))
        # Initializing array of random length with random float digits from [0, 1]

    def get_next(self):
        pop_number = np.random.random_integers(self._Array.__len__())
        # Generating random number and getting value responding this number to array
        res = self._Array[pop_number]

        self._Array = np.delete(self._Array, pop_number)
        # removing selected element from our array
        self._Array = np.append(self._Array, np.random.rand())
        # appending random number to the end of the array
        return res


if __name__ == '__main__':
    shuffle = ShuffleGenerator()
    print(shuffle.__doc__)

    for i in range(100):
        print(shuffle.get_next())
