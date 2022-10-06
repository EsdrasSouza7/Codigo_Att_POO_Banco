from poo.conta.conta import Conta
from poo.banco.banco import Banco

banco = Banco()
while True:

    print("Banco Nº7\nO que gostaria de fazer?\n1-Cadastrar nova conta  2-Conferir Saldo\n3-Depositar Valor(Creditar) "
          " 4-Sacar Valor(Debitar)")
    print("5-Transferir valor entre contas 0-Sair.")
    escolha = int(input("Digite aqui: "))

    if escolha == 1:
        numero = str(input("\n\nDigite o numero que gostaria "))
        test = banco.procurar_conta(numero)
        if test is None:
            numconta = Conta(numero)
            banco.cadastrar(numconta)
            print("Conta cadastrada com sucesso\n")
        else:
            print("numero de conta já existente\n")

    if escolha == 2:
        numero = str(input("\n\nDigite o numero da conta que gostaria de verificar o saldo: "))
        # conta = banco.procurar_conta(numero)
        saldo = banco.saldo(numero)
        if saldo is not None:
            print("O Saldo é: ", saldo, "\n")

    if escolha == 3:
        numero = str(input("\n\nDigite a conta que gostaria de depositar: "))
        test = banco.procurar_conta(numero)
        if test is not None:
            valor = float(input("Digite o Valor do Deposito: "))
            print("O Saldo anterior era:", banco.saldo(numero))
            banco.creditar(numero, valor)
            print("O Saldo atual é: ", banco.saldo(numero), "\n")
        else:
            print("Conta inexistente\n")

    if escolha == 4:
        numero = str(input("\n\nDigite a conta que gostaria de sacar: "))
        test = banco.procurar_conta(numero)
        if test is not None:
            valor = float(input("Digite o Valor do Saque: "))
            print("O Saldo anterior era:", banco.saldo(numero))
            banco.debitar(numero, valor)
            print("O Saldo atual é: ", banco.saldo(numero), "\n")
        else:
            print("Conta inexistente\n")

    if escolha == 5:
        numero = str(input("\n\nDigite o numero da conta de origem: "))
        test = banco.procurar_conta(numero)
        if test is not None:
            numero2 = str(input("Digite o numero da conta conta de destino: "))
            test2 = banco.procurar_conta(numero2)
            if test2 is not None:
                valor = float(input("Digite o Valor que será transferido: "))
                banco.transferir(numero, numero2, valor)
                print("Valor transferido com sucesso!\n")
            else:
                print("Conta de destino inexistente\n")
        else:
            print("Conta inexistente\n")

    if escolha == 0:
        x = str(input("Gostaria de Sair? S/N: "))
        if x == "s" or x == "S" or x == 'sim' or x == 'Sim' or x == 'SIM':
            break
        print("\n")
