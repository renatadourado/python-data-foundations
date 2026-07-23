"""Operações frequentes de tratamento de dados."""

import pandas as pd

df = pd.DataFrame(
    {
        "produto": ["Notebook", "Mouse", "Mouse", "Teclado"],
        "categoria": ["Informática", "Acessórios", "Acessórios", None],
        "preco": ["3500.00", "120.00", "120.00", "250.00"],
        "quantidade": [2, 10, 10, 5],
    }
)

df["preco"] = pd.to_numeric(df["preco"], errors="coerce")
df["categoria"] = df["categoria"].fillna("Não informado")
df = df.drop_duplicates()
df["receita"] = df["preco"] * df["quantidade"]

filtro = df[df["receita"] >= 1000]
agrupado = df.groupby("categoria", as_index=False)["receita"].sum()

print(filtro)
print(agrupado.sort_values("receita", ascending=False))
