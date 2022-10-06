from poo.conta.conta import Conta
from poo.conta.poupanca import ContaPoupanca


class CriarPoupanca:
    if __name__ == '__main__':
        conta = Conta("21.342-7")
        #print(type(conta))
        conta = ContaPoupanca(conta)
        #print(type(conta))

        conta.creditar(500.87)
        conta.debitar(45.00)
        print(conta.get_saldo())

        conta.render_juros(0.01)
        print(conta.get_saldo())

        #poupanca.creditar(500.87)
        #poupanca.debitar(45.00)

        #print(poupanca.get_saldo())

        #poupanca.render_juros(0.01)
        #print(poupanca.get_saldo())
