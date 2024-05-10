a = int(input("Digite o primeiro número: "))
opcao = (input("Digite a operação desejada: "))
b = int(input("Digite o 2º número: 6"))

match (opcao):
   case "+": 
    resultado = a + b
   case "-":
    resultado = a - b
   case "*":
    resultado = a * b
   case "/":
    resultado = a / b

print (f"Resultado: {resultado}.")

    
