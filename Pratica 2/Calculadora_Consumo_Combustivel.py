"""
Calculadora de Consumo de Combustível

Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

Distância percorrida: 300 km
Combustível gasto: 25 litros 
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais
"""

#Dados da viagem
distancia = 300
combustivel = 25

#Calculo do consumo
consumo = distancia / combustivel

#Exibição do resultado
print("Dados da Viagem")
print(f"Distancia percorrida: {distancia}km")
print(f"Combustivel gasto: {combustivel}L")

print(f"Consumo Medio: {consumo:.2f}km/l")