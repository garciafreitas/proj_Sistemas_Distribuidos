import time

createMatrizC = open('matC.txt', 'w')
matrizResultado = []

#carregar matriz A
loadMatrizA = open("./matrizes_win/matA_win_teste.txt",'r')
loadedMatrizA = loadMatrizA.readlines()#matriz A carregada
map(float, loadedMatrizA)
print("Matriz A:\n\t",loadedMatrizA)

#carregar matriz B
loadMatrizB = open("./matrizes_win/matB_win_teste.txt",'r')
loadedMatrizB = loadMatrizB.readlines()#matriz B carregada
map(float, loadedMatrizB)
print("Matriz B:\n\t",loadedMatrizB)

#print ("\tMatrizResultado --> \n",loadedMatrizA * loadMatrizB)

def multiMatrizes():
    def _init_(self,loadedMatrizA):
        self.mat = loadedMatrizA
        self.linha_A = len(loadedMatrizA.linha_A[0])
        self.coluna_A= len(loadedMatrizA.coluna_A[0])
        
    def _mul_(self,loadedMatrizB):
        self.mat = loadedMatrizB
        self.mat = loadedMatrizB
        self.linhaha_B = len(loadedMatrizB.linha_B[0])
        self.coluna_B= len(loadedMatrizB.coluna_B[0])
    assert loadedMatrizA.coluna_A == loadedMatrizB.coluna_B

    
    for linha_A in range(loadedMatrizA.linha_A):
            # Adicionando linha
                matrizResultado = []
                for colunauna in range(loadedMatrizB.coluna_B):
                        #adicionando uma nova coluna na linha
                        matrizResultado[loadedMatrizA.linha_A].append(0)
                        for k in range(loadedMatrizA.coluna_A):
                            matrizResultado[loadedMatrizA.linha_A][colunauna] += loadedMatrizA.coluna_A[loadedMatrizA.linha_A][k] * loadedMatrizB.coluna_B[k][colunauna]
    return matrizResultado
createMatrizC.readlines(matrizResultado)
print('Resultado:',matrizResultado)
print("\n\nMatriz C foi criada com o calculo.")
time.perf_counter()