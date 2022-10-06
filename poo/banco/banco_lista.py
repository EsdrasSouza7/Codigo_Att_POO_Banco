from poo.conta.conta import Conta
from poo.conta.poupanca import ContaPoupanca
from poo.conta.contaEspecial import ContaEspecial


class BancoLista:

    def __init__(self):
        self.contas = []
        self.taxa = 0.01

    def cadastrar(self, conta: Conta):
        self.contas.append(conta)

    def procurar_conta(self, numero):
        for conta in self.contas:
            if conta.get_numero() == numero:
                return conta
        return None

    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)

        else:
            print("Conta Inexistente!")

    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
            if isinstance(conta, ContaEspecial):
                self.render_bonus(numero)
        else:
            print("Conta Inexistente!")

    def saldo(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            return conta.get_saldo()
        else:
            print("Conta Inexistente!")

    def transferir(self, origem, destino, valor):
        origem = self.procurar_conta(origem)
        destino = self.procurar_conta(destino)

        if origem and destino:
            if self.saldo(origem.get_numero()) >= valor:
                origem.debitar(valor)
                destino.creditar(valor)
                print("Transferência realizada com sucesso!")
            else:
                print("Saldo Insuficiente, faça um empréstimo")
        else:
            print("Transferência Impossível! Conta Inexistente!")

    def render_juros(self, numero):
        conta = self.procurar_conta(numero)
        if isinstance(conta, ContaPoupanca):
            conta.render_juros(self.taxa)
        else:
            print("conta nao é Poupança")

    def render_bonus(self, numero):
        conta = self.procurar_conta(numero)
        if isinstance(conta, ContaEspecial):
            conta.renderBonus()
        else:
            print("sua Conta não é Especial")