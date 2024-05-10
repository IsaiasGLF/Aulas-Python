import os
os.system("cls || clear")

#for i in range (1, 6): #deve-se sempre começar com 0, pois se começar com 1 no 6 ele para (ou seja, só irá contar 5x) c = 1 ou só colocar um +1
#for i in range (6, 0, -1): #caso queira contar de trás pra frente   
#for i in range (1, 6, 2): #vai contar de 2 em 2
#print(i)

i = int(input('inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for d in range (i, f+1, p):
    print (d)


