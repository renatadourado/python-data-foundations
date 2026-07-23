"""Operações com listas."""

frutas = ["banana", "abacaxi", "morango"]

frutas.append("manga")
frutas.insert(1, "laranja")
frutas.remove("banana")

print(frutas[0])
print(frutas[-1])
print(frutas[0:2])
print(len(frutas))
print("morango" in frutas)

frutas.sort()
print(frutas)

outras_frutas = ["melancia", "uva"]
frutas.extend(outras_frutas)
print(frutas)
