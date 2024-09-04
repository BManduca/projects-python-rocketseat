from abc import ABC, abstractmethod

class Pagamento(ABC):

  @abstractmethod
  def realizar_pagamento(self, valor):
    pass

  def validar_pagamento(self):
    pass

class PagamentoCartao(Pagamento):

  def realizar_pagamento(self, valor):
    print(f"Pagando com cartão: {valor}")

  def validar_pagamento(self):

    approved = str(input('COMPRA CARTÃO FOI APROVADA? (S/N)  ')).upper()

    while approved not in 'SN':
      print('\n << RESPOSTA INCORRETA >> ')
      approved = str(input('COMPRA CARTÃO FOI APROVADA? (S/N)  ')).upper()

      if approved == 'S':
        print('\n << COMPRA CARTÃO APROVADA >> ')
      else:
        print('\n << COMPRA CARTÃO REJEITADA >> ')

class PagamentoBoleto(Pagamento):

  def realizar_pagamento(self, valor):
    print(f"Pagando com boleto: {valor}")

  def validar_pagamento(self):

    boleto_vencimento = str(input('O BOLETO PASSOU DA DATA DE VENCIMENTO? (S/N)  ')).upper()

    while boleto_vencimento not in 'SN':
      print('\n << RESPOSTA INCORRETA >> ')
      boleto_vencimento = str(input('O BOLETO PASSOU DA DATA DE VENCIMENTO? (S/N)  ')).upper()

      if boleto_vencimento == 'N':
        print('O BOLETO ESTÁ EM DIA E PODE SER PAGO!')
      else:
        print('O BOLETO ESTÁ VENCIDO!')


value = int(input('INSIRA O VALOR A SER PAGO: '))

pagamento_cartao = PagamentoCartao()