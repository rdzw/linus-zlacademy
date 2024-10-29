from pagamento import Pagamento

class PagamentoBoleto(Pagamento):
    def __init__(self):
        super().__init__("Boleto")

    def processar_pagamento(self):
        print("Pagamento processado com boleto.")
