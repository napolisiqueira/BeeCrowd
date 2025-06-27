"""

Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

Entrada
Não há nenhuma entrada neste problema.

Saída
A saída contém um valor correspondente ao valor de S.
O valor deve ser impresso com dois dígitos após o ponto decimal.

"""

impares = []
exponencial = 2
exponenciais = [] 

for i in range(2, 40):
    if i % 2 == 1:
        impares.append(i)

for i in range(len(impares)+1):
    exponenciais.append(exponencial)
    exponencial += exponencial

result = 1
for i in range(len(impares)):
    result += (impares[i] / exponenciais[i])

print(f"{result:.2f}")