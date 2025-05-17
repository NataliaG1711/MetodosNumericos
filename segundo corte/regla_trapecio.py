#LEER SOBRE REGLA TRAPECIO Y REGLA DE SIMPSON
#COMO CALCULAR EL AREA BAJO LA CURVA USANDO N TRAPECIOS
#REGLA DE SIMPSON 1/3
#REGLA DE SIMPSON 1/3 CON N INTERVALOS
#METODO DE ROMBERG
#APRENDER A USAR INDICES
import numpy as np

def f(x):
    return x**2

n_trap = 100
a = 0
b = 3
x = np.linspace(a,b,n_trap + 1)
suma = 0
for i in range(1, len(x) - 1):
    suma += f(x[i])

integral = (b-a)* (f(x[0])+f(x[n_trap]) + 2*suma) / (2 * n_trap)

print('{:<30}'. format('Regla del trapecio'))
print('{:<30}'. format(integral))


