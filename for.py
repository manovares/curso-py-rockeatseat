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