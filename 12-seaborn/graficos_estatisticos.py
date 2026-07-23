"""Gráfico estatístico com Seaborn."""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame(
    {
        "categoria": ["A", "A", "B", "B", "C", "C"],
        "valor": [10, 14, 9, 15, 20, 18],
    }
)

sns.boxplot(data=df, x="categoria", y="valor")
plt.title("Distribuição por categoria")
plt.tight_layout()
plt.show()
