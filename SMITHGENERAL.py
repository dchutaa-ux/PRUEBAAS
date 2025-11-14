#CODIGO 2 GRAM SCHIMIDT GENERAL
import numpy as np
def gram_schmidt(vectors):
    orthonormal_basis = []
    for v in vectors:
        w=v.copy()
        for u in orthonormal_basis:
            proj = np.dot(w,u)*u
            w=w-proj
        norm=np.linalg.norm(w)
        if norm > 1e-10:
                w=w/norm
                orthonormal_basis.append(w)
    return orthonormal_basis
            #ejemplo
v=[np.array([2.0,1.0,0.0]),np.array([4.0,0.0,1.0])]
Q=gram_schmidt(v)
for i,q in enumerate (Q):
    print(f"Vector ortonormal {i+1}: {q}")
