"""
Crie um programa que gera uma senha aleatória com o módulo random,
utilizando caracteres especiais, possibilitando o usuário a informar
a quantidade de caracteres dessa senha aleatória.
"""
import random
import string

def gerar_senhas(tamanho):
    caracteres = string.ascii_letters
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
nova_senha = gerar_senhas(tamanho_senha)

print(f"Nova senha gerada: {nova_senha}")