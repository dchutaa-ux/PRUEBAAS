# CODIGO 7 RESOLUCION DE SISTEMAS LINEALES USAND QR
import numpy as np

def resolver_por_qr(A, b):
  
    Q, R = np.linalg.qr(A)
    Qt_b = np.dot(Q.T, b)
    x = np.linalg.solve(R, Qt_b)
    return x

# Ejemplo
A = np.array([[2.0, 1.0],
              [1.0, 3.0]])
b = np.array([1.0, 2.0])

x = resolver_por_qr(A, b)
print("Solución del sistema Ax = b:")
print(x)