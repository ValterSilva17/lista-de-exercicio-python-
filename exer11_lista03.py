import random

palavras = ["python", "programacao", "computador", "teclado", "algoritmo", "github"]
palavra_secreta = random.choice(palavras).upper()
letras_descobertas = ["_" for letra in palavra_secreta]
tentativas = 6
letras_digitadas = []

print("=== JOGO DA FORCA ===")


while tentativas > 0 and "_" in letras_descobertas:
    print(f"\nPalavra: {' '.join(letras_descobertas)}")
    print(f"Tentativas restantes: {tentativas}")
    print(f"Letras já testadas: {', '.join(letras_digitadas)}")
    
    chute = input("Digite uma letra: ").upper()

    if chute in letras_digitadas:
        print("Você já tentou essa letra!")
        continue
    
    letras_digitadas.append(chute)

    if chute in palavra_secreta:
        print(f"Boa! A letra {chute} existe na palavra.")
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == chute:
                letras_descobertas[i] = chute
    else:
        tentativas -= 1
        print(f"Que pena! A letra {chute} não existe.")

if "_" not in letras_descobertas:
    print(f"\nPARABÉNS! Você venceu! A palavra era: {palavra_secreta}")
else:
    print(f"\nGAME OVER! Você foi enforcado. A palavra era: {palavra_secreta}")