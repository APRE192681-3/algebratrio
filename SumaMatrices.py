#suma de matrices

def SumaMatrices(A,B):
    resultado=[]
    for i in range(len(A)):
        fila=[]
        for y in range(len(A[0])):  
            fila.append(A[i][y] + B[i][y])
        resultado.append(fila)

    return resultado

A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[9,8,7],[6,5,4],[3,2,1]]

resultado = SumaMatrices(A,B)
print(resultado)


    
