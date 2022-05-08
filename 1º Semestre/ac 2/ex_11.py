valor = float(input("Digite o valor do produto: "))
forma_pagamento = int(input("Digite a forma de pagamento"))

if forma_pagamento == 1:
    desconto = (valor*10)/100
    valor_total = valor - desconto
    print(f"O valor pago será de {valor_total}")

elif forma_pagamento == 2:
    desconto2 = (valor*15)/100
    valor_total2 = valor - desconto2
    print(f"O valor pago será de {valor_total2}")
    
elif forma_pagamento == 3:
    parcelamento = valor/2
    print(f"O valor pago será de {parcelamento}")

else:
    valor = valor + ((valor*10)/100)
    print(f"O valor pago será de {valor}")