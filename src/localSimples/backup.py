#local simples não possui qualquer RPC, apenas a programação tradicional, tudo em um unico bloco, necessário utilizar paralelismo de threads
#enquanto uma thread irá processar (multiplicar) uma parte da matriz enquanto que outra thread processa (multiplica) a outra parte.
#Ao final, você precisará realizar a junção dos dois resultados (merging) para compor um resultado final
#https://pt.stackoverflow.com/questions/384972/como-fa%C3%A7o-para-multiplicar-duas-matrizes-no-python

#def main()
def main():  
    #Carregar os arq txt das matrizes

    #loadMatrizA recebe o  comando open responsável por localizar e trazer o arq
    #loadedMatrizA recebe a var anterior e realiza a leitura das linhas
    #no print é mostrado a Matriz A, processo se repete para a B
    
    loadMatrizA = open("./matrizes_win/matA_win_teste.txt",'r')
    loadedMatrizA =loadMatrizA.readlines()#matriz A carregada
    print("Matriz A:\n\t",loadedMatrizA)
    
    #carregar matriz B
    loadMatrizB = open("./matrizes_win/matB_win_teste.txt",'r')
    loadedMatrizB =loadMatrizB.readlines()#matriz B carregada
    print("Matriz B:\n\t",loadedMatrizB)

    class multiMatrizes():
        def __init__(self,mat):
            self.mat = mat
            self.lin = len(loadedMatrizA)
            self.col= len(loadedMatrizB)
        
        def getLinha(self, nLinhas):
            return[i for i in self.mat[nLinhas]]
        
        def getColunas(self, nColunas):
            return[i[nColunas] for i in self.mat]
        
        def __mul__(self,mat2):
            matrizResultado = []
            

            for i in range(self.lin):
                matrizResultado.append([])

                for j in range(mat2.col):
                    listMult = [x*y for x, y in open(self.getLinha(i), mat2.getColunas(j))]
                    matrizResultado[i].append(sum(listMult))
    print("Resultado: \n",loadedMatrizA * loadedMatrizB)

    