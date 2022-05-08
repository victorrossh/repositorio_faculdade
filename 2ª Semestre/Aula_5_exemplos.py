'''
Classe Cachorro
- Atributos: nome, idade
- Métodos: andar, comer, latir
'''


class Cachorro:
    # atributos
    def __init__(self, nome, idade):
        self.nome = nome                       # responsável pela criação de um novo objeto e definir os atributos.
        self.idade = idade


    # metodos
    def andar(self, distancia):
        print(f"O cachorro andou {distancia} metrôs.")
    
    def comer(self):
        print(f"O cachorro de nome {self.nome} comeu")
    
    def latir(self):
        print("Au Au..,")


dog = Cachorro("Spike", 2)
print(dog.nome, dog.idade)
dog.nome = "Spike"
dog.idade = 2
print(f"O cachorro de nome {dog.nome} possui {dog.idade} anos de idade. ")
dog.andar(2)
dog.latir()           # dog é o objeto da classe cachorro
dog.comer()

meu_cachorro = Cachorro("Amora", 1) # substanciado pela classe "SEMPRE"
print(meu_cachorro.idade)  
meu_cachorro.nome = "Amora"
meu_cachorro.idade = 1
print(f"O cachorro de nome {meu_cachorro.nome} possui {meu_cachorro.idade} ano de idade. ")
meu_cachorro.andar(5)                                                      # sempre que eu quiser botar parâmetros eu coloco do lado do self, e acrescendo no atributo o valor.
meu_cachorro.latir()
meu_cachorro.comer()