import numpy as np

a = 0
b = 3
NumRec = 4

def f(x):
    return x**2

def trapecio(NumRec):
    Rango = np.linspace(a, b, NumRec + 1)
    sumLarga = 0

    if NumRec == 0:
        return 0

    for i in range(1, NumRec):
        sumLarga += f(Rango[i])

    formulaLarga = (b - a) * (f(Rango[0]) + 2 * sumLarga + f(Rango[NumRec])) / (2 * NumRec)

    return formulaLarga

# Metodo Romberg

def Romberg(j, k, NumRec):
    matrizCeros = np.zeros((NumRec, NumRec))

    for k in range(NumRec):
        matrizCeros[k, 0] = trapecio(k+1)

    for j in range(1, NumRec):
        for k in range(j, NumRec):
            matrizCeros[k, j] = (4*(j+1) * matrizCeros[k, j - 1] - matrizCeros[k - 1, j - 1]) / (4*(j+1) - 1)

    return matrizCeros

result = Romberg(a, b, NumRec)
print(result)