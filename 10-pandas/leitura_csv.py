"""Leitura e validação básica de CSV."""

from pathlib import Path
import pandas as pd

caminho = Path("dados.csv")

if caminho.exists():
    df = pd.read_csv(caminho)

    print(df.head())
    print(df.info())
    print(df.isnull().sum())
else:
    print("Inclua um arquivo chamado dados.csv nesta pasta para executar o exemplo.")
