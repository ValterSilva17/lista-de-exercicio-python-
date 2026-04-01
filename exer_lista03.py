string1 = input("Digite a primeira frase: ")
string2 = input("Digite a segunda frase: ")

print(f"\nString 1: '{string1}' - Tamanho: {len(string1)} caracteres")
print(f"String 2: '{string2}' - Tamanho: {len(string2)} caracteres")


if len(string1) == len(string2):
    print("As duas strings possuem o mesmo tamanho.")
else:
    print("As duas strings possuem tamanhos diferentes.")

if string1 == string2:
    print("As duas strings possuem o mesmo conteúdo.")
else:
    print("As duas strings possuem conteúdo diferente.")