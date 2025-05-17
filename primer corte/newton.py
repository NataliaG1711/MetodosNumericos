from math import *

def f(x):
    #return (x-2)**2
    #return exp(-x)-x
    return 20*(e**(0.15*x)) - 100


def derivada(f, x, h = 0.0001):
    return (f(x + h) - f(x)) / h

def newton():
    raiz = 0
    Xold = 6
    tol = 10**-6
    iteraciones = 0

    while raiz == 0:
        Xnew = Xold - (f(Xold) / derivada(f, Xold))
        error = abs((Xnew - Xold) / Xnew)
        iteraciones += 1
        
        print('{:<3} {:<22} {:<25}'.format(iteraciones, Xnew, error))
        
        if error < tol:
            raiz = Xnew
            break

        Xold = Xnew

    return raiz

print("Raíz aproximada:", newton())
