from pagamento_cartao import PagamentoCartao
from pagamento_boleto import PagamentoBoleto

def testar_pagamentos():
    pagamento_cartao = PagamentoCartao()
    pagamento_boleto = PagamentoBoleto()

    print("\n-- Testando pagamento com Cartão --")
    pagamento_cartao.detalhes_pagamento()
    pagamento_cartao.processar_pagamento()

    print("\n-- Testando pagamento com Boleto --")
    pagamento_boleto.detalhes_pagamento()
    pagamento_boleto.processar_pagamento()

def menu():
    while True:
        print("\n--- Menu de Pagamentos ---")
        print("1 - Testar Pagamento com Cartão")
        print("2 - Testar Pagamento com Boleto")
        print("3 - Testar Ambos os Pagamentos")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                pagamento = PagamentoCartao()
                pagamento.detalhes_pagamento()
                pagamento.processar_pagamento()
            case '2':
                pagamento = PagamentoBoleto()
                pagamento.detalhes_pagamento()
                pagamento.processar_pagamento()
            case '3':
                testar_pagamentos()
            case '0':
                print("Saindo do programa.")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
