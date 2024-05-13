soma = 0
for i in range (3): 
    numero = int(input(f"Digite a {i+1}ª nota: "))
    
    soma+=numero
    media = soma / 4


print ("Sua média é: ", media)

if media >= 7:
     print ("Aluno Aprovado")

if media <= 4:
     print ("Aluno Reprovado")