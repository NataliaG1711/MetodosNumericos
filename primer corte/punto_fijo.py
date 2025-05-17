from math import *
from matplotlib import pyplot as plt
import numpy as np

#DESPEJAR LA X
#X = G(X)
#SALE DE F(X) = 0

def g(x):
    #return exp(-x)
    #return (2*np.sin(np.sqrt(x)))**2
    m = 2
    k = 50
    t = 0.1
    return 0.02 - e**(-x*t)*cos((sqrt((k/m)-x**2))*t) 


def punto_fijo(xold, raiz, g, tol = 0.000001):
    iteraciones = 0
    while raiz == 0:
        xnew = g(xold)
        error = abs((xnew - xold)/xnew)
        iteraciones += 1
        print('{:<3} {:<22} {:<25}'.format(iteraciones,xnew,error))
        if error < tol:
            raiz = xnew
            #print(raiz)
            break
        else:
            xold = xnew
    return raiz       


xold = 0.5
raiz = 0
punto_fijo(xold,raiz,g)

x = np.arange(-1000,1000)
#y = 2*np.sin(np.sqrt(x)) - np.sqrt(x)
y = 0.02 - e**(-x*0.1)*cos((sqrt((50/2)-x**2))*0.1)
plt.grid(True)
plt.plot(x,y)
plt.show()
