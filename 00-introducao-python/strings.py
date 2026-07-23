"""Exemplos básicos com strings."""

nome = "Renata"
area = "Engenharia de Dados"

# Concatenação
apresentacao = nome + " estuda " + area
print(apresentacao)

# f-string
print(f"{nome} está construindo um portfólio de {area}.")

# Fatiamento
linguagem = "Python"
print(linguagem[0:3])
print(linguagem[::-1])

# Métodos
texto = "  python para dados  "
print(texto.strip())
print(texto.upper())
print(texto.title())
print(texto.replace("dados", "engenharia de dados"))
