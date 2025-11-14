#CODIGO 3 DESCOMPOSICION QR USANDO GRAN SMIDHT
import numpy as np

def qr_descomposicion_gram_schmidt(A):
    n_filas, n_columnas = A.shape
    Q = np.zeros((n_filas, n_columnas))
    R = np.zeros((n_columnas, n_columnas))

    for j in range(n_columnas):
        v = A[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        if R[j, j] > 1e-10:
            Q[:, j] = v / R[j, j]

    return Q, R

# Ejemplo
A = np.array([[5.0, 1.0, 4.0],
              [3.0, 1.0, 1.0],
              [0.0, 1.0, 1.0]])

Q, R = qr_descomposicion_gram_schmidt(A)

print("Matriz Q (ortonormal):")
print(Q)
print("\nMatriz R (triangular superior):")
print(R)