pequena = int(input("Digite a quantidade de camisetas pequenas: "))
media = int(input("Digite a quantidade de camisetas médias: "))
grande = int(input("Digite a quantidade de camisetas grandes: "))


valor_pequena = 10*pequena
valor_media = 12*media
valor_grande = 15*grande

valor_total = valor_pequena + valor_media + valor_grande

print(f"O valor total será de {valor_total}")