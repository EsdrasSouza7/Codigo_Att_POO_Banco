from poo.conta.conta import Conta
from poo.conta.contaEspecial import ContaEspecial

class CriarConta:

   if __name__ == '__main__':
       conta = Conta('21.342-7')
       conta.creditar(543)
       especial = ContaEspecial('785-853')
       especial.creditar(543)
       print(type(conta))
       print(conta.get_saldo())
       conta = especial

       print(type(conta))
       print(conta.get_saldo())
       conta.renderBonus()
       print(conta.get_saldo())
