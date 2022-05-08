altura = float(input("Digite sua altura: "))
sexo = str(input("Masculino ou Feminino ?:  "))

if (sexo=="masculino"):
    contam= (round(72.7*altura)- 58)
    print(f"O seu peso é de {contam} quilos.")

else:
    contaf = (round(62.1*altura) -44.7)
    print(f"O seu peso é de {contaf}")
    
