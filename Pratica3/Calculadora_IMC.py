"""
Calculadora de IMC


Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso" 

< 25: classificacao = "Peso normal"

 < 30: classificacao = "Sobrepeso"

 Para os demais cenários: classificacao = "Obeso"
"""
# Inserir os dados
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

#Calculo do IMC
IMC = peso / (altura ** 2)

print(f"IMC = {IMC:.2f}kg/m2")

#Condicional
if IMC <= 18.5:
    classificacao = "Abaixo do peso"
elif IMC <= 25:
    classificacao = "Peso Normal"
elif IMC <= 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"    

print(f"Seu IMC é {IMC:.1f}")
print(f"Classificação: {classificacao}")
