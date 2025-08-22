"""
Conversor de Temperatura 

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

#Inserir os dados
temperatura = float(input("Digite a temperatura: "))

origem = input("Digite a unidade de origem (Ex:C, F, K): ").upper()
destino = input("Digite a unidade de destino (Ex:C, F, K): ").upper()

if origem == destino: #Se origem for iguais, mantem a temperatura
    resultado = temperatura
elif origem == "C": #Se origem for C, converter para F ou K
    if destino == "F":
        resultado = (temperatura * 1.8) + 32
    else:
        resultado = temperatura + 273.15
elif origem == "F":   # Se origem for F, converter para C ou K
    if destino == "C":
        resultado = (temperatura - 32) / 1.8
    else:
        resultado = (temperatura - 32) * 5/9 + 273
else: #Se origem for K, converter para C ou F
    if destino == "C":
        resultado = temperatura - 273
    else:
        resultado = (temperatura - 173) * 1.8 + 32

print(f"{temperatura}{origem} é igual a {resultado:.2f}{destino}")
