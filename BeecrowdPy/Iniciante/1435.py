"""

Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, e construa
a matriz de acordo com o exemplo abaixo.

Entrada
A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas.
O final da entrada é marcado por um valor de ordem igual a zero (0).

Saída
Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. Os valores das matrizes devem
ser formatados em um campo de tamanho 3 justificados à direita e separados por espaço. Após o último caractere de cada
linha da matriz não deve haver espaços em branco. Após a impressão de cada matriz deve ser deixada uma linha em branco.

"""

while True:
    N = int(input())
    if N == 0:
        break

    matriz = [[0 for _ in range(N)] for _ in range(N)] 
    for i in range(N):
        for j in range(N):
            dist_top = i
            dist_bottom = (N - 1) - i
            dist_left = j
            dist_right = (N - 1) - j

            matriz[i][j] = min(dist_top, dist_bottom, dist_left, dist_right) + 1

    for i in range(N):
        for j in range(N):
            if j == 0:
                print(f"{matriz[i][j]:>3d}", end="")
            else:
                print(f" {matriz[i][j]:>3d}", end="")
        print() 

    print() 