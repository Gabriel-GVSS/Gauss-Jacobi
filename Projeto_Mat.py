#calcular sistemas de equaçoes pelo metodo Gauss Jacobi
#Autor: Gabriel Victor da Silva Santos

from sympy import *
import numpy as np

arr=np.array([[15, 2, -1, -200],[2, 12, 1, -250],[1, 2, 8, 30]])
A = np.array([
    [10, 1, 1, 2, 3, -2, 6.57],
    [-4, -20, 3, 3, 2, 7, -68.448],
    [5, -3, 15, -1, -4, 1, -112.05],
    [-1, 1, 2, 8, -1, 2, -3.968],
    [1, 2, 1, 3, 9, -1, -2.18],
    [-4, 3, 1, 2, -1, 12, 10.882]
])

matx=A             #Mudar rapido de matriz

# variaveis que serã manipuladas com o tamanho das matrizes
Ncol=len(Matrix(matx).col(0))
Nlin=len(Matrix(matx).row(0))

def cond():                                           # Condição de matriz calculavel
   aux=0                                              # variavel auxiliar para saber se a condição da implemetação é valida

   matriz_atualizada = np.delete(matx, -1, axis=1)    # Elimina a ultima coluna da matriz

   for i in range(Ncol):                                          #interação para saber se o modulo da diagonal principal é maior que a soma do modulo dos outro
      soma_modulos = np.sum(np.abs(matriz_atualizada[i]))         #Calcula a soma das linhas em valores absolutos
      modulos_sub = soma_modulos-np.abs(matriz_atualizada[i, i])  #Subtrai o valor da diagonal principal

      if np.abs(matriz_atualizada[i, i])<= modulos_sub:            #condicional para saber se a matriz pode ser calculada por esse metodo
         print('Não pode ser implementada, resposta com erros')
         aux = 1

   if aux ==0:
      print('Pode ser implementada')
   return aux                                                       # Retorna valor 0 ou 1 para parar o codigo

def div():

   Mt_div = np.array([[]])          #Criando matrizes vazias para manipulaçao matematica
   Mt_som = np.array([[]])

   for i in range(Ncol):                                             #Cria uma matriz coluna com os valores da diagonal principal
      Mt_div = Matrix(Mt_div).row_insert(i, Matrix([matx[i, i]]))

   matriz_numpy1 = np.array(Mt_div.tolist(), dtype=float)            #Muda de tipo, do tipo sympy para numpy

   divisor = matx / matriz_numpy1                                    #Em uma nova variavel faz a divisao, entre a matriz dada e a diagonal principal

   for i in range(Ncol):                                             #Cria uma nova matriz apenas com a ultima coluna da matriz dada e a matriz da diagonal principal
      Mt_som = Matrix(Mt_som).row_insert(i, Matrix([divisor[i, -1]]))

   matriz_atualizada = np.delete(divisor, -1, axis=1)                #Exclui a ultima coluna da matriz dividida

   for i in range(Ncol):                                             #Na matriz dividida, adiciona 0 na diagonal principal
      matriz_atualizada[i,i] = 0

   return matriz_atualizada, Mt_som                                  #Retorna as duas matrizes



def implemt():
   x0=zeros(Ncol,1)                                   # Cria uma matriz coluna com valores 0
   xi=x0                                                    # Cria uma nova matriz igual a primeira
   for i in range(10):                                      # Implementaçao do codigo de Gauss Jacobi
      xi =matri_s - matri_d*x0
      x0=xi
   print()
   print('Resultados do x1 ao xn')
   print(xi)
   print()
   print('O erro aproximado da resposta é de:')
   print(xi-x0)



cond()

matri_d, matri_s = div()

implemt()



