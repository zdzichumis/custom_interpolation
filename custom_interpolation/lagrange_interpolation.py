""" Function for interpolation using Lagrange method.

    Parameters
    ----------
    x : ndarray-like of shape n
        x coordinates of points to interpolate

    y : ndarray-like of shape n
        y coordinates of points to interpolate

    Returns
    -------
    
    Polynomial(coef) : Polynomial
        The smallest degree polynomial interpolating all given points.

    Examples
    --------

    x = np.array([-1, 0, 1, 2])
    y = np.array([-2, -1, 0, 7])
    result = lagrange_interpolation(x, y)
    result.show()
    points = x, y
    result.plot([-1, 4], points = points)

    x = np.linspace(-1, 1, 11)
    y = 1/(1+25*x**2)
    result = lagrange_interpolation(x, y)
    result.show()
    points = x, y
    result.plot([-1, 1], points = points)

    n = 11
    x = np.array(np.sort([np.cos((2*i+1)/(2*n)*np.pi) for i in range(n)]))
    y = 1/(1+25*x**2)
    result = lagrange_interpolation(x, y)
    result.show()
    points = x, y
    result.plot([-1, 1], points = points)
    plt.show()
"""
import numpy as np
import matplotlib.pyplot as plt
from .Polynomial import Polynomial

def lagrange_interpolation(x, y):
    n = len(x)
    coef = np.empty(n)
    A = np.array([[x[j]**i for i in range(n)] for j in range(n)])
    print(A.shape)
    coef = np.linalg.solve(A, y)
    return Polynomial(coef)
