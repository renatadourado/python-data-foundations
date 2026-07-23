"""Operações com sets."""

grupo_a = {"Python", "SQL", "Pandas"}
grupo_b = {"Python", "Spark", "Azure"}

grupo_a.add("Git")

print(grupo_a | grupo_b)  # união
print(grupo_a & grupo_b)  # interseção
print(grupo_a - grupo_b)  # diferença
print(grupo_a ^ grupo_b)  # diferença simétrica

imutavel = frozenset({"Python", "SQL"})
print(imutavel)
