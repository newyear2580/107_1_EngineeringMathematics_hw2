# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 00:47:39 2018

@author: abc
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *              # 導入sympy

def f(x) :
    return x*np.sin(x)

def g(x) :
    return x**2 - x**4/(3*2)

x = np.linspace(-np.pi, np.pi, 100)
y1 = f(x)
y2 = g(x)
plt.plot(x, y1, '-', x, y2, '--')

plt.xlabel('x')
plt.ylabel('f(x) & g(x)')
plt.title('Plot the functions x*sinx and x^2 - x^4/(3!)')
plt.text(1, -6, 'Copyright@Chen Li Wei')

plt.show()
