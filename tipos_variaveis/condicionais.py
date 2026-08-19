# if, elif e else


#Exemplo de "if"
idade = int(input("Quantos anos voce tem?"))
print("Exemplo de comando if")
if idade >= 18:
    print("Voce é maior de idade.")
elif idade >= 12:
    print("Voce é um adolescente")
else:
    print("Voce é menor de idade")

mensagem = "Pode tirar a carteira de habilitaçao" if idade >= 18 else "Voce nao pode tirar a carteira de habilitaçao"
print(mensagem)