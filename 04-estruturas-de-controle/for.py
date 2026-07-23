"""Laço for e enumerate."""

tecnologias = ["Python", "SQL", "Pandas"]

for tecnologia in tecnologias:
    print(tecnologia)

for indice, tecnologia in enumerate(tecnologias, start=1):
    print(indice, tecnologia)

quadrados = [numero ** 2 for numero in range(1, 6)]
print(quadrados)
