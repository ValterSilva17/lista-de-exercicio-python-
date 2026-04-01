peso = float(input("Digite o peso total de peixes em kilos "))

limite = 50.0
valor_mult = 4.0

if peso > limite:
    excesso = peso - limite
    multa = excesso * valor_mult
else:
    excesso = 0
    multa = 0

if excesso > 0:
    print("EXCESSO DETECTADO: ", excesso)
    print("VALOR DA MULTA: ",multa)
else:
    print("PESO DENTRO DO LIMITE. Não há multa a pagar.")