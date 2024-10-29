# menu.py
from pagamentocartaocredito import PagamentoCartaoCredito
from pagamentoboleto import PagamentoBoleto
from pagamentopix import PagamentoPix

def processar(pagamento):
    """Função que chama o método processar_pagamento() da classe de pagamento"""
    pagamento.processar_pagamento()

def exibir_menu():
    print("\n=== Sistema de Pagamentos ===")
    print("1. Pagamento com Cartão de Crédito")
    print("2. Pagamento com Boleto")
    print("3. Pagamento via Pix")
    print("4. Sair")

def pagamento_cartao():
    numero = input("Digite o número do cartão de crédito (16 dígitos): ")
    pagamento = PagamentoCartaoCredito()
    try:
        pagamento.numero_cartao = numero
        processar(pagamento)
    except ValueError as e:
        print(f"Erro: {e}")

def pagamento_boleto():
    codigo = input("Digite o código do boleto (13 dígitos): ")
    pagamento = PagamentoBoleto()
    try:
        pagamento.codigo_boleto = codigo
        processar(pagamento)
    except ValueError as e:
        print(f"Erro: {e}")

def pagamento_pix():
    chave = input("Digite a chave Pix (e-mail ou chave numérica): ")
    pagamento = PagamentoPix()
    try:
        pagamento.chave_pix = chave
        processar(pagamento)
    except ValueError as e:
        print(f"Erro: {e}")

def switch_case(opcao):
    """Dicionário para emular switch-case"""
    opcoes = {
        '1': pagamento_cartao,
        '2': pagamento_boleto,
        '3': pagamento_pix,
        '4': sair
    }
    func = opcoes.get(opcao, lambda: print("Opção inválida!"))
    func()

def sair():
    print("Encerrando o sistema. Até logo!")
    exit(0)

if __name__ == "__main__":
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        switch_case(opcao)
