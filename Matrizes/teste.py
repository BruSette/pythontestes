'''
Created on 6 de set de 2016

@author: bruno
'''
def crie_matriz(n_linhas, n_colunas, valor):
    matriz = [] 
    for i in range(n_linhas):
        linha = [] 
        for j in range(n_colunas):
            linha.append(valor)
        matriz.append(linha)
   
    return matriz
   
A = crie_matriz(5,5,0)
A[1][1] = 2
print(A[1][1])