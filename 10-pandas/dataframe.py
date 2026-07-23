"""Introdução a DataFrames."""

import pandas as pd

dados = {
    "produto": ["Notebook", "Mouse", "Teclado"],
    "quantidade": [2, 10, 5],
    "preco": [3500.0, 120.0, 250.0],
}

df = pd.DataFrame(dados)
df["receita"] = df["quantidade"] * df["preco"]

print(df.head())
print(df.dtypes)
print(df.shape)
print(df.describe(numeric_only=True))
