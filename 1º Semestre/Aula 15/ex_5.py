def area_triangulo (base,altura):
    area = (base*altura)/2
    return(f"A área do quadrado é {area} metrôs quadrados: ")


base = float(input("Informe o valor da base: "))
altura = float(input("Informe o valor da altura: "))
print(area_triangulo(base,altura))
