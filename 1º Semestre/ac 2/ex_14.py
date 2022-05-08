valor_hora = float(input("Digite o valor da hora: "))
hora_trabalhada = float(input("Digite a hora trabalhada: "))
salariobruto = valor_hora * hora_trabalhada
fgts = (salariobruto*11)/100
sind = (salariobruto*3)/100
cinco = (salariobruto*5)/100
dez = (salariobruto*10)/100
vinte = (salariobruto*20)/100



if salariobruto <=900:
    liquido = (salariobruto - sind)

elif salariobruto >= 900 and salariobruto <= 1500:
    liquido = (salariobruto - sind)- cinco

elif salariobruto >=1500 and salariobruto <= 2500:
    liquido = (salariobruto - sind) - dez

else:
    liquido(salariobruto - sind) - vinte

    print(f"Seu salário bruto é de {salariobruto}")
    print(f"O valor do seu FGTS é de {fgts}")
    print(f"O sindicato vai obter do seu sálario R${sind} .")
    print(f"O seu sálario líquido é de R${liquido}")