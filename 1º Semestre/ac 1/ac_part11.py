salario = float(input("Digite o sálario: "))

aumento = (15*salario)/100

aumento_salario = salario + aumento

imposto = (8*aumento_salario)/100

salario_final = (aumento + salario) - imposto

print (f"O seu pagamento era de {salario}, o sálario com aumento é de {aumento_salario} e o sálario final é de {salario_final} ")
