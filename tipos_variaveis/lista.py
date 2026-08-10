#Declaracao

minha_lista = [1,2,3,4,6,"Matheus",True, False]

print("Minha lista de exemplo", minha_lista)
minha_lista[0] = "Python"
print("minha _lista[0]: ",minha_lista[0])
print(minha_lista[0:4])

#Metodo append(): Adiciona um elemento ao final da lista
minha_lista.append(6)
print("Apos append(6):", minha_lista)

#Metodo index
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)

#Metodo insert: Insere um elemento em um indice especifico
minha_lista.insert(2,10)
print("Apos o insert(2,10):", minha_lista)

#Metodo pop
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print('Apos pop(3): ', minha_lista)


minha_lista.remove(True)
print("Apos remove(True):", minha_lista)

#so organiza listas com numeros inteiros
minha_lista.sort()
print("Apos sort:", minha_lista)