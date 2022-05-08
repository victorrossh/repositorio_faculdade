salario_fixo = float(input("Digite o valor do salário: "))

if salario_fixo <1500:
    acrescimo = salario_fixo*3/100
    total = salario_fixo + acrescimo
    print(total)
else:
    acrescimo2 = salario_fixo*5/100
    total2 = salario_fixo + acrescimo2
    print(total2)
