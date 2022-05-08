def area_quadrado (n1):
    area = n1**2
    return(f"A área do quadrado é {area:.2f} metrôs quadrados: ")


n1 = float(input("Informe um lado do quadrado: "))
print(area_quadrado(n1))
