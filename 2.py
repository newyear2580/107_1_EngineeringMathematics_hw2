
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

diffeq = Eq( 3*y(x).diff(x,x)+2*y(x).diff(x)+y(x), 0 )
ans = dsolve( diffeq, y(x) )
print('\n')
print(ans)

# c1 = 1,c2 = 0  , x:[0.1] plot y(x)

x = np.linspace(0, np.pi, 100)
y = np.exp(-x/3)*(np.cos(np.sqrt(2)*x/3))

plt.plot(x, y, '-')

plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Plot np.exp(-x/3)*(np.cos(np.sqrt(2)*x/3))')
plt.text(0, 0.01, 'Copyright@Chen Li Wei')

plt.show()
