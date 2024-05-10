import os
os.system("cls || clear")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

numUm = float(input("Digite o 1ª valor: "))
numDois = float(input("Digite o 2ª valor: "))

soma = numUm + numDois
media = soma / 2
produto = numUm * numDois
os.system("cls || clear")

maior = max(numUm, numDois)
menor = min (numUm, numDois)


print("Média: {}".format(media))
print("Soma: {}".format(soma))
print("Produto: {}".format(produto))


if numUm == numDois:
    print ("Os números são iguais!")
else:
    print("Maior Valor: {}".format(maior))
    print("Menor Valor: {}".format(menor))




