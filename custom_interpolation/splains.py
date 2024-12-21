"""A class for storing, evaluating and plotting splains.

    Parameters
    ----------
    cubics : dictionary with tuples of 2 real numbers as keys and Polynomial objects with degree_=3 as values
        The dictionary with ranges on which a cubic is defined as keys and the cubics as values

    Attributes
    ----------

    cubics_ : dictionary with tuples of 2 real numbers as keys and Polynomial objects with degree_=3 as values
        The dictionary with ranges on which a cubic is defined as keys and the cubics as values
    
    splains_count_ : int
        Number of cubics

    Examples
    --------

    coef = np.array([-1, 0, 0, 1])
    polynomial = Polynomial(coef)
    polynomial.show()
    polynomial.plot(xlim = [-2, 4])
"""
import numpy as np
import matplotlib.pyplot as plt
from .polynomial import Polynomial

class Splains:
    
    def __init__(self, cubics):
        self.cubics_ = cubics
        self.splains_count_ = len(cubics)
        
    def show(self, xlim):
        for x_range, cubic in self.cubics_.items():
            if x_range[0] < xlim[1] and x_range[1] > xlim[0]:
                print(f"On interval [{max(x_range[0], xlim[0])}, {min(x_range[1], xlim[1])}] the formula for the splain is:")
                cubic.show()
        
    def eval(self, x):
        for x_range, cubic in self.cubics_.items():
            if x_range[0] < x and x_range[1] > x:
                return cubic.eval(x)
    
    def plot(self, n = 1000, points = None, col = "blue"):
        for x_range, cubic in self.cubics_.items():
            cubic.plot(x_range, n = int(n/self.splains_count_), col = col)
    
        if points:
            plt.scatter(points[0], points[1], c="red")
    
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.show()
