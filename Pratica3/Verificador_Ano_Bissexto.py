"""
Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.

Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100)
que não são divisíveis por 400.
"""

# Inserir os dados
ano = int(input("Digite o ano: "))

#Verificação se o ano é bissexto
if ano % 4 == 0: #Se for divisivel pro 4 e não sobrar resto
    if ano % 100 == 0: #Se for divisivel por 100, precisa ser analisado
        if ano % 400 == 0: #Se for divisivel por 400, é bissexto
            print(f"{ano} é um ano bissexto")
        else:
            print(f"O ano {ano} não é bissexto")
    else:
        print(f"{ano} é um ano bissexto")
else:
    print(f"O ano {ano} não é bissexto")

"""
Jeito mais facil
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto)
"""