#Modulos de algebra lineal
#Programa 1: Producto escalar

#Código Andrea
def ProductoEscalar (a,b):
    operacion=(a[0]*b[0])+(a[1]*b[1])+(a[2]*b[2])+(a[3]*b[3])
    return (operacion)
#Programa principal
a=[5,10,20,30]
b=[23,78,45,67]

resultado=ProductoEscalar(a,b)
print ("El producto escalar de los vectores a y b son:",resultado)
