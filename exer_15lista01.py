salario_bruto = float(input("Digite o valor total do seu salario "))

ir = salario_bruto * 0.11        # 11% de Imposto de Renda
inss = salario_bruto * 0.08      # 8% de INSS
sindicato = salario_bruto * 0.05  # 5% de Sindicato

total_des = ir + inss + sindicato
salario_liquido = salario_bruto - total_des

print("+ Salário Bruto : R$", salario_bruto)
print("- IR (11%)      : R$", ir)
print("- INSS (8%)     : R$", inss)
print("- Sindicato (5%): R$", sindicato)
print("= Salário Líquido : R$", salario_liquido)
