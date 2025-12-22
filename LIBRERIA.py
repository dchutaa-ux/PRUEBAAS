import numpy as np
import numpy.polynomial as poly

def intercambiaFilas(A,fil_i,fil_j):
    A[[fil_i,fil_j],:]=A[[fil_j,fil_i],:]
    
def operacionFila(A,fil_m,fil_piv,factor):  #fil_m=fil_m - factor*fil_piv
     A[fil_m,:]=A[fil_m,:]=A[fil_m,:] - factor*A[fil_piv,:]
     
def rescaleFila(A,fil_m,factor):
         A[fil_m,:] = factor*A[fil_m,:]
         
def escalonaSimple(A):
    nfil=A.shape[0]
    ncol=A.shape[1]
    
    for j in range(0,nfil):
        for i in range(j+1,nfil):
            factor=A[i,j]/A[j,j]
            operacionFila(A,i,j,factor)
 
def escalonaConPiv(A):
    nfil=A.shape[0]
    ncol=A.shape[1]          
    for j in range(0,nfil): 
        imax=np.argmax(np.abs(A[j:nfil,j])) #estamos buscando por columnna quién tiene mayor absoluto; imax=índice
        intercambiaFilas(A,j+imax,j)
        for i in range(j+1,nfil):
            factor=A[i,j]/A[j,j]
            operacionFila(A,i,j,factor)  
            
def sustRegresiva (A,b): #Resuelve un sistema escalonada solo si A es escalonada (A triangular superior)
    N=b.shape[0] #A y b deben ser array numpy bidimensional 
    x=np.zeros((N,1))
    for i in range(N-1,-1,-1):
        x[i,0]=(b[i,0]-np.dot(A[i,i+1:N],x[i+1:N,0]))/A[i,i]
    return x #Array bidimensional 

def sustProgresiva (A,b): #Resuelve un sistema escalonada solo si A es escalonada (A triangular inferior)
    N=b.shape[0] #A y b deben ser array numpy bidimensional 
    x=np.zeros((N,1))
    for i in range(0,N):
        x[i,0]=(b[i,0]-np.dot(A[i,0:i],x[0:i,0]))/A[i,i]
    return x #Array bidimensional 


def GaussElimSimple(A,b):
    Ab=np.append(A,b,axis=1) #para crear la matriz aumentada
    escalonaSimple(Ab) #aplica esacalonamiento
    A1=Ab[:,0:Ab.shape[1]-1].copy()
    b1=Ab[:,Ab.shape[1]-1].copy()
    b1=b1.reshape(b.shape[0],1)
    x=sustRegresiva(A1,b1)
    return x #Array bidimensional      

def GaussElimiPiv(A,b):
    Ab=np.append(A,b,axis=1) #para crear la matriz aumentada
    escalonaConPiv(Ab) #aplica esacalonamiento
    A1=Ab[:,0:Ab.shape[1]-1].copy()
    b1=Ab[:,Ab.shape[1]-1].copy()
    b1=b1.reshape(b.shape[0],1)
    x=sustRegresiva(A1,b1)
    return x #Array bidimensional      

def hilbert_matrix(n): #Matriz mal condicionada 
   A=np.zeros((n,n))
   for i in range (1,n+1):
       for j in range(1,n+1):
           A[i-1,j-1]=1/(i+j-1)
   return A 
    
#DESCOMPOSICIÓN LU    
def LUdecomposition(A): #A debe ser una matriz cuadrada
    nrows = A.shape[0] #número de filas
    U=A.copy()
    L=np.eye(nrows,nrows,dtype=np.float64)
    
    for col in range(0,nrows-1): #desde la columnna 0 hasta la penúltima columna
        for row in range(col+1,nrows): #se modifica dese la columnna+1 hasta la última fila
            mult = U[row,col]/U[col,col] #Multiplicador
            L[row,col] = mult
            operacionFila(U,row,col,mult)
    return(L,U)

def SolveByLU(A,b):
    LU=LUdecomposition(A)
    L=LU[0] 
    U=LU[1]
    
    Y=sustProgresiva(L,b)
    X=sustRegresiva(U,Y)
    
    return X

def interpLagrange(cx,cy): #cx:coordenadas x = [x_1,...,x_n], cy:coordenadas y = [y_1,...,y_n]
    n=len(cx)
    p=poly.Polynomial([0]) # para construir el polinomio de posición 0, osea el término independent 
    for i in range(n):
        mascara =np.ones(n,dtype=bool)
        mascara[i]=False
        raices=cx[mascara]
        Laux=poly.Polynomial.fromroots(raices) # construye un polinomio con ceficientes que son las raices
        p=p+cy[i]*Laux/Laux(cx[i])
    return p