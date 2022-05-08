gasolina = float(input("Digite o valor da Gasolina: "))
etanol = (input("Digite o valor do etanol: "))

valor_pago = float(input("Digite o valor pago: "))

total1 = valor_pago/gasolina 

total2 = valor_pago/etanol

escolha = ""

if (total1 > total2):   
    escolha = "É mais vantajoso abastecer com gasolina"

elif (total1 < total2):
    escolha = "É mais vantajoso abastecer com etanol"

print(f"Você abasteceu {total1} litros de gasolina.{escolha}")
