
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

system = [Eq( x(t).diff(t)-4*y(t), 1 ),Eq( y(t).diff(t)+x(t), 2)]
ans = dsolve( system )
print('\n')
print(ans)

# c1 = c2 = 1  , x:[0.4pi] plot y(x)

def f(x) :
    return 4*np.sin(2*x)+4*np.cos(2*x)+2

def g(x) :
    return 2*np.cos(2*x)-2*np.sin(2*x)-1/4

x = np.linspace(0, 4*np.pi, 100)
y1 = f(x)
y2 = g(x)
plt.plot(x, y1, '-', x, y2, '--')

plt.xlabel('t')
plt.ylabel('x(t) | y(t)')
plt.title('Plot the functions 4sin(2t)+4cos(2t)+2 and 2cos(2t)-2sin(2t)-1/4')
plt.text(8, 7, 'Copyright@Chen Li Wei')

plt.show()
