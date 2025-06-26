"""

Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma de A + i para cada i com os valores (0 <= i <= N-1). Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.

Entrada
A entrada contém somente valores inteiros, podendo ser positivos ou negativos. Todos os valores estão na mesma linha.

Saída
A saída contém apenas um valor inteiro.

n2 --> Numero de vezes da iteração 

n3 numero que vai ser somado a soma
e depois somado 1


"""

lista = list(map(int, input("Digite dois valores: ").split(" ")))

n1 = lista[0]
for i in lista[1::1]:
    if not i <= 0:
        n2 = i

soma = 0
for i in range(n2):
    soma += n1 
    n1 += 1  
print(soma)