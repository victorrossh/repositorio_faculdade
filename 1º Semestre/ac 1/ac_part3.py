pães = int(input("Digite a quantidade de pães: "))

broa = int(input("Digite a quantidade de broa: "))


conta1 = 0.12*pães

conta2 = 1.50*broa

valor_total = conta1 + conta2

poupança = conta1 + conta2/10



print(f"O valor da poupança é {poupança} ")

print (f"O valor da conta será de {valor_total}")