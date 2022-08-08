
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

diffeq = Eq( y(x).diff(x,x) - y(x), exp(x) )
ans = dsolve( diffeq, y(x) )
print('\n')
print(ans)

# c1 = c2 = 1  , x:[0.1] plot y(x)

x = np.linspace(0, 1, 100)
y = np.exp(x) + np.exp(-x) + x*np.exp(x)/2

plt.plot(x, y, '-')

plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Plot exp(x) + exp(-x) + x*exp(x)/2')
plt.text(0.6, 2, 'Copyright@Chen Li Wei')

plt.show()
