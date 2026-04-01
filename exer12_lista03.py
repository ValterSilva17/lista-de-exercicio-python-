telefone = input("Digite o telefone (7 ou 8 dígitos): ").replace("-", "").strip()

if len(telefone) == 7:
    print("Telefone possui 7 dígitos. Vou adicionar o dígito 3 na frente.")
    telefone_ajustado = "3" + telefone
elif len(telefone) == 8:
    print("Telefone possui 8 dígitos. Está correto.")
    telefone_ajustado = telefone
else:
    telefone_ajustado = None
    print("Erro: O telefone deve ter 7 ou 8 dígitos.")

if telefone_ajustado:
    parte1 = telefone_ajustado[:4]
    parte2 = telefone_ajustado[4:]
    print(f"Telefone corrigido: {parte1}-{parte2}")