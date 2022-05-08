custo_fabricacao = float(input("Digite o valor do veículo: "))

distribuidor = custo_fabricacao*28/100
imposto = custo_fabricacao*45/100

distribuidor_imposto = imposto+distribuidor

custo_consumidor = custo_fabricacao + distribuidor_imposto

print(f"O valor do veículo para o consumidor será de {custo_consumidor}.")