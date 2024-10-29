from pedido import Pedido

class Cliente:
    def __init__(self, nome=None):
        self._nome = nome
        self._pedidos = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    def fazer_pedido(self, pedido):
        if isinstance(pedido, Pedido):
            self._pedidos.append(pedido)
            print(f"Pedido adicionado ao cliente {self._nome}.")
        else:
            print("Pedido inválido.")

    def mostrar_pedidos(self):
        if not self._pedidos:
            print("Nenhum pedido encontrado.")
        else:
            print(f"Pedidos do cliente {self._nome}:")
            for pedido in self._pedidos:
                pedido.mostrar_pedido()
