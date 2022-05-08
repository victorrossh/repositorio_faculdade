while True:
    try:
        a = int(input("Digite um número: "))
        b = int(input("Digite um número: "))
        c = a / b
        print(c)
    except ZeroDivisionError:
        print("Divisão por zero.")
    except ValueError:
        print("O valor informado não é inteiro.")
    except Exception:
        print("Erro inesperado.")
    else:
        print(" Operação realizada com sucesso. ")
    break
