"""Definição e chamada de funções."""


def calcular_media(valores):
    """Retorna a média de uma sequência numérica."""
    if not valores:
        return 0
    return sum(valores) / len(valores)


notas = [8.0, 9.5, 7.5]
print(calcular_media(notas))
