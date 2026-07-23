"""Escopo global, local e nonlocal."""

mensagem = "Escopo global"


def funcao_externa():
    contador = 0

    def funcao_interna():
        nonlocal contador
        contador += 1
        print("Contador local:", contador)

    funcao_interna()
    print(mensagem)


funcao_externa()
