"""
Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:

Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""
nome_produto = "Cadeira Infantil"
preco_produto = 12.40
quantidade = 3
preco_total = preco_produto * quantidade

print(f"Nome do produto {nome_produto}")
print(f"Valor: R${preco_produto}")
print(f"Quantidade {quantidade}")

print(f"Preço Total: R${preco_total:.2f}")