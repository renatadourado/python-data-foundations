"""Remoção segura de arquivo."""

from pathlib import Path

arquivo = Path("exemplo_with.txt")

if arquivo.exists():
    arquivo.unlink()
    print("Arquivo removido.")
else:
    print("Arquivo não encontrado.")
