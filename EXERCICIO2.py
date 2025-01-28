frase = input("Digite uma frase: ")

quantidade_vogais = 0

for letra in frase:
   if letra in "aeiou" or letra in "AEIOU":
       quantidade_vogais +=1
print("A frase contém: ", quantidade_vogais)

