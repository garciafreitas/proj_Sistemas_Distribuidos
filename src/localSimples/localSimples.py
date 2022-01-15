import time

createMatrizC = open('matC.txt', 'w')

loadMatrizA = open("./matrizes_win/matA_win_teste.txt",'r')

#carregar matriz A
loadedMatrizA = loadMatrizA.readlines()#matriz A carregada
print("Matriz A:\n\t",loadedMatrizA)

#carregar matriz B
loadMatrizB = open("./matrizes_win/matB_win_teste.txt",'r')
loadedMatrizB = loadMatrizB.readlines()#matriz B carregada
print("Matriz B:\n\t",loadedMatrizB)

print ("\tMatrizResultado --> \n",loadedMatrizA * loadMatrizB)

def multiMatrizes():
    def _init_(self,loadedMatrizA):
        self.mat = mat
        self.linha_A = len(linha_A[0])
        self.coluna_A= len(coluna_A[0])
        
    def _mul_(self,loadedMatrizB):
        self.mat = mat
        self.linhaha_B = len(linha_B[0])
        self.coluna_B= len(coluna_B[0])
    assert coluna_A == coluna_B

    matrizResultado = []
    for linhaha in range(linha_A):
            # Adicionando linha
                matrizResultado = []
                for colunauna in range(coluna_B):
                        #adicionando uma nova coluna na linha
                        matrizResultado[linhaha].append(0)
                        for k in range(coluna_A):
                            matrizResultado[linhaha][colunauna] += coluna_A[linhaha][k] * coluna_B[k][colunauna]
    return matrizResultado
createMatrizC.writelinhaes(matrizResultado)
print("Matriz C foi criada com o calculo.")
time.perf_counter()