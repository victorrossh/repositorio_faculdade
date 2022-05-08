salario = float(input("Digite o seu sálario: "))
valor_casa = float(input("Digite o valor da casa : "))
anos_pagar = int(input("Digite o tempo de pagamento: "))

meses = anos_pagar*12

parcelas = valor_casa/meses

minino = (salario*30)/100

if parcelas < minino:
    print ("Empréstimo bancario aprovado")

else:
    print ("Empréstimo bancario não aprovado")