import numpy as np

# Definir la matriz A
A = np.array([[2, 1],
              [5, 3]])

# Verificar si la matriz es invertible
if np.linalg.det(A) != 0:
    A_inv = np.linalg.inv(A)
    print("La matriz inversa es:")
    print(A_inv)
else:
    print("La matriz no es invertible (determinante igual a cero).")
