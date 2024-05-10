numero_par = 0

numero_impar = 0


for i in range (5): 
    numero = int(input(f"Digite o {i+1}º número: "))
    if i % 2 == 0:
        numero_par += 1

    else:
        numero_impar += 1


print (f"Quantidade de Números pares: {numero_par}");
print (f"Quantidade de Números impares: {numero_impar}");