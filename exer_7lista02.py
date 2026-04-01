valor1 = int(input("Digite um numero "))
valor2 = int(input("Digite outro numero "))
valor3 = int(input("Digite outro numero "))

maior = valor1
if valor1 > maior:
    maior = valor2
if valor3 > maior:
    maior = valor3

menor = valor1
if valor2 < menor:
    menor = valor2
if valor3 < menor:
    menor = valor3

print("O maior numero é", maior)
print("O menor numero é", menor)