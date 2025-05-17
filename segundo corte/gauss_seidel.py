import numpy as np

iteraciones = 25
p = 2
tolerancia = 0.00001

A = np.array([[3,1,2], [2,1,1], [1,4,6]])
b = np.array([4,6,2])
#Diagonal
D = np.diag(np.diag(A))
#Diagonal inferior
L = np.tril(A)-D
#Diagonal superior
U = np.triu(A)-D

T = np.dot(-np.linalg.inv(D+L), U)

C = np.dot(-np.linalg.inv(D+L), b)

x0 = np.array([0,0,0])

for i in range(iteraciones):
    x1 = np.dot(T,x0) +C
    error = np.linalg.norm(x1-x0, ord=p)/np.linalg.norm(x1,ord=p)
    if error < tolerancia:
        break
    else:
        x0 = x1
    print(x1)


inv_A = np.linalg.inv(A)
sol = np.dot(inv_A, b.T)
print(sol)




























































