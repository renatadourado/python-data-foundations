"""Exemplo de documentação de funções."""


def calcular_fatorial(numero):
    """Calcula o fatorial de um número inteiro não negativo.

    Args:
        numero: Número inteiro maior ou igual a zero.

    Returns:
        O valor do fatorial.

    Raises:
        ValueError: Quando o número for negativo.
    """
    if numero < 0:
        raise ValueError("O número não pode ser negativo.")

    resultado = 1
    for valor in range(2, numero + 1):
        resultado *= valor
    return resultado


print(calcular_fatorial(5))
