import numpy as np

def f(x):
    return np.sqrt(x**7+1)

n_rec = 4
a = 1
b = 4
x = np.linspace(a,b,n_rec + 1)

suma_par = 0
suma_impar = 0
for i in range(1, len(x) - 1):
    if i % 2 == 0:
        suma_par += f(x[i])
    else:
        suma_impar += f(x[i])

integral = (b-a)* (f(x[0])+ (4 * suma_impar) + (2 * suma_par) +  f(x[n_rec])) / (3 * n_rec)

print('{:<30}'. format('Regla de simpson'))
print('{:<30}'. format(integral))

