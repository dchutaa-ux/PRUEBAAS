#CODIGO 1 RANGO DE UNA MATRIZ POR ELIMINACION GAUSEANA
import numpy as np
def rango_por_gauss(A):
    
    A = A.astype(float)  
    filas, columnas = A.shape
    fila_actual = 0

    for col in range(columnas):
        # Buscar fila con pivote no nulo
        pivote = None
        for f in range(fila_actual, filas):
            if A[f, col] != 0:
                pivote = f
                break

        if pivote is not None:

            if pivote != fila_actual:
                A[[fila_actual, pivote]] = A[[pivote, fila_actual]]
            
            A[fila_actual] = A[fila_actual] / A[fila_actual, col]
            
            for f in range(fila_actual + 1, filas):
                A[f] = A[f] - A[f, col] * A[fila_actual]

            fila_actual += 1

    rango = sum([not np.allclose(row, 0) for row in A])
    return rango

# Ejemplo
M = np.array([[1, -1, 3, 1],
              [2, -2, 6, 2],
              [1, 4, 3, 2]])

rango = rango_por_gauss(M)
print(f"El rango de la matriz es: {rango}")