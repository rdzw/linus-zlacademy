from prato import Prato
from bebida import Bebida

class Pedido:
    def __init__(self):
        self.pratos = []
        self.bebidas = []

    def adicionar_prato(self, prato):
        if isinstance(prato, Prato):
            self.pratos.append(prato)
            print(f"Prato {prato.nome} adicionado ao pedido.")
        else:
            print("Item inválido, não é um prato.")

    def adicionar_bebida(self, bebida):
        if isinstance(bebida, Bebida):
            self.bebidas.append(bebida)
            print(f"Bebida {bebida.nome} adicionada ao pedido.")
        else:
            print("Item inválido, não é uma bebida.")

    def remover_prato(self, prato):
        if prato in self.pratos:
            self.pratos.remove(prato)
            print(f"Prato {prato.nome} removido do pedido.")
        else:
            print("Prato não encontrado no pedido.")

    def remover_bebida(self, bebida):
        if bebida in self.bebidas:
            self.bebidas.remove(bebida)
            print(f"Bebida {bebida.nome} removida do pedido.")
        else:
            print("Bebida não encontrada no pedido.")

    def calcular_total(self):
        total = sum(prato.preco for prato in self.pratos) + sum(bebida.preco for bebida in self.bebidas)
        return total

    def mostrar_pedido(self):
        print("Pedido atual:")
        for prato in self.pratos:
            prato.mostrar_info()
        for bebida in self.bebidas:
            bebida.mostrar_info()
        print(f"Total: R${self.calcular_total():.2f}")
