class Bebida:
    def __init__(self, nome=None, preco=0.0, tamanho=0):
        self._nome = nome
        self._preco = preco
        self._tamanho = tamanho

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = valor

    @property
    def tamanho(self):
        return self._tamanho

    @tamanho.setter
    def tamanho(self, valor):
        self._tamanho = valor

    def mostrar_info(self):
        print(f"Bebida: {self._nome}, Preço: R${self._preco:.2f}, Tamanho: {self._tamanho}ml")

    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"Preço atualizado: R${self._preco:.2f}")
