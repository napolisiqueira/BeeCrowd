"""

Faça um programa que leia um vetor A[100]. No final, mostre todas as posições do vetor que armazenam um
valor menor ou igual a 10 e o valor armazenado em cada uma das posições.

Entrada
A entrada contém 100 valores, podendo ser inteiros, reais, positivos ou negativos.

Saída
Para cada valor do vetor menor ou igual a 10, escreva "A[i] = x", onde i é a posição do vetor e x é o valor
armazenado na posição, com uma casa após o ponto decimal.

"""

i = 0
while True:
    number = float(input())

    if number <= 10:
        print(f"A[{i}] = {number}")
    i += 1

    if i >= 100:
        break