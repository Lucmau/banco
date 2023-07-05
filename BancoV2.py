saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
limite_valor_total = 1500
limite_valor_por_saque = 500

usuarios = []
contas = []

def criar_usuario():
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf)
    
    if len(cpf) != 11:
        print("NUMERO DE CPF ERRADO")
        return
  
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
  
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta():
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf)
    
    if len(cpf) != 11:
      print("Numero de CPF ERRADO")
      return
    
    if usuario:
        numero_conta = len(contas) + 1
        conta = {"numero_conta": numero_conta, "usuario": usuario}
        contas.append(conta)
        print("\n=== Conta criada com sucesso! ===")
    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
  
def filtrar_conta(numero_conta):
    contas_filtradas = [conta for conta in contas if conta["numero_conta"] == numero_conta]
    return contas_filtradas[0] if contas_filtradas else None

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta
[6] Sair
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
        criar_usuario()

    elif opcao == "5":
        criar_conta()

    elif opcao == "6":
        print("Obrigado por utilizar nosso banco. Volte sempre!")
        break

    else:
        print("Opção inválida. Digite novamente.")
        
