#CODIGO 6 DETERMINANTE USANDO OPERACIONES ELEMENTALES
import numpy as np
def determinante_por_gauss(A):
    A = A.astype(float)
    n = A.shape[0]
    det = 1.0
    num_swaps = 0

    for i in range(n):
        if A[i, i] == 0:
            for j in range(i+1, n):
                if A[j, i] != 0:
                    A[[i, j]] = A[[j, i]]
                    num_swaps += 1
                    break
            else:
                return 0.0  

        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j] = A[j] - factor * A[i]

    for i in range(n):
        det *= A[i, i]

    if num_swaps % 2 == 1:
        det *= -1

    return det

# Ejemplo
M = np.array([[5, 1, 2, 0],
              [0, 1, -1, 2],
              [0, 0, 5, 2],
              [-1, -3, 0, 1]])

print("Determinante por Gauss:", determinante_por_gauss(M))
