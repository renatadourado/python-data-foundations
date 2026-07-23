"""Gráfico interativo com Plotly."""

import pandas as pd
import plotly.express as px

df = pd.DataFrame(
    {
        "mes": ["Jan", "Fev", "Mar", "Abr"],
        "vendas": [120, 150, 135, 180],
    }
)

fig = px.line(
    df,
    x="mes",
    y="vendas",
    markers=True,
    title="Evolução mensal das vendas",
)
fig.show()
