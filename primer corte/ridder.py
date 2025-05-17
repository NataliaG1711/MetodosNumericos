from math import *

def f(x):
    return exp(-x)-x

def ridder (x0,x1,f,tol = 0.000001):
    anterior = x0
    if f(x0)*f(x1)<0:
        for i in range (50):
            m = (x0 + x1)/2
            pos = m + (x1-m)* (f(m)/f(x0))/sqrt((f(m)/f(x0))**2 - f(x1)/f(x0))
            error = abs((pos - anterior)/pos)

            if error <= tol:
                break
            if f(x0)*f(pos)<0:
                x1 = pos
                anterior = pos
            else:
                x0 = pos
                anterior = pos
            
            print('{:<3} {:<22} {:<25}'.format(i,pos,error))

x0 = 0
x1 = 20
print(ridder(x0,x1,f))


