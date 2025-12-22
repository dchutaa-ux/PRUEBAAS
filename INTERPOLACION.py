import numpy as np
import LIBRERIA as lib
import matplotlib.pyplot as plt
import numpy.polynomial as poly


'''Interpolación''' #La interpolación genera una interpolación buena mientras más datos hay
#x=np.array([0,1,2,3,4,5,7,8,9,11,12,13,14,15,16,17,18,19]) #coordenadas "x" de los puntos a interpolar
x=np.arange(1,50)
#y=np.array([1,3,-4,-5,17,-19]) #coordenadas "y" de los puntos a interpolar
y=np.sin(x)
pol=lib.interpLagrange(x,y)

print(pol)
print(pol(x))

'''Gráfica'''
a=x.min()
b=x.max() #aumentamos valores en el eje x
#b=x.max()+2 #aumentamos valores en el eje x, +2
xx=np.linspace(a,b,200)
yy=pol(xx)
yy_Exacta=np.sin(xx)

fig, ax=plt.subplots(figsize=(10,8))
ax.plot(xx,yy,'b',lw=2,label='Polinomio interpolante')
ax.plot(x,y,'ro',alpha=0.6,label='Datos')
ax.plot(xx,yy_Exacta,'g',lw=2,label='Polinomio solución exacta')
ax.legend(loc=2)
ax.set_xlabel(r"$x$", fontsize=10)
ax.set_ylabel(r"$y$", fontsize=10)
plt.grid()
plt.show()