from poo.conta.conta import Conta
from poo.conta.poupanca import ContaPoupanca


class VerificarPoupanca:
    if __name__ == '__main__':
        opcao = int(input("ESCOLHA: [1] CONTA E [2] POUPANCA: "))
        if opcao == 1:
            conta = Conta("21.342-7")
        else:
            conta = ContaPoupanca("21.342-7")

        conta.creditar(500.87)
        conta.debitar(45.00)
        print("Saldo: ",conta.get_saldo())
        if isinstance(conta, ContaPoupanca):
            conta.render_juros(0.1)
            print("Saldo com juros: {}".format(conta.get_saldo()))