"""Principais tipos de dados."""

inteiro = 10
decimal = 10.5
texto = "Python"
booleano = True
valor_nulo = None

print(type(inteiro))
print(type(decimal))
print(type(texto))
print(type(booleano))
print(type(valor_nulo))

# Conversão de tipos
numero_texto = "25"
numero = int(numero_texto)
print(numero + 5)

# Datas
from datetime import date, datetime

hoje = date.today()
agora = datetime.now()

print(hoje)
print(agora)
