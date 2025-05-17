from math import *

from matplotlib import pyplot as plt
import numpy as np

#BUSCAR SACAR UNA FUNCIÓN F(X) = 0


def f(x):
    #return 16 - (1/2)*(x+sqrt(x**2+4*(6.21)))
    #return sqrt(x)
    #return exp(-x)-x
    #return (x**2)-12
    '''
    k = 0.7
    w = 4
    return 3.6 - 9*np.exp(-k*x)*np.cos(w*x)

    '''
    #return ((x/12)*np.cosh((6/x))+6-(x/12))-15
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
'''

x = np.linspace(1,2)
#y = 2*np.sin(np.sqrt(x)) - np.sqrt(x)
#y = 0.01 - np.e**((-x*0.05)/(2*5))*np.cos(np.sqrt(1/(5*10**-4)-(x/(2*5))**2)*0.05)
#y = 3.6 - 9*np.exp(-0.7*x)*np.cos(4*x)
y = ((x/12)*np.cosh((6/x))+6-(x/12))-15
plt.grid(True)
plt.plot(x,y)
plt.show()'
'''