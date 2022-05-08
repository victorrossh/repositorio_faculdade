a = int(input("Coeficiente a: "))

if (a==0):
    print("Não é uma equação de segundo grau.")

else: 
    b = int(input("Coeficiente b: "))
    c =int(input("Coeficiente c: "))
    delta = b**2 - (4*a*c)

if (delta<0):
    print("A equação não possui raízes reais.")

elif (delta==0):
    raiz = -b/2*a

else:
    raiz1 = (-b + (delta)**(0.5))/(2*a)
    raiz2 = (+b + (delta)**(0.5))/(2*a)
    print("A equação possui duas raízes")
    print("A equação possui duas raizas reais.")
    print(f"Raizes {raiz1:.3f} e {raiz1:.3f}")


