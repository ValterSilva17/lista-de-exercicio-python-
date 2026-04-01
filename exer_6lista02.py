valor1 = int(input("Digite um numero "))
valor2 = int(input("Digite outro numero "))
valor3 = int(input("Digite outro numero "))

if valor1 > valor2 and valor1 > valor3: 
    print("O numero maior é ", valor1)
elif valor2 > valor1 and valor2 > valor3:
    print("O numero maior é", valor2)
else:
    print("O numero maior é", valor3)
    