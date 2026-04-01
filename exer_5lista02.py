nota1 = float(input("Digite a primeira nota "))
nota2 = float(input("Digite a segunda nota "))

media = (nota1 + nota2) / 2 

if media >= 7:
    print("Você foi 'Aprovado' ")
elif media < 7:
    print("Você foi 'Reprovado'")
if media == 10:
    print("Parabéns, você foi Aprovado com Distinção ")

print("Sua media ", media)