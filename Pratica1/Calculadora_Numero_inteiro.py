"""
Calculadora de Número Inteiro
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
Entrada: O arquivo de entrada contém 4 valores inteiros. 
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.
"""

#Para inserir os valores inteiros
A = int(input())
B = int(input())
C = int(input())
D = int(input())

#Calcular a diferença
DIFERENCA = (A * B - C * D)

#Mostrar o resultado
print("Diferenca =", DIFERENCA)