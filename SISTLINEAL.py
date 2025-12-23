import numpy as np
import LIBRERIA as lib
import time


A=np.random.rand(4,4)
b=np.random.rand(4,1)

start_time = time.perf_counter() #para calcular el tiempo iniciado
X=lib.GaussElimSimple(A,b)
normErr1 = np.linalg.norm(A@X-b,1) #Error no tan bueno
end_time = time.perf_counter() #para calcular el tiempo final
elapsed_time1= end_time - start_time #para calcular el tiempo total
#print("El tiempo en segundos en calcular es: \n",elapsed_time1)

#print("||Ax-b||_1: es la norma L1 \n",np.linalg.norm(A@X-b,1)) #ord=1: La norma L1 o de Manhattan, que es la suma de los valores absolutos de los elementos.
#A la matriz AX-b le saca la norma1 y está bien condicionado cuando la respuesta es 0 o casi 0  
#print("||Ax-b||_1: es la norma L2 o Euclidiana \n",np.linalg.norm(A@X-b,2)) #ord=2: La norma L2 o Euclidiana que es la raíz cuadrada de la suma de los cuadrados de los elementos.
#print("||Ax-b||_1: es la norma del infinito \n",np.linalg.norm(A@X-b,np.inf)) #inf = La norma del infinito, que es el valor absoluto máximo de un elemento


start_time = time.perf_counter() #para calcular el tiempo iniciado
X = lib.GaussElimiPiv(A,b) #Mejor error
normErr2 = np.linalg.norm(A@X-b,1)
end_time = time.perf_counter() #para calcular el tiempo final
elapsed_time2= end_time - start_time #para calcular el tiempo total
#print("El tiempo en segundos en calcular es: \n",elapsed_time2)


start_time = time.perf_counter() #para calcular el tiempo iniciado
X = np.linalg.solve(A,b) #Mejor error y tiene menor costo computacional (osea menos tiempo en calcular)
normErr3 = np.linalg.norm(A@X-b,1)
end_time = time.perf_counter() #para calcular el tiempo final
elapsed_time3= end_time - start_time #para calcular el tiempo total
#print("El tiempo en segundos en calcular es: \n",elapsed_time3)


#print("El error de la normaErr1 \n", normErr1)
#print("El error de la normaErr2 \n", normErr2)
#print("El error de la normaErr3 \n", normErr3)
print ("{:25s}{:25s}{:25s}".format("Error Gauss simple","Erros Gauss piv","Error linalg.solve"))
print("-"*70)
print("{:20e} {:20e} {:20e}".format(normErr1,normErr2,normErr3))

print ("{:25s}{:25s}{:25s}".format("Gauss simple time","Gauss piv time","linalg.solve time"))
print("-"*70)
print("{:20e} {:20e} {:20e}".format(elapsed_time1,elapsed_time2,elapsed_time3))