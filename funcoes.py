def saudacao(nome):
    print(f"Ola, {nome}")

print("\n Chamando a função saudacao:")
saudacao("Alice")
saudacao("Bob")


def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\n chamando função quadrado")
resultado_quadrado = quadrado(5)
print("Resultado da funcao quadrado: ", resultado_quadrado)

def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\n Chamando a função soma:")
resultado_soma = soma(20,50)
print("A soma do numero 20 e numero 50 é", resultado_soma)