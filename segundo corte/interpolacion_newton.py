import numpy as np

'''
def f(x):
    return -0.55* x**3 + 3.83* x**2 - 6.67*x + 5.41

def new(xi, b, n, f,x):
    A = np.zeros((n, n))
    xi = np.linspace(xi, b, n)

    prod = np.zeros(n)
    prod[0] = 1
    prod[1] = x - xi[1]
    for i in range(2, n):
        prod[i] = prod[i - 1] * (x - xi[i-1])


    A[:, 0] = f(xi)

    for j in range(1, n):
        for i in range(j, n):
            A[i, j] = (A[i, j - 1] - A[i - 1, j - 1]) / (xi[i] - xi[i - j])
    print(A)

    diag = np.diag(A)
    p = diag[0]
    for j in range(1, n):
        p += diag[j] * prod[j]
    print(p)

xi = 0
b = 4
n = 4
x = 2.6
new(xi, b, n, f,x)
'''
import numpy as np

def newton_interpolation(xi, yi, x_eval):
    n = len(xi)
    # Crear una copia de yi para manipular
    coef = np.copy(yi)
    
    # Calcular las diferencias divididas
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (xi[i] - xi[i-j])
    
    # Evaluar el polinomio usando la forma de Newton
    resultado = coef[n-1]
    for i in range(n-2, -1, -1):
        resultado = resultado * (x_eval - xi[i]) + coef[i]
        
    return resultado

# Datos
xi = [0.9, 2.1, 2.9, 4.2]
yi = [2.1, 3.2, 4.9, 4.2]
x_eval = 2.6

# Resultado
p = newton_interpolation(xi, yi, x_eval)
print(f"Valor interpolado en x = {x_eval}: {p:.4f}")

























