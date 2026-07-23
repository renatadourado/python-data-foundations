"""Laço while, break e continue."""

contador = 0

while contador < 10:
    contador += 1

    if contador == 4:
        continue

    if contador == 8:
        break

    print(contador)
