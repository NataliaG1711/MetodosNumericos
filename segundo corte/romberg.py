import numpy as np

def f(x):
    return x**3

def romberg(f,a,b,n_rec):

    I = np.zeros((n_rec,n_rec))
    n_col_act = 0
    
    for k in range(n_rec):
        if k == 0:
            for n in range(n_rec):
                integral = 0
                suma = 0
                if n == 0:
                    x = np.linspace(a,b,n+2)
                    integral = (b-a) * (f(x[0]) + f(x[n+1])+ 2*suma) / (2*(n+1))
                    I[n][k] = integral
                else:
                    n_col_act += 1
                    I[n][k] = (4**(k)) * (I[n][k-1] - I[n-1][k-1]) / (4**(k) - 1)


                print(I)

    print('La integral es:', round(I[n][k], 6))

a = 0
b = 3
n_rec = 3
romberg(f,a,b,n_rec)