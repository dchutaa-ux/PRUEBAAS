import numpy as np

# Definir la matriz A
A = np.array([[2, 1],
              [5, 3]])

# Calcular el determinante
det_A = np.linalg.det(A)

print(f"Determinante de A: {det_A:.2f}")
