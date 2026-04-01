area = float(input("Digite o tamanho da área a ser pintada "))

litros_necessarios = (area / 6) * 1.1

latas_sozinhos = litros_necessarios // 18

if litros_necessarios % 18 > 0:
    latas_sozinhos += 1
preco_latas = latas_sozinhos * 80

galoes_sozinhos = litros_necessarios // 3.6
if litros_necessarios % 3.6 > 0:
    galoes_sozinhos += 1
preco_galoes = galoes_sozinhos * 25

latas_mistura = int(litros_necessarios // 18)

resto_litros = litros_necessarios % 18

galoes_mistura = resto_litros // 3.6
if resto_litros % 3.6 > 0:
    galoes_mistura += 1

preco_mistura = (latas_mistura * 80) + (galoes_mistura * 25)

print("Litros totais (com 10% de folga): ", litros_necessarios)

print(f"Opção 1 (Só latas 18L): {int(latas_sozinhos)} latas - R$ {preco_latas:.2f}")
print(f"Opção 2 (Só galões 3,6L): {int(galoes_sozinhos)} galões - R$ {preco_galoes:.2f}")
print(f"Opção 3 (Melhor Mistura): {latas_mistura} latas e {int(galoes_mistura)} galões - R$ {preco_mistura:.2f}")
