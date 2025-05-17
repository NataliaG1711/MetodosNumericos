import numpy as np
'''
def f(x):
    #return 0.6042* x**2 - 0.89*x + 2.41
    return 3**x

def Lag(a,b,n,f,x):
    xi = np.linspace(a,b,n+1)
    sum = 0
    for i in range(n+1):
        prod = 1
        for j in range(n+1):
            if j != i:
                prod *= (x-xi[j])/(xi[i] - xi[j])
        sum += prod*f(xi[i])
    return sum

x = 0.8
InterpLag = Lag(0,1,3,f,x)
error = abs(InterpLag - f(x))/(f(x))
print('\n')

print('{:<20} {:<20} {:<20}'.format('f(x)', 'Lagrange', '%Error'))
print('{:<20} {:<20} {:<20}'.format(f(x), InterpLag, error*100))


'''
def lagrange(xi,yi,x):
    n=len(xi)
    coef = np.zeros(n)
    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= (x - xi[j]) / (xi[i] - xi[j])
        coef[i] = yi[i] * prod
        print(coef[i])
    return np.sum(coef)

xi = [9,12,15]
yi = [18,25,30]

print(lagrange(xi,yi,10.5))