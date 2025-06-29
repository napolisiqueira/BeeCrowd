"""

Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares
ou ímpares. Só que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois
vetores encher, você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem
lidos. Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo
primeiro os valores do vetor impar. Cada vetor pode ser preenchido tantas vezes quantas for necessário.

Entrada
A entrada contém 15 números inteiros.

Saída
Imprima a saída conforme o exemplo abaixo.

"""

par = []
impar = []
for i in range(15):
    valor = int(input())
    if(valor % 2 == 0):
        par.append(valor)
    else:
        impar.append(valor)
    
    if(len(par)==5):
        ix = 0
        for v in par:
            print("par[%d] = %d" %(ix,v))
            ix += 1
        par = []
    if(len(impar)==5):
        ix = 0
        for v in impar:
            print("impar[%d] = %d" %(ix,v))
            ix += 1
        impar = []
if(len(impar)> 0):
    ix = 0
    for v in impar:
        print("impar[%d] = %d" %(ix,v))
        ix += 1

if(len(par)>0):
    ix = 0
    for v in par:
        print("par[%d] = %d" %(ix,v))
        ix += 1