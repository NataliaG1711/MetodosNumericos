#AGARRAR UNA FUNCION QUE CORTE AL EJE X EN VARIOS PUNTOS(FUNCION DE BESSEL) LLAMAR SCIPY.SPECIAL IMPORT JN
#ENCONTRAR LOS INTERVALOS DONDE ESTÁN LAS RAICES (METODO DE BISECCION)
#DESPUES DE ENCONTRAR LOS INTERVALOS, CALCULAR LA RAIZ DE CADA INTERVALO
#COMO SE ENCUENTRAN LOS INTERVALOS? ESCOGER UN X0 Y X1
# X0 = 0; X1 = X0 + DELTA(X), DEPENDE DEL INTERVALO QUE QUIERA RECORRER, POR EJEMPLO DELTA(X) = 0.15
#DONDE SE ENCUENTRA LA RAIZ SE ALMACENA EN UNA LISTA, SE PASA EL SIG INTERVALO Y SE ACTUALIZAN LOS VALORES
#F(X0)*F(X1)<0
from scipy.special import jn
import biseccion_bessel
'''
def intervals(funcion, orden, x0, x1, avance = 0.15):
    intervalos = []
    x_act = x0
    act = funcion(orden, x_act)

    for x_sig in range(x0+1, x1+1):
        sig = funcion(orden, x_sig)
        if act * sig < 0:
            intervalos.append((x_act, x_sig))

        x_act = x_sig
        act= sig

        return intervalos

'''

def intervals(funcion, orden, x0, x1, avance=0.15):
    intervalos = []
    x_act = x0
    
    while x_act < x1:
        x_sig = x_act + avance
        act = funcion(orden, x_act)
        sig = funcion(orden, x_sig)
        
        if act * sig < 0:
            intervalos.append((x_act, x_sig))
        
        x_act = x_sig
    
    return intervalos
    
def bessel(n, x):
    return jn(n,x)

x0 = 0
x1 = 20

orden = 1

intervalos = intervals(bessel, orden, x0, x1)

print("-" * 50)

for i, intervalo in enumerate(intervalos):
    raiz = biseccion_bessel.biseccion(bessel, orden, intervalo[0], intervalo[1])
    if raiz is not None:
        print(f'Intervalo {i+1}: [{intervalo[0]}, {intervalo[1]}]')
        print(f'Raíz: {raiz}')
        print("-" * 50)