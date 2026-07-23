# 🎮 Análise Exploratória de Vendas de Videogames

Projeto de **Análise Exploratória de Dados (EDA)** desenvolvido integralmente em **Python** para investigar vendas de jogos eletrônicos por plataforma, gênero, editora, ano e região.

## Objetivos

- Identificar os jogos com maiores vendas globais.
- Comparar vendas por gênero, plataforma e editora.
- Analisar a evolução das vendas ao longo dos anos.
- Comparar América do Norte, Europa, Japão e outras regiões.
- Verificar valores ausentes e limitações do conjunto de dados.

## Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- pathlib

## Estrutura do repositório

```text
video-game-sales-eda/
├── assets/
│   └── capa.png
├── data/
│   ├── README.md
│   └── raw/
│       └── vgsales.csv
├── reports/
│   └── figures/
├── src/
│   └── eda_video_game_sales.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

O único arquivo de código-fonte do projeto é Python:

```text
src/eda_video_game_sales.py
```

## Dataset esperado

O projeto utiliza o arquivo `vgsales.csv`, com as colunas:

`Rank`, `Name`, `Platform`, `Year`, `Genre`, `Publisher`, `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales` e `Global_Sales`.

As vendas são apresentadas em milhões de unidades. Coloque o dataset em:

```text
data/raw/vgsales.csv
```

## Como executar

Clone o repositório e entre na pasta:

```bash
git clone URL_DO_SEU_REPOSITORIO
cd video-game-sales-eda
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative no Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a análise:

```bash
python src/eda_video_game_sales.py
```

Os gráficos serão salvos automaticamente em:

```text
reports/figures/
```

## Análises realizadas

1. Visão geral e estatísticas descritivas.
2. Verificação de valores ausentes.
3. Top 10 jogos por vendas globais.
4. Vendas globais por gênero.
5. Top 15 plataformas.
6. Top 15 editoras.
7. Evolução das vendas por ano.
8. Comparação regional das vendas.
9. Avaliação de registros sem ano de lançamento.

## Resultados gerados

O script gera os seguintes gráficos:

- `vendas_globais_por_genero.png`
- `top_15_plataformas.png`
- `top_15_editoras.png`
- `vendas_globais_por_ano.png`
- `vendas_regionais_por_ano.png`
- `participacao_vendas_por_regiao.png`

## Autora

**Renata Franklin Dourado**  
Estudante de Engenharia de Dados em transição de carreira.
