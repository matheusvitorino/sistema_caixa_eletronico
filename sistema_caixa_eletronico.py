import os

os.system("cls")

print("Sistema de Caixa Eletrônico")

nome_usuario = input("Usuário: ")
senha_usuario = int(input("Senha: "))

saldo = 1000.0

while True:
    print("===Menu===")
    print("[1] - Ver Saldo")
    print("[2] - Depositar")
    print("[3] - Sacar")
    print("[4] - Sair")

    opcao = int(input("Escolha uma opção: "))

    os.system("cls")

    if opcao == 1:
        print(f"Seu saldo é: R$ {saldo:.2f}")

    elif opcao == 2:
        deposito = float(input("Escolha o valor do depósito R$: "))
        
        if deposito <= 0:
            print("Valor inválido!")
        else:
            saldo += deposito
            print(f"Depósito realizado! Novo saldo: R$ {saldo:.2f}")

    elif opcao == 3:
        saque = float(input("Informe o valor que gostaria de sacar R$: "))

        if saque <= 0:
            print("Valor inválido!")
        elif saque > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= saque
            print(f"Saque realizado com sucesso! Novo saldo: R$ {saldo:.2f}")

    elif opcao == 4:
        input("Pressione <Enter> para sair...")
        break

    else:
        print("Opção inválida!")

print("Finalizou o Programa!")
