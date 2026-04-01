frase = input("Digite uma frase: ").lower()

espacos = 0
vogais = 0
lista_vogais = "aeiouáéíóúâêîôûãõ" 

for letra in frase:
    if letra == " ":
        espacos += 1
    elif letra in lista_vogais:
        vogais += 1

print(f"Frase analisada: {frase}")
print(f"Quantidade de espaços: {espacos}")
print(f"Quantidade de vogais: {vogais}")
