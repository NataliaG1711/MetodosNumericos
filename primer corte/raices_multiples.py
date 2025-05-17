from math import *

from matplotlib import pyplot as plt
import numpy as np

def f(x):
    R = 0.082054
    T = 365
    a = 3.592
    p = 1
    b = 0.04267
    #return (x-2)**2
    #return exp(-x)-x
    #return x*3 - 5*x*2 + 7*x -3
    #return (p+a/x*2)(x-b) - R*T
    #return 16 - (1/2)*(x+sqrt(x**2+4*(6.21)))
    return (80*np.exp(-x*10)+(20/x)*(1-np.exp(-x*10))) - 40



def der (x0,f,h = 0.001):
    return (f(x0+h) - f(x0))/h
    
def sec_der(x0,f,h=0.001):
    return (f(x0+2*h) - 2*f(x0+h) + f(x0))/h**2

def new_raph(x0,f,tol=0.000001):
    for i in range (50):
        deriv=der(x0,f)
        sec_deriv = sec_der(x0,f)

        pos = x0 - f(x0)* deriv/(deriv**2 - f(x0)*sec_deriv)
        error = abs((pos - x0)/pos)

        if error <= tol:
            break
        else:
            x0 = pos

        print('{:<3} {:<22} {:<25}'.format(i,pos,error))

x0 = 1

print(new_raph(x0,f))