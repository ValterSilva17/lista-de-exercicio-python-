import re

cpf_input = input("Digite o CPF (xxx.xxx.xxx-xx): ")
cpf = re.sub(r'\D', '', cpf_input) 

if len(cpf) != 11 or cpf == cpf[0] * 11:
    print("CPF Inválido (Formato incorreto ou números repetidos).")
else:
    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1
    
    resto = (soma * 10) % 11
    digito_1 = resto if resto < 10 else 0

    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1
        
    resto = (soma * 10) % 11
    digito_2 = resto if resto < 10 else 0

    if int(cpf[9]) == digito_1 and int(cpf[10]) == digito_2:
        print(f"O CPF {cpf_input} é VÁLIDO!")
    else:
        print(f"O CPF {cpf_input} é INVÁLIDO!")