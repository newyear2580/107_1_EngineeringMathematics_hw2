
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 00:47:39 2018

@author: abc
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *              # 導入sympy

# Define x, y
x = symbols('x')
y = symbols('y', cls = Function )

# Solve the DE: y" - y = exp(x)

diffeq = Eq( y(x).diff(x,x) + 4*y(x), 3*sin(2*x) )
ans = dsolve( diffeq, y(x) )
print('\n')
print(ans)

# c1 = c2 = 1  , x:[0.2pi] plot y(x)

x = np.linspace(0, 2*np.pi, 100)
y = np.cos(2*x) + np.sin(2*x) - 3*x*np.cos(2*x)/4

plt.plot(x, y, '-')

plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Plot cos(2*x) + sin(2*x) - 3*x*cos(2*x)/4')
plt.text(0, -3, 'Copyright@Chen Li Wei')

plt.show()
#np.cos(2*x) + np.sin(2*x) - 3*x*np.cos(2*x)/4
