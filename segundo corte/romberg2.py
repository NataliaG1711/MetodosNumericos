import numpy as np

def f(x):
    return x**3

def romberg(f, a, b, n_rec):
    I = np.zeros((n_rec, n_rec)) 
    for n in range(n_rec):
        N = 2**n
        h = (b - a) / N
        x = np.linspace(a, b, N + 1)
        I[n][0] = h * (f(x[0]) / 2 + np.sum(f(x[1:-1])) + f(x[-1]) / 2)

    for k in range(1, n_rec):
        for n in range(k, n_rec):
            I[n][k] = (4**k * I[n][k-1] - I[n-1][k-1]) / (4**k - 1)

    print(I)
    print('La integral es:', round(I[n_rec-1][n_rec-1], 6))

a = 0
b = 3
n_rec = 3
romberg(f, a, b, n_rec)