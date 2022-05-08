qntd_temperatura= float(input("Digite a quantidade de temperaturas para análise: "))
maior = -999999999999
menor = 999999999999
n= qntd_temperatura
t=0
while qntd_temperatura >0:
    temp = float(input("Digite a temperatura do local: "))
    
    if temp > maior:
        maior = temp 
    if temp < menor: 
        menor = temp
    
    t += temp #acumulador
    media = t /n
    qntd_temperatura -= 1

    print (f"A maior qntd_temperatura é de {maior:.2f} e a menor é de {menor:.2f} e a média é de {media:.2f}")



