from pagamento import Pagamento

class PagamentoCartao(Pagamento):
    def __init__(self):
        super().__init__("Cartão")

    def processar_pagamento(self):
        print("Pagamento processado com cartão.")
