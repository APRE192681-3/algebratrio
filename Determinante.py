#Modulos de algebra lineal
#Programa 3: Determinate de una matriz 2x2

#Codigo Rodrigo
def Determinante(a,b):
    operacion=(a[0]*b[1])-(b[0]*a[1])
    return (operacion)
#se descompuso la matriz en 2 listas tal que a corresponde al renglon 1 y b corresponde al renglon 2
a=[5,-3]
b=[6,7]
resultado=Determinante(a,b)
print("El determinate de la matriz es: ",resultado)
