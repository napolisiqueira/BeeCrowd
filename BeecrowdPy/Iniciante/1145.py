"""

Escreva um programa que leia dois valores X e Y. A seguir, mostre uma sequência de 1 até Y,
passando para a próxima linha a cada X números.

Entrada
O arquivo de entrada contém dois valores inteiros, (1 < X < 20) e (X < Y < 100000).

Saída
Cada sequência deve ser impressa em uma linha apenas, com 1 espaço em branco entre cada número,
conforme exemplo abaixo. Não deve haver espaço em branco após o último valor da linha.

"""
# import time
import sys

number_one, number_two = map(int, input().split(" "))


# inicio = time.time()
i = 1
while True:
    p = 1
    if i < number_one:
        r = ""
        while p <= number_two :
            r+= str(f" {i} ")
            p += 1
            i += 1
        print(r.strip())
    else:
        sys.exit()
    # else:
    #     fim = time.time()
    #     break

# tempo_execucao = fim - inicio
# print(f"Tempo de execução: {tempo_execucao:.2f} segundos")