#CODIGO 8 RESOLUCION DE SISTEMAS LINEALES USANDO ELIMINACION DE GAUSS
import numpy as np

def resolver_por_gauss(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)

    
    Ab = np.hstack([A, b.reshape(-1, 1)])

    for i in range(n):
        # Pivote no nulo
        if Ab[i, i] == 0:
            for j in range(i+1, n):
                if Ab[j, i] != 0:
                    Ab[[i, j]] = Ab[[j, i]]
                    break
        Ab[i] = Ab[i] / Ab[i, i]
        for j in range(i+1, n):
            Ab[j] = Ab[j] - Ab[j, i] * Ab[i]

    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])

    return x

# Ejemplo
A = np.array([[2.0, 1.0],
              [1.0, 3.0]])
b = np.array([1.0, 2.0])

x = resolver_por_gauss(A, b)
print("Solución del sistema Ax = b:")
print(x)