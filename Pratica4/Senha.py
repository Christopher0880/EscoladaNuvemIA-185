"""
Crie um programa que verifique se uma senha é forte.
Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número.
O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.
"""

while True:
    senha = input("Digite a senha ou digite 'sair' para encerrar: ")

    #Verificação do sair
    if senha.lower() == "sair":
        print("Programa encerrado")
        break
    
    if len(senha) < 8:
        print("Senha fraca, precisa ter pelo menos 8 caracteres")
        continue
    if not any(caractere.isdigit() for caractere in senha):
        print("Senha fraca, pecisa ter pelo menos um número")
        continue
    print("Senha inserida com sucesso")
    break