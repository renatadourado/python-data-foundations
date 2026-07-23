"""Introdução a Series."""

import pandas as pd

vendas = pd.Series(
    [120.5, 98.0, 150.75],
    index=["Janeiro", "Fevereiro", "Março"],
    name="vendas",
)

print(vendas)
print(vendas.mean())
print(vendas.max())
