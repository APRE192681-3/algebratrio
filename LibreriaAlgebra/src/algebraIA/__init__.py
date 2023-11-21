#Modulos de algebra lineal
#Programa 3: Determinate de una matriz 2x2

#Codigo Rodrigo
def Determinante(a,b):
    operacion=(a[0]*b[1])-(b[0]*a[1])
    return (operacion)
#se descompuso la matriz en 2 listas tal que a corresponde al renglon 1 y b corresponde al renglon 2

#Modulos de algebra
#Programa 2: magnitud de un vector en R2
#Código Andrea
def MagnitudVector (x,y):
    operacion=(x**2)+(y**2)
    magnitud=operacion**0.5
    return(magnitud)

#Modulos de algebra lineal
#Programa 1: Producto escalar

#Código Andrea
def ProductoEscalar (a,b):
    operacion=(a[0]*b[0])+(a[1]*b[1])+(a[2]*b[2])+(a[3]*b[3])
    return (operacion)

def SumaMatrices(A,B):
    resultado=[]
    for i in range(len(A)):
        fila=[]
        for y in range(len(A[0])):  
            fila.append(A[i][y] + B[i][y])
        resultado.append(fila)

    return resultado

def suma_vectores(vector1, vector2):
    resultado=[]
    for i in range(len(vector1)):
        resultado.append(vector1[i] + vector2[i])
    return resultado
    