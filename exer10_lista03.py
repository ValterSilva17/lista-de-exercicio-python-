
unidades = ["", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove"]
especiais = ["Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove"]
dezenas = ["", "", "Vinte", "Trinta", "Quarenta", "Cinquenta", "Sessenta", "Setenta", "Oitenta", "Noventa"]

num = int(input("Digite um número entre 0 e 99: "))

if num == 0:
    resultado = "Zero"
elif num < 10:
    resultado = unidades[num]
elif num < 20:
    resultado = especiais[num - 10]
else:
    d = num // 10  
    u = num % 10   
    
    if u == 0:
        resultado = dezenas[d]
    else:
        resultado = f"{dezenas[d]} e {unidades[u]}"

print(f"Por extenso: {resultado}")