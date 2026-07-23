"""Leitura e escrita usando with."""

arquivo = "exemplo_with.txt"

with open(arquivo, "w", encoding="utf-8") as destino:
    destino.write("O bloco with fecha o arquivo automaticamente.\n")

with open(arquivo, "r", encoding="utf-8") as origem:
    print(origem.read())
