he = int(input("Informe a hora de entrada:  "))
me = int(input("Informe os minutos de entrada:  "))
hs = int(input("Informe a hora de saída:  "))
ms = int(input("Informe os minutos de saida:  "))
ht = hs - he
mt = ms - me

if ht == 1:
    valor_pago = 4
    if mt > 0:
        valor_pago += 2
elif ht == 2:
    valor_pago = 6
    if mt > 0:  
        valor_pago += 1
else:
    valor_pago = 6
    ht = ht - 2
    valor_pago = valor_pago + ht
    if mt > 0:
        valor_pago += 1
print(f"valor a pagar é de R${valor_pago},00")