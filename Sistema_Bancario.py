menu = """
Selecione uma das opções:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input (menu)

    if opcao == "1":
        valor = float (input("Informe o valor para efetuar o depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado, em alguns instantes o valor estará disponível em sua conta.")

        else:
            print("Operação falhou! Revise o valor informado.")

    elif opcao == "2":
        valor =float(input("Informe o valor para efetuar o saque: "))
        

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque extrapolou o limite diário.")

        elif excedeu_saques:
            print("O número máximo de tentativas extrapolou, permitido apenas 03 por dia.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Aguarde a contagem das notas e retire no local indicado.")

        else:
            print("Operação falhou! Valor informado nulo.")
    
    elif opcao == "3":
        print("\n**************** EXTRATO ****************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("******************************************")

    elif opcao == "0":
        print("Obrigado por nos escolher! Aguardamos o seu retorno!")        
        break

    else:
        print("Operação anulada, por favor selecione novamente a opção pretendida, conforme o menu disponível.")
        