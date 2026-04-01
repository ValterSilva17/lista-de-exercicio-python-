letra = input("Digite uma letra: ")


if letra in 'aeiou' or 'AEIOU':
    print(f"A letra '{letra}' é uma VOGAL")

else:
    print(f"A letra '{letra}' é uma CONSOANTE")