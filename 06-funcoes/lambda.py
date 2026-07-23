"""Funções lambda."""

dobro = lambda numero: numero * 2
print(dobro(10))

produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse", "preco": 120},
]

ordenados = sorted(produtos, key=lambda produto: produto["preco"])
print(ordenados)
