from pagamento import Pagamento

class PagamentoPix(Pagamento):
    def __init__(self, chave_pix=""):
        self._chave_pix = chave_pix

    @property
    def chave_pix(self):
        return self._chave_pix

    @chave_pix.setter
    def chave_pix(self, chave_pix):
        if "@" not in chave_pix and len(chave_pix) < 10:
            raise ValueError("Chave Pix inválida. Use um e-mail ou chave numérica.")
        self._chave_pix = chave_pix

    def processar_pagamento(self):
        print(f"Pagamento via Pix com a chave {self._chave_pix} processado com sucesso.")