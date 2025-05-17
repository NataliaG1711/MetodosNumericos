import numpy as np

def f(x):

    return x**2

n_rec = 5
a = 0 
b = 3

delta_x = (b-a)/n_rec
x = np.linspace(a,b,n_rec+1)

sum_izq = 0
sum_der = 0
sum_med = 0

for i in range(len(x)-1):
    sum_izq += f(x[i]) * delta_x
    sum_der += f(x[i+1])* delta_x
    sum_med += f((x[1+i] + x[i])/2) * delta_x

print('{:<30} {:<30} {:<30}'. format('Ext izq', 'medio', 'ext der'))
print('{:<30} {:<30} {:<30}'. format(sum_izq,sum_med,sum_der))


    
        