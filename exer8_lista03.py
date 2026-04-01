
frase = input("Digite uma frase ou palavra: ")

texto_limpo = frase.replace(" ", "").lower()

texto_invertido = texto_limpo[::-1]


if texto_limpo == texto_invertido:
    print(f"'{frase}' é um PALÍNDROMO!")
else:
    print(f"'{frase}' NÃO é um palíndromo.")
