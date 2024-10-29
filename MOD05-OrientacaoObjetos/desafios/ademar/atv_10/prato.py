class Prato:
    def __init__(self, nome=None, preco=0.0, ingredientes=None):
        self._nome = nome
        self._preco = preco
        self._ingredientes = ingredientes if ingredientes is not None else []

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
    def ingredientes(self):
        return self._ingredientes

    def mostrar_info(self):
        ingredientes = ', '.join(self._ingredientes)
        print(f"Prato: {self._nome}, Preço: R${self._preco:.2f}, Ingredientes: {ingredientes}")

    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"Preço atualizado: R${self._preco:.2f}")
