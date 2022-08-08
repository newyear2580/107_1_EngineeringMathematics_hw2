
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

# Solve the DE: x**2*y" + xy' - y = log(x)

diffeq = Eq( x**2*y(x).diff(x,x) + x*y(x).diff(x) - y(x), log(x) )
ans = dsolve( diffeq, y(x) )
print('\n')
print(ans)
print('\n')
# c1 = c2 = 1  , x:[0.2pi] plot y(x)
x = np.linspace(0, 1, 100)
y = x + x**(-1) - np.log(x)

plt.plot(x, y, '-')

plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Plot x+1/x-np.log(x)')
plt.text(0.6, 20, 'Copyright@Chen Li Wei')

plt.show()
