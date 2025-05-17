import sympy as sp


def mclaurin(x_val, a=4, order=4):
    x = sp.symbols('x')
    f = sp.sqrt(x)
    
    serie = sp.sqrt(a)
    
    fact = 1
    
    for n in range(1, order + 1):

        derivada = sp.diff(f, x, n)
        fact *= n
        serie += (derivada.subs(x, a) / fact) * (x - a) ** n
    
    f_aprox = sp.lambdify(x, serie, 'numpy')
    
    return f_aprox(x_val)

x = 3
aprox = 2 * mclaurin(x)

print(f"Aproximación: {aprox}")
