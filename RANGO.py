#CODIGO 5 INVERSA DE UNA MATRIZ USANDO DESCOMPOSCION QR
import numpy as np

def inversa_por_qr(A):
    Q, R = np.linalg.qr(A)
    if np.linalg.matrix_rank(R) < R.shape[0]:
        raise ValueError("La matriz no es invertible (R no tiene rango completo).")

    R_inv = np.linalg.inv(R)
    Q_T = Q.T
    A_inv = R_inv @ Q_T
    return A_inv

# Ejemplo
A = np.array([[2.0, 7.0],
              [5.0, 6.0]])

A_inv = inversa_por_qr(A)
print("Inversa de A usando QR:")
print(A_inv)