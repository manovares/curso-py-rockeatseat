# Criando um dicionario de exemplo
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

print("Meu dicionario: ", pessoa)

print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Silva"
print("Sobrenome:", pessoa["sobrenome"])
print("Meu dicionario: ", pessoa)


pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])

# Removendo um par chave p valor
del pessoa["sobrenome"]

print("Meu dicionario de exemplo: ", pessoa)

#Metodos: keys(), values(), items()

chaves = list(pessoa.keys())
print("Chaves do dicionario: ", chaves)
print("Primeira chave:", chaves[0])


valores = list(pessoa.values())
print("Valores do dicionarios:", valores)
print("Primeiro valor do dicionario:", valores[0])

itens = list(pessoa.items())
print("Pares chave-valor do dicionario:", itens)
print("Primeiro valor:", itens[0][1])
