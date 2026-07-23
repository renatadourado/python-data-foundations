# 14 — Projeto: VideoGames Sales

Análise exploratória de dados de vendas globais de videogames.

## Objetivos

- Identificar os jogos mais vendidos.
- Avaliar os gêneros mais populares.
- Comparar plataformas e distribuidoras.
- Analisar vendas por região e por ano.
- Identificar valores ausentes.
- Produzir gráficos e conclusões.

## Arquivos

- `videogame_sales.ipynb`: notebook principal.
- `dataset/`: local reservado para o arquivo `vgsales.csv`.
- `imagens/`: local para gráficos exportados.
- `relatorio.md`: síntese do projeto.

## Como executar

1. Coloque `vgsales.csv` dentro da pasta `dataset`.
2. Ajuste no notebook o caminho de leitura para:

```python
pd.read_csv("dataset/vgsales.csv")
```

3. Instale as dependências:

```bash
pip install pandas matplotlib plotly seaborn ydata-profiling
```

4. Abra o notebook no Jupyter.
