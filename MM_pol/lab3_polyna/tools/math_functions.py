import numpy as np


def liner_function(x, b1, b0):
    return b0 + (b1 * x)


def parabolic_function(x, b2, b1, b0):
    return b0 + (b1 * x) + (b2 * x * x)


def hyperbolic_function(x, b1, b0):
    return b0 + (b1 * (1 / x))


def logarithmic_function(x, b1, b0, base):
    return b0 + (b1 * (np.log(x) / np.log(base)))
