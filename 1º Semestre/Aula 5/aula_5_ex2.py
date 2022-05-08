salario = float(input("Digite seu sálario: "))

if salario > 1250:
    novo_salario = (salario*10)/100
    total1 = salario + novo_salario
    print(f"O salário total é de {total1}")


else:
    novo_salario2 = (salario*15)/100
    total2 = salario + novo_salario2
    print(f"O seu sálario atual é {total2}")
    