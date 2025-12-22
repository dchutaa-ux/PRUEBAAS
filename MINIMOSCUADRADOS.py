import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import LIBRERIA as lib

#define true model parameters
xa, xb=-3, 5 #intervalo
x=np.linspace(xa,xb,500) #intervalo sobre el cual efectuamos el esperimento
a, b, c, d= 1, 2, 5, 4
y_exact=a+b*x+c*x**2+d*x**3

#simulate noisy data
m=50
#X=1-2*np.random.rand(m) #entre -1 y 1
X=xa + (xb-xa)*np.random.rand(m)
Y=a+b*X+c*X**2+d*X**3+20*np.random.randn(m) #c*n.random.randn(m) el c representa que los puntos se van alejar de la gráfica inicial osea más ruido osea mas coeficientes osea más dispersión

#fit the data to the model using linear least square
A=np.vstack([X**0, X**1, X**2, X**3]) #see np.vander for alternative #A:matriz de coeficientes
#sol, r, rank,sv = la.lstsq(A.T,Y) #la.lstsq resuelve por mínimos cuadrados


At=np.array([X**0,X**1,X**2,X**3])
auxMat=np.matmul(At,At.T) #auxMat es At_T*A
np.reshape(Y,(m,1))
b=np.matmul(At,Y)
b=b.reshape(-1,1)
sol=lib.GaussElimiPiv(auxMat,b)


y_fit=sol[0]+sol[1]*x+sol[2]*x**2+sol[3]*x**3
fig, ax=plt.subplots(figsize=(12,4))


ax.plot(X, Y, 'go', alpha=0.5, label='Simulated data')
ax.plot(x, y_exact , 'r', lw=2, label='True value $y=1+2x+150x^2+200x^3$')
ax.plot(x, y_fit, 'b', lw=2, label='Least square fit')
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"$y$", fontsize=18)
ax.legend(loc=2)
plt.show()