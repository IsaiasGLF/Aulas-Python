nome_produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))
preco_unitario = float(input("Digite o preço unitário do produto: "))

total = quantidade * preco_unitario

if quantidade <= 5:
    desconto = total * 0.02
elif quantidade <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05

total_a_pagar = total - desconto

print("Total: R$", total)
print("Desconto: R$", desconto)
print("Total a pagar: R$", total_a_pagar)
