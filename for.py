print("For utlizando lista")
lista = [1,2,3,4,5]
for elemento in lista:
    print(elemento)

print("For utlizando tupla")
tupla = (1,2,3,4,5)
for elemento in tupla:
    print(elemento)

print("For utilizando dicionario - chaves")
pessoa = {"nome": "João", "idade": 18, "Cidade": "São Paulo"}
for chave in pessoa.keys():
    print(chave)

print("For utilizando dicionario - valores")
for valor in pessoa.values():
    print(valor)


for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

#range
print("\n Utilizando a função range()")
for numero in range(5):
    print("Numero:", numero)

print("\n Utilizando a função range() com len()")
lista = [1,2,3,4,5]
print(lista)
for indice in range(0, len(lista)):
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 0
print(lista)

#enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Indice 1")