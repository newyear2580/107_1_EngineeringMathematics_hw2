
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

system = [Eq( x(t).diff(t)+500*x(t)+500*y(t), 5000 ),
          Eq( y(t).diff(t)+5000*x(t)+5000*y(t), 50000)]
ans = dsolve( system )
print('\n')
print(ans)

def f(x) :
    return 10-10*np.exp(-5500*x)

def g(x) :
    return 10/11-(10/11)*np.exp(-5500*x)

def h(x) :
    return 10-10/11-(100/11)*np.exp(-5500*x)

x = np.linspace(0, 60, 100)
y1 = f(x)
y2 = g(x)
y3 = h(x)
plt.plot(x, y1, '-', x, y2, '--', x, y3, '-.')

plt.xlabel('t')
plt.ylabel('I(t)')
plt.title('Electrical network')
plt.text(40, 2, 'I1 -', color = 'blue' )
plt.text(45, 2, 'I2 --', color = 'orange' )
plt.text(50, 2, 'I3 -.', color = 'green' )
plt.text(40, 0, 'Copyright@Chen Li Wei')

plt.show()
