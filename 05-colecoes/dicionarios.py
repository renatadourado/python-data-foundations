"""Operações com dicionários."""

pessoa = {
    "nome": "Renata",
    "formacao": "Engenharia Química",
    "objetivo": "Engenharia de Dados",
}

print(pessoa["nome"])
print(pessoa.get("objetivo"))

pessoa["cidade"] = "Ponta Grossa"
pessoa.update({"linguagem": "Python"})

for chave, valor in pessoa.items():
    print(chave, valor)

print(list(pessoa.keys()))
print(list(pessoa.values()))
print(len(pessoa))
