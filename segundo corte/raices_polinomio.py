import numpy as np
#p(x) = 6-5*x+2x**2
def raices_polinomio():
    coef = [6, -5,2]
    n = len(coef)
    C = np.zeros((n-1,n-1))
    C[:-1,1:n] = np.eye(n-2)
    C[-1,:] = -np.array(coef[:n-1])/coef[n-1]
    print(C)

    raices = np.linalg.eigvals(C)
    print("Raices del polinomio:", raices)
    
raices_polinomio()
