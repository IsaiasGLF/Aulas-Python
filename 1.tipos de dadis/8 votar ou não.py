import os
os.system("cls || clear")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade < 18 or idade > 65:
    print("Voto não obrigatório")

else:
    print ("Voto obrigatório")    