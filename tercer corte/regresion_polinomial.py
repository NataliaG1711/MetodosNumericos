from matplotlib import pyplot as plt
import numpy as np

def min_cuad(x, y):
    sumXY = 0
    sumXX = 0
    sumX = 0
    sumY = 0
    n = len(x)
    for i in range(len(x)):
        sumXY += x[i] * y[i]
        sumXX += x[i] ** 2
        sumX += x[i]
        sumY += y[i]   

    a1 = (n * sumXY - sumX * sumY) / (n * sumXX - sumX ** 2)
    a0 = (sumY - a1 * sumX) / n
    return a0, a1  

x_dato = np.array([0,1,2,3,4,5,6,7,8])
y_dato = np.array([0,1,4,9.5,17,27,38,50,70])
a0, a1 = min_cuad(x_dato, y_dato)
print(a0, a1)

y_est = a0 + a1 * x_dato

media_y = np.mean(y_dato)

num = np.sum((y_est-media_y) ** 2)
den = np.sum((y_dato-media_y) ** 2)
r = np.sqrt(num/den)
print('r =', r)


resol = 20
xx = np.linspace(-1, 10, resol)
yy = a0 + a1 * xx

fig,ax = plt.subplots()
ax.plot(xx, yy, 'r')
ax.plot(x_dato, y_dato, 'o')
plt.show()