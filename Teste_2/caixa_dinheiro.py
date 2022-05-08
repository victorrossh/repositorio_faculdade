valor = int(input("Digite o valor desejável para sacar: "))
totced = 0
total = valor
ced = 200

while True:
    if total >=ced:
        total -=ced
        totced +=1
    else:
        print(f"Total de {totced} cédulas de R${ced}.")
        if ced ==200:
            ced = 100
        elif ced == 100:
                ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 10:
            ced =5
        elif ced ==5:
            ced = 2
        
        totced = 0
        if total==0:
            break  