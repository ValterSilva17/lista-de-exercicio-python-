data = input("Digite uma data (dd/mm/aaaa): ")

dia, mes, ano = data.split('/')

meses = [
    "", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

mes_extenso = meses[int(mes)]

print(f"Data por extenso: {dia} de {mes_extenso} de {ano}")