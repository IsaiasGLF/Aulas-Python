soma = 0
for i in range (4): 
    numero = int(input(f"Digite a {i+1}ª nota: "))
    
    soma+=numero
    media = soma / 4

print ("Sua média é: ", media)