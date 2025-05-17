def biseccion(f, orden, a, b, tol = 10**-6):
    error = float('inf')
    iteraciones = 0


    while error > tol:  
        m = (a + b) / 2  
        error = abs((b - a) / 2)
        iteraciones += 1


        print('{:<3} {:<22} {:<25}'.format(iteraciones, m, error))
        
        if f(orden, a) * f(orden, m) < 0: 
            b = m
        else:  
            a = m

    return m