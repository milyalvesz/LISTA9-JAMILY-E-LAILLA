valor_real = float(input("Digite o valor em reais (R$): "))
cotacao_dolar = float(input("Digite a cotação do dólar (em R$): "))

valor_dolar = valor_real/cotacao_dolar

print("Você pode comprar US$", valor_dolar)