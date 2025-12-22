# CODIGO 4 INVERSA DE UNA MATRIZ POR ELIMINACION GAUSEANA
import numpy as np

def inversa_por_gauss(A):
    n = A.shape[0]
    I = np.identity(n)
    AI = np.hstack((A.astype(float), I))  # Matriz aumentada [A | I]

    for i in range(n):
        if AI[i, i] == 0:
            for j in range(i+1, n):
                if AI[j, i] != 0:
                    AI[[i, j]] = AI[[j, i]]
                    break
            else:
                raise ValueError("La matriz no es invertible.")

        AI[i] = AI[i] / AI[i, i]

        for j in range(n):
            if i != j:
                AI[j] = AI[j] - AI[j, i] * AI[i]

    A_inv = AI[:, n:] 
    return A_inv

# Ejemplo
A = np.array([[1, 1, 0, 0],
              [0, -1, -2, 0],
              [0, 0, 1, -1],
              [0, 0, 0, 1]])

A_inv = inversa_por_gauss(A)
print("Matriz inversa:")
print(A_inv)