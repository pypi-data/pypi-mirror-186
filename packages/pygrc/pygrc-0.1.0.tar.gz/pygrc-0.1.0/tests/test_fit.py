import pygrc
import numpy as np
import random
import math

def function(x, *args):
    return args[0]*x + args[1]

# this will the least square against two numpy arrays
def test_fit_lsq():
    x = np.linspace(0,10,10)
    y = np.zeros(10)
    for i in range(len(y)):
        y[i] = 2*x[i] + 2*random.random()
    m=pygrc.Fit(x, y, 1,1).fit_lsq(function,[(-1,10),(-2,10)],.1)
    assert math.fabs(m.values["x0"]-2.0) <  0.1, \
        "Least Square x0 parameter does not converge to true value"
    assert math.fabs(m.values["x1"]-1.0) <  1., \
        "Least Square x1 parameter does not converge to true value"
