from math import *
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    #return (x-2)**2
    #return 2*sin(sqrt(x)) - sqrt(x)

    #return exp(-x)-x
    #return 0.01 - np.e**((-x*0.05)/(2*5))*np.cos(np.sqrt(1/(5*10**-4)-(x/(2*5))**2)*0.05)

    #return 0.01 - np.exp(-x*0.05)*np.cos(x*(0.1-0.05))

    return ((x/12)*np.cosh((6/x))+6-(x/12))-15

def biseccion(a,b):

    tol = 10**-6
    error = float('inf')
    iteraciones = 0


    while error > tol:  
        m = (a + b) / 2  
        error = abs((b - a) / 2)
        iteraciones += 1


        print('{:<3} {:<22} {:<25}'.format(iteraciones, m, error))
        
        if f(a) * f(m) < 0: 
            b = m
        else:  
            a = m

    return m

a = -1
b = 5

print("Raíz aproximada:", biseccion(a,b))
'''
x = np.arange(0,100)
#y = 2*np.sin(np.sqrt(x)) - np.sqrt(x)
#y = 0.01 - np.e**((-x*0.05)/(2*5))*np.cos(np.sqrt(1/(5*10**-4)-(x/(2*5))**2)*0.05)
y = 0.01 - np.exp(-x*0.05)*np.cos(x*(0.1-0.05))
plt.grid(True)
plt.plot(x,y)
plt.show()

'''





