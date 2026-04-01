import random

palavras = ["PYTHON", "ALGORITMO", "NOTEBOOK", "TECLADO", "CELULAR", "DESENVOLVEDOR"]
palavra_original = random.choice(palavras)

letras = list(palavra_original)
random.shuffle(letras)

palavra_baralhada = "".join(letras)

print("=== JOGO DO EMBARALHAMENTO ===")
print(f"Descubra a palavra: {palavra_baralhada}")

tentativas = 3
while tentativas > 0:
    chute = input(f"\nSua resposta ({tentativas} tentativas restantes): ").upper()
    
    if chute == palavra_original:
        print("🎉 PARABÉNS! Você acertou!")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print("Errado! Tente novamente.")
        else:
            print(f"Acabaram as chances! A palavra era: {palavra_original}")