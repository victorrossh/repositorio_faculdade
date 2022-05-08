from Aula_4 import converte_para_celsius, converte_para_fahrenheit

try:
    resultado = converte_para_celsius(0)
    assert resultado == 32
    print("Teste concluido")
except AssertionError:
    print("Teste errado")

try:
    resultado = converte_para_celsius(27)
    assert resultado == 80.6
    print("Teste concluído")
except AssertionError:
    print("Teste errado")
try: 
    resultado = converte_para_fahrenheit(32)
    assert resultado == 0
    print("Teste concluído")
except AssertionError:
    print("Teste errado")

try:
    converte_para_fahrenheit(41)
    assert resultado == 5.0
    print("Teste concluído")
except AssertionError:
    print("Teste errado")