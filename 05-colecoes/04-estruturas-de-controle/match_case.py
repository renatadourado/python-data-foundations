"""Estrutura match case, disponível a partir do Python 3.10."""

opcao = 2

match opcao:
    case 1:
        print("Cadastrar")
    case 2:
        print("Listar")
    case 3:
        print("Excluir")
    case 4:
        print("Sair")
    case _:
        print("Opção inválida")
