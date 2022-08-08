
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

diffeq = Eq( y(x).diff(x,x) + y(x), sin(x)/cos(x) )
ans = dsolve( diffeq, y(x) )
print('\n')
print(ans)

# c1 = c2 = 1  , x:[0.4pi] plot y(x)

x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)+np.cos(x)-np.log(np.abs(np.sin(x)/np.cos(x)+1/np.cos(x)))*np.cos(x)

plt.plot(x, y, '-')

plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Plot sin(x)+cos(x)*(1-ln|tan(x)+sec(x)|)')
#plt.text(0, -1.5, 'Copyright@Chen Li Wei')

plt.show()

#np.sin(x) + (1 + np.log(np.sin(x) - 1)/2 - np.log(np.sin(x) + 1)/2)*np.cos(x)
