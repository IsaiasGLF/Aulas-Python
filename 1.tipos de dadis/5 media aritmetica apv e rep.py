import os
os.system("cls || clear")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

notaUm = int(input("Digite a 1ª nota: "))
notaDois = int(input("Digite a 2ª nota: "))
notaTres = int(input("Digite a 3ª nota: "))

media = (notaUm + notaDois + notaTres) / 3

os.system("cls || clear")

print ("Nome: {}\nIdade: {}\n1ª Nota: {}\n2ª Nota: {}\nMédia: {}".format(nome, idade, notaUm, notaDois, media))

if media >= 7:
    print("Aluno aprovado")

if media <= 6.9 or media == 5:
    print("Aluno em recuperação")

if media <5:
    print("Aluno reprovado")