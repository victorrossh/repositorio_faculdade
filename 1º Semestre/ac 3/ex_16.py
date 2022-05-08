idade = int(input("Digite a sua idade: "))
ano_serviço = int(input("Digite o ano que vc entrou na empresa: "))

tempo_serviço = 2021 - ano_serviço


if idade >=65 and tempo_serviço >=30:
    print("Requer aposentadoria")
elif idade >=60 and tempo_serviço >=25:
    print("Requer aposentadoria")

else:
    print("Não requer aposentadoria.")