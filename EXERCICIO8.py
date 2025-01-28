nomes = []

for i in range(5):
    nome = input("Digite o nome: ")
    nomes.append(nome)

cont = 0

for nome in nomes:
    if nome[0] == 'A':
        cont += 1

print("A quantidade de nomes que começam com a letra 'A' é: ", cont)
