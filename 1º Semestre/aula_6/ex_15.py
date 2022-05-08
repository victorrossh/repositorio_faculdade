primeiro = int(input("Primeiro número: "))
segundo = int(input("Segundo número: "))
terceiro= int(input("Terceiro número: "))

print(primeiro, segundo,terceiro)

if (terceiro > segundo):
    aux = terceiro
    terceiro = segundo
    segundo = aux
if (segundo > primeiro):
    aux = segundo
    segundo = primeiro
    primeiro = aux
if (terceiro > segundo):
    aux = terceiro
    terceiro = segundo
    segundo = aux

print(terceiro,segundo,primeiro)