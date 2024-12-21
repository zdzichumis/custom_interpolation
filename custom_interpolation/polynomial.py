"""A class for storing, evaluating and plotting polynomials.

    Parameters
    ----------
    coef : ndarray-like of shape n
        The list of coeficients of the polynomial with degree n (a coventing used is the i-th element is of the list is coefficient of the i-th power)

    Attributes
    ----------

    coef_ : ndarray of shape n
        The list of coeficients of the polynomial
    
    degree_ : int
        Degree of the polynomial

    Examples
    --------

    coef = np.array([-1, 0, 0, 1])
    polynomial = Polynomial(coef)
    polynomial.show()
    polynomial.plot(xlim = [-2, 4])
"""
import numpy as np
import matplotlib.pyplot as plt

class Polynomial:
    
    def __init__(self, coef):
        self.coef_ = coef
        self.degree_ = len(coef)
        
    def show(self):
        text = f"P(x)={self.coef_[0]}"
        for i in range(1, self.degree_):
            text = text + f"+{self.coef_[i]}*x^{i}"
        print(text)
        
    def eval(self, x):
        return sum(self.coef_[i]*x**i for i in range(self.degree_))
    
    def plot(self, xlim, n = 1000, points = None, col = "blue"):
        x = np.linspace(xlim[0], xlim[1], n)
        plt.plot(x, self.eval(x), c = col)
        if points:
            plt.scatter(points[0], points[1], c = "red")
        
        plt.xlabel("x")
        plt.ylabel("f(x)")
