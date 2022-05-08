n = input("digite um nome: ")
lista = ['victor', 'Hertz', 'Fabiana', 'Vitor'] 
if n in lista:
   print ('o nome está na lista')
else:
  print ("o nome não está na lista")
x = lista.index('victor')
print("victor está na posição %d da lista: " %x)
lista[0] = 'josé'
print(lista)    

