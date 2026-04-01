tamanho = float(input("Tamanho do arquivo (MB): "))
velocidade = float(input("Velocidade do link de Internet "))

velocidade_megabytes = velocidade / 8

tempo_segundos = tamanho / velocidade

tempo_minutos = tempo_segundos / 60

print("Velocidade real de download: ", velocidade, "MB/s")
print("Tempo total aproximado ", tempo_segundos, "segundos")
print("Ou aproximadamente ", tempo_minutos, "minutos")
