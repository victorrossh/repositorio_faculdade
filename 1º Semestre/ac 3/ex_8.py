salario = float(input("Digite o sálario: "))
hora_trabalhada = int(input("Digite a hora trabalhada: "))


if hora_trabalhada <=160:
    total = salario*hora_trabalhada
    print(total)

else:
    acrescimo = 50*salario/100
    salario_total = salario + acrescimo
    print(f"O sálario total é de R${salario_total}")