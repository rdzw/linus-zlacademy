from pagamento import Pagamento

class PagamentoCartaoCredito(Pagamento):
    def __init__(self, numero_cartao=""):
        self._numero_cartao = numero_cartao

    @property
    def numero_cartao(self):
        return self._numero_cartao

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao):
        if len(numero_cartao) != 16:
            raise ValueError("O número do cartão de crédito deve ter 16 dígitos.")
        self._numero_cartao = numero_cartao

    def processar_pagamento(self):
        print(f"Pagamento com cartão de crédito {self._numero_cartao} processado com sucesso.")