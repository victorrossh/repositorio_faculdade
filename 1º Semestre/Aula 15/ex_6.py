def area_triangulo(base,altura):
    area = (base*altura)/2
    return (f"O valor da área é de {area:.2f} metrôs quadrados. ")


base = float(input("Informe o valor da base: "))
altura = float(input("Informe o valor da altura: "))
print(area_triangulo(base, altura))

def area_quadrado(lado):
    areaq = lado**2
    return(f"A área do quadrado é {areaq:.2f} metrôs quadrados.")

lado = float(input("Digite o valor do lado: "))
print(area_quadrado(lado))


def area_circulo(raio):
    areac = 3.14*(raio)**2
    return(f"A area do círculo é de {areac:.2f}")

raio = float(input("Informe o valor do raio: "))
print(area_circulo(raio))



def area_losango(dm ,dn):
    areal = (dm * dn)/2
    return (f"A área do losango é {areal:.2f} metrôs quadrados.")

dm = float(input("Informe a diagonal maior: "))
dn = float(input("Informe a diagonal menor: "))
print(area_losango(dm, dn))

def area_retangulo (base,altura):
    arear= base*altura
    return (f"A área do retângulo é de {arear:.2f}")

base = float(input("Informe o valor da base: "))
altura = float(input("Informe o valor da altura: "))
print(area_retangulo(base, altura))
