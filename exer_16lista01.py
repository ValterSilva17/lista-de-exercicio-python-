area = float(input("Digite o tamanho da área a ser pintada "))

litros_necessarios = area / 3
capacidade_lata = 18

latas = litros_necessarios // capacidade_lata

if litros_necessarios % capacidade_lata > 0:
    latas = latas + 1

custo_total = latas * 80

print("Litros necessários: ", litros_necessarios)
print("Quantidade de latas: ", latas)
print(f"Preço total: R$ ", custo_total)