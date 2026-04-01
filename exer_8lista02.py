valor1 = float(input("Digite um valor "))
valor2 = float(input("Digite outro valor "))
valor3 = float(input("Digite outro valor "))

if valor1 < valor2 and valor1 < valor3:
    print("Pode comprrar está com otimo preço", valor1)
elif valor2 < valor1 and valor2 < valor3:
    print("Pode comprrar está com otimo preço", valor2)
else:
    print("Pode comprar está com otimo preço", "essa compra = ", valor3)