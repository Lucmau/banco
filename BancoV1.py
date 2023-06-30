saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
limite_valor_total = 1500
limite_valor_por_saque = 500

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""

while True:
    print("\nBem-vindo(a) ao Banco XYZ")
    print(menu)

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
        extrato += f"Depósito: +{valor}\n"
        print(f"Depósito de {valor} realizado com sucesso.")

    elif opcao == "2":
        if numero_saques >= limite_saques:
            print("Limite máximo de saques atingido.")
            continue

        valor = float(input("Digite o valor a ser sacado: "))
        if valor > saldo:
            print("Saldo insuficiente.")
        elif valor > limite_valor_por_saque:
            print(f"O valor máximo por saque é de {limite_valor_por_saque}.")
        elif saldo - valor < -limite:
            print(f"Você atingiu o limite de crédito disponível.")
        elif saldo - valor < -limite_valor_total:
            print(f"Você atingiu o limite de crédito total disponível.")
        else:
            saldo -= valor
            extrato += f"Saque: -{valor}\n"
            numero_saques += 1
            print(f"Saque de {valor} realizado com sucesso.")

    elif opcao == "3":
        print("Extrato bancário:")
        print(extrato)
        print(f"Saldo atual: {saldo}")

    elif opcao == "4":
        print("Obrigado por utilizar nosso banco. Volte sempre!")
        break

    else:
        print("Opção inválida. Digite novamente.")
