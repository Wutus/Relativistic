import numpy as np

class CoordConverter:
    def __init__(self, xlim, ylim, xtarget, ytarget):
        self.xlim = xlim
        self.ylim = ylim
        self.xtarget = xtarget
        self.ytarget = ytarget

    def map(self, x, y):
        return ((x - self.xlim[0])/(self.xlim[1] - self.xlim[0]) * (self.xtarget[1] - self.xtarget[0]) + self.xtarget[0],
            (y - self.ylim[0])/(self.ylim[1] - self.ylim[0]) * (self.ytarget[1] - self.ytarget[0]) + self.ytarget[0])

    def reverse_map(self, x, y):
        return ((x - self.xtarget[0])/(self.xtarget[1] - self.xtarget[0]) * (self.xlim[1] - self.xlim[0]) + self.xlim[0],
            (y - self.ytarget[0])/(self.ytarget[1] - self.ytarget[0]) * (self.ylim[1] - self.ylim[0]) + self.ylim[0])

    def map_values(self, x, y):
        return (x/(self.xlim[1] - self.xlim[0]) * (self.xtarget[1] - self.xtarget[0]),
            y/(self.ylim[1] - self.ylim[0]) * (self.ytarget[1] - self.ytarget[0]))

    def reverse_map_values(self, x, y):
        return (x/(self.xtarget[1] - self.xtarget[0]) * (self.xlim[1] - self.xlim[0]),
            y/(self.ytarget[1] - self.ytarget[0]) * (self.ylim[1] - self.ylim[0]))

    # def zoom(self, xzoom = 0.0, yzoom = 0.0):
    #     self.xlim = (self.xlim[0] - xzoom/2, self.xlim[1] + xzoom/2)
    #     self.xlim = (self.ylim[0] - yzoom/2, self.ylim[1] + yzoom/2)

    def change_target(self, xtarget = None, ytarget = None):
        if xtarget is not None:
            self.xtarget = xtarget
        if ytarget is not None:
            self.ytarget = ytarget