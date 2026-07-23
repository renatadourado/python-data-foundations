"""Operadores de comparação, pertencimento e identidade."""

idade = 46
idade_minima = 18

print(idade == idade_minima)
print(idade != idade_minima)
print(idade > idade_minima)
print(idade >= idade_minima)
print(idade < idade_minima)
print(idade <= idade_minima)

linguagens = ["Python", "SQL"]
print("Python" in linguagens)
print("Java" not in linguagens)

a = 1
b = a
c = 1.0

print(a == c)  # compara valores
print(a is b)  # compara identidade do objeto
