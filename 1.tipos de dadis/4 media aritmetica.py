import os
os.system("cls || clear")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

notaUm = int(input("Digite a 1ª nota: "))
notaDois = int(input("Digite a 2ª nota: "))

media = (notaUm + notaDois) / 2

os.system("cls || clear")

print ("Nome: {}\nIdade: {}\n1ª Nota: {}\n2ª Nota: {}\nMédia: {}".format(nome, idade, notaUm, notaDois, media))
