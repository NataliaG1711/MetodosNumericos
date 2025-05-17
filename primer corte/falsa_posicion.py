from math import *

from matplotlib import pyplot as plt
import numpy as np

#BUSCAR SACAR UNA FUNCIÓN F(X) = 0


def f(x):
    return x**2-12


def reg_falsi(x0,x1,f,tol=0.0001):
    anterior = x0 
    for i in range(100):
        if f(x0)*f(x1) < 0:
            pos = x0 - ((x0-x1)*f(x0))/(f(x0) - f(x1))
        #else
            #break
        error = abs((pos - anterior)/pos)

        if error <= tol:
            break
        if f(x0)*f(pos) < 0:
            x1 = pos
            anterior = x1
        else: 
            x0 = pos
            anterior = x0
        
        print('{:<3} {:<22} {:<25}'.format(i,pos,error))
    
x0 = 2
x1 = 5
print(reg_falsi(x0,x1,f))
