def épar(x):
    return (x%2==0)

def par_ou_impar(x):
    if x%2==0:
        return "Par"
    else:
        return "ímpar"

n1 = int(input("Digite um valor para saber se é par ou ímpar: "))
print(par_ou_impar(n1))
