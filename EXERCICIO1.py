preco = float(input("Digite o preço do produto: R$"))
desconto = float(input("Digite a porcentagem de desconto: "))

valor_desconto = preco*(desconto/100)
preco_final = preco-valor_desconto

print("Valor do desconto: R$", valor_desconto)
print("Preço final do produto: R$", preco_final)
