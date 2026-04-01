
tabela_leet = {
    'A': '4',
    'E': '3',
    'I': '1',
    'O': '0',
    'T': '7',
    'S': '5',
    'B': '8',
    'G': '6'
}

texto_original = input("Digite o texto para converter em Leet: ").upper()
texto_leet = texto_original

for letra, numero in tabela_leet.items():
    texto_leet = texto_leet.replace(letra, numero)

print(f"Original: {texto_original}")
print(f"Leet 1337: {texto_leet}")
