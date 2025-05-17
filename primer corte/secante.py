from math import *

from matplotlib import pyplot as plt
import numpy as np

def f(x):
    #return exp(-x)-x
    #return 0.01 - np.e**((-x*0.05)/(2*5))*np.cos(np.sqrt(1/(5*10**-4)-(x/(2*5))**2)*0.05)
    m = 2
    k = 50
    t = 0.1
    #return 0.02 - np.e**(-x*t)*np.cos((np.sqrt((k/m)-x**2))*t) 
    return 


def der(x0,x1,f):
    return ((f(x0)-f(x1))/(x0-x1))

def sec(x0,x1,f,tol =0.000001):
    for i in range(50):
        derivate = der(x0,x1,f)
        pos = x0 -f(x0)/(derivate)
        error = abs((pos-x0)/pos)
        if error <= tol:
            break
        x0 = x1
        x1 = pos

        print('{:<3} {:<22} {:<25}' .format(i,pos,error))
        #print(f'{i} Raiz: {pos} - Error: {error}')

x0= 0
x1 = 1
print(sec(x0,x1,f))
'''
x = np.arange(-1000,1000)
y = 0.02 - np.e**(-x*t)*np.cos((np.sqrt((k/m)-x**2))*t) 
plt.grid(True)
plt.plot(x,y)
plt.show()
'''
