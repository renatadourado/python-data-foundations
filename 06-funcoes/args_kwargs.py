"""Uso de *args e **kwargs."""


def somar(*valores):
    return sum(valores)


def exibir_perfil(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


print(somar(10, 20, 30))
exibir_perfil(nome="Renata", area="Engenharia de Dados", linguagem="Python")
