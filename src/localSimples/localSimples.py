import time

createMatrizC = open('matC.txt', 'w')
matrizResultado = []

#carregar matriz A
loadMatrizA = open("./matrizes_win/matA_win_teste.txt",'r')
#loadMatrizA = loadMatrizA.readlines()#matriz A carregada

#carregar matriz B
loadMatrizB = open("./matrizes_win/matB_win_teste.txt",'r')

for linhaA in loadMatrizA:
   linhasA = linhaA.split()
   #print(linhasA[0],linhasA[1],linhasA[2])
   for colunaA in loadMatrizB:
       matrizResultado[linhasA.append(0)]
       for k in range(loadMatrizA.colunaA):
           matrizResultado[loadMatrizA.linhasA][colunaA] +=loadMatrizA.coluna_A[loadMatrizA.linha_A][k] * loadMatrizB.coluna_B[k][colunaA]