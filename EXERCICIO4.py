import random
def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)

    print("Bem-vindo ao jogo de Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    tentativas = 0

    while True:

        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print("Parabéns! Você acertou o número. \n" "Seu número foi: ")

jogo_adivinhacao()
