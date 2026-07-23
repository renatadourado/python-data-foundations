"""Tratamento de exceções."""


def dividir(dividendo, divisor):
    if divisor == 0:
        raise ValueError("O divisor não pode ser zero.")
    return dividendo / divisor


try:
    numero = int("10")
    resultado = dividir(numero, 2)
except ValueError as erro:
    print(f"Erro de valor: {erro}")
except TypeError as erro:
    print(f"Erro de tipo: {erro}")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Execução finalizada.")
