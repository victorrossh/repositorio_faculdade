print("Informe o turno que você estuda: ")
letivo = input("M = matutino , V= vespertino, N= noturno ")

if letivo == "M":
    print("Bom Dia")

elif letivo == "V":
    print("Boa Tarde")

elif letivo == "N":
    print("Boa Noite")

else:
    print("Valor Inválido")