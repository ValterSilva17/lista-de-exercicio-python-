num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = float(input("Digite um número real: "))


resultado_a = (num1 * 2) * (num2 / 2)

resultado_b = (num1 * 3) + num3

resultado_c = num3 ** 3

print(f"A O produto do dobro de {num1} com a metade de {num2} é: {resultado_a}")

print(f"B A soma do triplo de {num1} com {num3} é: {resultado_b}")

print(f"C O número {num3} elevado ao cubo é: {resultado_c:.2f}")