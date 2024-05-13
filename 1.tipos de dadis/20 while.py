import os
os.system("cls || clear")

soma: float = 0
for i in range (3): 
   while True :
    nota = float(input("Digite uma nota: "))
    if nota < 0 or nota > 10:
        print ("Nota inválida...\n")
    else:
        soma += nota
        break

media = soma / 3

print (f"Média: {media}")

if nota >= 7:
    print ("Aprovado")

elif nota < 6.9 or nota == 5:
    print ("Recuperação")    

elif nota < 5:
    print ("Reprovado")    