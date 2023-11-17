#Suma de vectores

def suma_vectores(vector1, vector2):
    resultado=[]
    for i in range(len(vector1)):
        resultado.append(vector1[i] + vector2[i])
    return resultado

vector1=[int(x) for x in input ("ingrese el primer vector").split()]
vector2=[int(x) for x in input ("ingrese el segundo vector").split()]

resultado=suma_vectores(vector1,vector2)
print(resultado)
