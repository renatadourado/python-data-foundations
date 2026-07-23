"""Ponto de entrada da aplicação."""

from modulo import calcular_total, saudacao


def main():
    print(saudacao("Renata"))
    print(calcular_total([10, 20, 30]))


if __name__ == "__main__":
    main()
