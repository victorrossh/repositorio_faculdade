idade = int(input("Digite sua idade: "))

if idade <= 10:
    print("O valor pago será de R$30.00.")

elif idade > 10 and idade <=29:
    print("O valor pago será de R$60.00.")
        
elif idade > 29 and idade <= 45:
    print("O valor pago será de R$120.00. ")
    
elif idade > 45 and idade <= 59:
    print("O valor pago será de R$150.00.")

else:
    print("O valor pago será de R$300.00. ")