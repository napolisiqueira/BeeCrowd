"""


Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 15), correspondente a ordem de uma matriz M de inteiros, e construa a matriz
de acordo com o exemplo abaixo.

Entrada
A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. O final da
entrada é marcado por um valor de ordem igual a zero (0).

Saída
Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. Os valores das matrizes devem ser formatados
em um campo de tamanho T justificados à direita e separados por espaço, onde T é igual ao número de dígitos do maior número da matriz.
Após o último caractere de cada linha da matriz não deve haver espaços em branco. Após a impressão de cada matriz deve ser deixada
uma linha em branco.


"""

import math

def digitos(numero):
  return math.floor(math.log10(numero)) + 1

while True:
  try:
    N = int(input())

    if (N == 0):
      break

    limite = digitos(1 << (2 * N - 2))

    for i in range(N):
      print(str(1 << i).rjust(limite), end='')
      for j in range(1, N):
        print(' ', end='')
        print(str(1 << (i + j)).rjust(limite), end='')
      print('')
    print('')
  except EOFError:
    break