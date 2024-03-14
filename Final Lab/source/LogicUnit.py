import numpy as np

class LogicUnit:

    def __init__(self, lowerMax, upperMax):
        self.lowerMax = lowerMax
        self.upperMax = upperMax

    def symbol(self):
        lowerArray = [697, 770, 852, 941]
        self.lowerDiffs = np.abs(lowerArray - self.lowerMax)
        upperArray = [1209, 1336, 1477, 1633]
        self.upperDiffs = np.abs(upperArray - self.upperMax)

        two_d_array = [
            [1, 2, 3, 'a'],
            [4, 5, 6, 'b'],
            [7, 8, 9, 'c'],
            ['*', 0, '#', 'd']
        ]
        return two_d_array[np.argmin(self.lowerDiffs)][np.argmin(self.upperDiffs)]