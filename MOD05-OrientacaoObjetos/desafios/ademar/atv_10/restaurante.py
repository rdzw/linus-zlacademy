class Restaurante:
    def __init__(self, nome=None):
        self._nome = nome
        self._clientes = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    def finalizar_pedido(self, cliente, pedido):
        if cliente in self._clientes:
            cliente.fazer_pedido(pedido)
            print(f"Pedido finalizado para o cliente {cliente.nome}.")
        else:
            print(f"Cliente {cliente.nome} não encontrado no sistema.")

    def adicionar_cliente(self, cliente):
        self._clientes.append(cliente)
        print(f"Cliente {cliente.nome} adicionado ao restaurante.")

    def gerar_relatorio_vendas(self):
        total_vendas = sum(cliente.calcular_total() for cliente in self._clientes if cliente._pedidos)
        print(f"Relatório de vendas: R${total_vendas:.2f}")

    def aplicar_promocao_prato(self, prato, desconto_percentual):
        novo_preco = prato.preco * (1 - desconto_percentual / 100)
        prato.atualizar_preco(novo_preco)

    def aplicar_promocao_bebida(self, bebida, desconto_percentual):
        novo_preco = bebida.preco * (1 - desconto_percentual / 100)
        bebida.atualizar_preco(novo_preco)
