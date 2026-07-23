"""Gráficos básicos com Matplotlib."""

import matplotlib.pyplot as plt

meses = ["Jan", "Fev", "Mar", "Abr"]
vendas = [120, 150, 135, 180]

plt.plot(meses, vendas, marker="o", label="Vendas")
plt.title("Evolução mensal das vendas")
plt.xlabel("Mês")
plt.ylabel("Vendas")
plt.legend()
plt.tight_layout()
plt.show()
