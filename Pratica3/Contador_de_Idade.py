"""
Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

Criança (0-12 anos),

Adolescente (13-17 anos),

Adulto (18-59 anos)

Idoso (60 anos ou mais)
"""

# Colocar a idade
idade = int(input("Digite sua idade: "))

#Condição
if idade <= 12:
    print("Você é Criança")
elif idade <= 17:
    print("Você é adolescente")
elif idade <= 59:
    print("Você é adulto")
else:
    print("Voce é idoso")