#Desafio Sistema Bancário


#Menu

menu = """

======================================
    ## Bem vindo ao Banco Python ##

    Digite a operação desejada:

        [S] Sacar
        [D] Depositar
        [E] Extrato
        [Q] Sair

   "Seu dinheiro é nossa alegria!"
====================================
"""
#dados da conta bancária

saldo = 100
extrato = ""
limite_saque= 500
limite_dia_saque = 3
numero_saque = 0

#Operação

while True:
    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Informe o valor que deseja depositar:"))

        if valor > 0:
                saldo += valor
                extrato += f"\nValor depositado R$: {valor:.2f}\n"
                print (f"\nValor depositado R$: {valor:.2f}\n")
            
        else:
                print ("A operação falhou! O formato do valor é inválido!")

    elif opcao == "S":
        valor = float(input("Informe o valor que deseja sacar:"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque
        excedeu_saque = numero_saque >= limite_dia_saque


        if excedeu_saldo:
                print("Operação Falhou!!Saldo insuficiente!")

        elif excedeu_saque:
            print ("Operação falhou!! Excedeu o limite de saque diário!")

        elif excedeu_limite:
              print("Operação falhou!!! O valor informado ultrapassa seu limite de saque")

        elif valor > 0:
                saldo -= valor
                limite_saque -= 1
                numero_saque += 1
                extrato += f"\nValor sacado R$: {valor:.2f}\n"
                print (f"\nValor sacado R$: {valor:.2f}\n")
        
        else:
            print ("A operação falhou! O formato do valor é inválido!")

    elif opcao == "E":
          print ("\n============Extrato=============\n")
          print("\nNão foram realizadas movimentações" if not extrato else extrato)
          print (f"\nSaldo R$: {saldo:.2f}\n")
          print("================================")
                
    
    elif opcao == "Q":
        break

