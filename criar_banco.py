from poo.banco.banco_lista import BancoLista
from poo.conta.conta import Conta
from poo.conta.contaEspecial import ContaEspecial


class CriarBanco:

    if __name__ == '__main__':
        #criando objs do tipo conta
        contaA = Conta('21.342-7')

        contaB = ContaEspecial('21.342-8')

        # criando obj do banco e cadastrando contas
        # banco = Banco()
        banco = BancoLista()
        banco.cadastrar(contaA)
        banco.cadastrar(contaB)

        print(type(contaA))
        print(type(contaB))

        banco.creditar(contaA.get_numero(),200)
        print(banco.saldo(contaA.get_numero()))

        banco.creditar(contaB.get_numero(),200)
        print(contaB.bonus)
        banco.render_bonus(contaB.get_numero())
        print(contaB.bonus)
        print(banco.saldo(contaB.get_numero()))

