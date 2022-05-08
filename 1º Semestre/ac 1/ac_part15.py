hora_trabalhada = float(input("Digite a quantidade de horas trabalhada: "))
hora_extra = float(input("Digite a quantidade de hora extra: "))

calculo_hora = 50*hora_trabalhada

calculo_extra = 75*hora_extra 

salario_bruto = calculo_hora + calculo_extra

salario_liquido = salario_bruto-(10*salario_bruto)/100 



print(f"O sálario bruto desse funcionário será de {salario_bruto} e o líquido com os descontos será de {salario_liquido}")