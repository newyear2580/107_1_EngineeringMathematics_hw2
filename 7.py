
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 00:47:39 2018

@author: abc
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *              # 導入sympy

# Define x, y
t = symbols('t')
x, y = symbols('x y', cls = Function )

# System of DE:
# dx/dt = -y + t
# dy/dt = x - t

# c1 = c2 = 1  , x:[0.2pi] plot y(x)

def f(x) :
    return -np.sin(x)+np.cos(x)+x+1

def g(x) :
    return np.cos(2*x)+np.sin(x)+x-1

x = np.linspace(0, 4*np.pi, 100)
y1 = f(x)
y2 = g(x)
plt.plot(x, y1, '-', x, y2, '--')

plt.xlabel('t')
plt.ylabel('x(t) | y(t)')
plt.title('Plot the functions cos(t)-sin(t)+t+1 and cos(t)+sin(t)+t-1')
plt.text(8, 1, 'Copyright@Chen Li Wei')

plt.show()
