"""Escrita de arquivo de texto."""

from pathlib import Path

arquivo = Path("exemplo.txt")
arquivo.write_text(
    "Python aplicado à Engenharia de Dados.\n",
    encoding="utf-8",
)

print(f"Arquivo criado em: {arquivo.resolve()}")
