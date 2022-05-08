'''
IDADE a partir DE 15 ANOS.
'''
idade = int(input("Digite sua idade: "))
if idade <=15:
    print("Idade não permitida. Somente idades a partir de 15 anos.")
else:
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))
    imc = peso/(altura**2)


    if imc <= 17:
        imc = peso/(altura**2)
        print("Muito abaixo")

    elif imc >= 17 and imc <=18.49:
        print("Abaixo do peso")

    elif imc >= 18.5 and imc <= 24.99:
        print("Peso Normal")

    elif imc >=25 and imc <= 29.99:
        print("Acima do peso")

    elif imc >=30 and imc <=34.99:
        print("Obesidade 1") 

    elif imc >=35 and imc <= 39.99:
        print("Obesidade 2 (Severa)") 

    else:
        print("Obesidade 3 (Mórbida)")  
  


