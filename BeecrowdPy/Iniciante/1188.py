"""
Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida,
calcule e mostre a soma ou a média considerando somente aqueles elementos que estão na área inferior da matriz,
conforme ilustrado abaixo (área verde).

Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média)
que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante de dupla precisão
(double) que compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

"""



resp: str = input()
lista: list =[]
for i in range(12): 
    for j in range(12):
        valor: float = float(input())
        if i > 6 and i > j and j > 11 - i:
            lista.append(valor)


if resp == "S":
    print(f"{sum(lista):.1f}")
elif resp == "M":
    print(f"{(sum(lista)/len(lista)):.1f}")