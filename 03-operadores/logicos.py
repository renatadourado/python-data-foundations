"""Operadores lógicos."""

tem_python = True
tem_sql = True
tem_experiencia_cloud = False

print(tem_python and tem_sql)
print(tem_python or tem_experiencia_cloud)
print(not tem_experiencia_cloud)

idade = 46
pode_participar = idade >= 18 and tem_python
print(pode_participar)
