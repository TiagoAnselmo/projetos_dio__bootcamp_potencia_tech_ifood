saldo = 500.00
limite_saque_diario = 1500.00
qtde_saques = 0
saque = 0.00
deposito = 0.00

lista_de_operacoes = []
lista_de_valores = []

print("""------------------------MENU BANCO XPTO------------------------
\tDigite 'D' para DEPÓSITO;
\tDigite 'E' para EXTRATO;
\tDigite 'S' para SAQUE;
\tDigite qualquer outro caracter para finalizar a operação.""")

opcao = input("\nInforme agora sua opção:  ")
opcao = opcao.upper()
print("\n")

while opcao == 'D' or opcao == 'E' or opcao == 'S':
        contador = 0
        n = contador
        if opcao == 'D':
            print(f"Saldo disponível em Conta Corrente: R$ {saldo:.2f}")
            deposito = float(input("Informe o valor que deseja depositar em R$(Reais):  "))
            if deposito > 0:
                print("\n")
                saldo += deposito

                lista_de_operacoes.append("Depósito")
                lista_de_valores.append(deposito)

                print(f"Depósito de {deposito:.2f} efetuado com sucesso.")
                print(f"Novo saldo disponível em Conta Corrente: R$ {saldo:.2f}\n")

                print("""\tDigite 'D' para DEPÓSITO;\n\tDigite 'E' para EXTRATO;\n\tDigite 'S' para SAQUE;\n\tDigite qualquer outro caracter para sair.""")
                opcao = input("\nInforme agora sua opção:  ")
                opcao = opcao.upper()
                print("\n")
            else:
                print("Valor inválido!\n")

                print("""\tDigite 'D' para DEPÓSITO;\n\tDigite 'E' para EXTRATO;\n\tDigite 'S' para SAQUE;\n\tDigite qualquer outro caracter para sair.""")
                opcao = input("\nInforme agora sua opção:  ")
                opcao = opcao.upper()
                print("\n")


        elif opcao == 'S':
            if qtde_saques < 3:
                print(f"Saldo disponível em Conta Corrente: R$ {saldo:.2f}")
                saque = float(input("Informe o valor do saque em R$: "))
                if saque <= saldo:
                    print(f"Saque de R$ {saque:.2f} efetuado com sucesso.")
                    qtde_saques += 1
                    saldo -= saque
                    print(f"Novo saldo disponível em Conta Corrente: R$ {saldo:.2f}\n")

                    print("""\tDigite 'D' para DEPÓSITO;\n\tDigite 'E' para EXTRATO;\n\tDigite 'S' para SAQUE;\n\tDigite qualquer outro caracter para sair.""")
                    opcao = input("\nInforme agora sua opção:  ")
                    opcao = opcao.upper()
                    print("\n")

                elif saque > saldo:
                    print("Saldo insuficiente.\n")

                    print("""\tDigite 'D' para DEPÓSITO;\n\tDigite 'E' para EXTRATO;\n\tDigite 'S' para SAQUE;\n\tDigite qualquer outro caracter para sair.""")
                    opcao = input("\nInforme agora sua opção:  ")
                    opcao = opcao.upper()
                    print("\n")

                else:
                    pass
            else:
                print("Limite diário de saques atingido.\n")
                #print(f"Saldo disponível em Conta Corrente: R$ {saldo:.2f}\n")
                print("""\tDigite 'D' para DEPÓSITO;\n\tDigite 'E' para EXTRATO;\n\tDigite 'S' para SAQUE;\n\tDigite qualquer outro caracter para sair.""")
                opcao = input("\nInforme agora sua opção:  ")
                print("\n")


        elif opcao == 'E':


            print("""\tDigite 'D' para DEPÓSITO;\n\tDigite 'E' para EXTRATO;\n\tDigite 'S' para SAQUE;\n\tDigite qualquer outro caracter para sair.""")
            opcao = input("\nInforme agora sua opção:  ")
            print("\n")



        else:
            print("Finalizando...")

print("\nVocê saiu da sua conta. Obrigado por escolher o Banco XPTO.")
print("Tenha um bom dia.")