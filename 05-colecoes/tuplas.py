"""Operações com tuplas."""

tecnologias = ("Python", "SQL", "Power BI")

print(tecnologias[0])
print(tecnologias[0:2])
print(len(tecnologias))
print(tecnologias.count("Python"))
print(tecnologias.index("SQL"))

linguagem, banco, visualizacao = tecnologias
print(linguagem, banco, visualizacao)

lista_tecnologias = list(tecnologias)
print(lista_tecnologias)
