from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, metodo):
        self._metodo = metodo

    @property
    def metodo(self):
        return self._metodo

    @metodo.setter
    def metodo(self, value):
        self._metodo = value

    @abstractmethod
    def processar_pagamento(self):
        pass

    def detalhes_pagamento(self):
        print(f"Processando pagamento via {self._metodo}")
