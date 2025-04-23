# Desafio Sistema Bancário II - Versão revisada com correções

import textwrap

def menu():
    menu_texto = """
    ======================================
        ## Bem vindo ao Banco Python ##

        Digite a operação desejada:

            [S] Sacar
            [D] Depositar
            [E] Extrato
            [NU] Novo Usuário
            [NC] Nova Conta
            [LC] Listar Conta
            [Q] Sair

    "Seu dinheiro é nossa alegria!"
    =====================================
    """
    return input(textwrap.dedent(menu_texto))

def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"\nValor depositado R$: {valor:.2f}\n"
        print("\n==== Valor depositado com Sucesso!====\n")
    else:
        print("A operação falhou! O formato do valor é inválido!!!")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nA operação falhou!! Você não tem saldo suficiente!")
    elif excedeu_limite:
        print("\nA operação falhou!! O valor do saque excede o limite!")
    elif excedeu_saques:
        print("\nA operação falhou!! Você excedeu o limite diário de saques!")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque Realizado com sucesso!! ===")
    else:
        print("\nA operação falhou!! O valor informado é inválido!")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO =========")
    print("Não foram realizadas movimentações" if not extrato.strip() else extrato)
    print(f"\nSaldo: \t\t R$ {saldo:.2f}")
    print("==============================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário cadastrado com este CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("===== Usuário Cadastrado com Sucesso! =====")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso!! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência:	{conta['agencia']}
        C/C:		{conta['numero_conta']}
        Titular:	{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao.upper() == "D":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(valor, saldo, extrato)

        elif opcao.upper() == "S":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao.upper() == "E":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao.upper() == "NU":
            criar_usuario(usuarios)

        elif opcao.upper() == "NC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao.upper() == "LC":
            listar_contas(contas)

        elif opcao.upper() == "Q":
            print("\nObrigado por utilizar nosso sistema bancário. Até logo!")
            break

        else:
            print("\nOperação inválida. Por favor, selecione uma opção válida.")

if __name__ == "__main__":
    main()