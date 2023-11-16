#Modulos de algebra
#Programa 2: magnitud de un vector en R2
#Código Andrea
def MagnitudVector (x,y):
    operacion=(x**2)+(y**2)
    magnitud=operacion**0.5
    return(magnitud)

#Código principal

x=2
y=2

resultado=MagnitudVector(x,y)
print("La magnitud es:",resultado)
    
