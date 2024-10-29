from prato import Prato
from bebida import Bebida
from pedido import Pedido
from cliente import Cliente
from restaurante import Restaurante

def main():
    restaurante = Restaurante("Restaurante Bom Sabor")

    # Criando alguns pratos e bebidas
    prato1 = Prato("Lasanha", 25.50, ["massa", "molho", "queijo"])
    bebida1 = Bebida("Refrigerante", 5.00, 350)

    # Adicionando cliente
    cliente = Cliente("João")
    restaurante.adicionar_cliente(cliente)

    # Fazendo um pedido
    pedido = Pedido()
    pedido.adicionar_prato(prato1)
    pedido.adicionar_bebida(bebida1)

    # Finalizando o pedido
    restaurante.finalizar_pedido(cliente, pedido)

    # Mostrando o pedido
    cliente.mostrar_pedidos()

if __name__ == "__main__":
    main()
