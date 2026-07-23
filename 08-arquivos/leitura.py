"""Leitura de arquivo de texto."""

from pathlib import Path

arquivo = Path("exemplo.txt")

if arquivo.exists():
    conteudo = arquivo.read_text(encoding="utf-8")
    print(conteudo)
else:
    print("O arquivo exemplo.txt ainda não existe.")
