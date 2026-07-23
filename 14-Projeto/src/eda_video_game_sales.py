"""Análise Exploratória de Dados de vendas de videogames.

Execute a partir da raiz do projeto:
    python src/eda_video_game_sales.py

O dataset deve estar em:
    data/raw/vgsales.csv
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "vgsales.csv"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"

REQUIRED_COLUMNS = {
    "Rank",
    "Name",
    "Platform",
    "Year",
    "Genre",
    "Publisher",
    "NA_Sales",
    "EU_Sales",
    "JP_Sales",
    "Other_Sales",
    "Global_Sales",
}

plt.rcParams["figure.figsize"] = (11, 6)
pd.set_option("display.max_columns", None)


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Carrega o CSV e valida as colunas obrigatórias."""
    if not path.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {path}\n"
            "Adicione o arquivo vgsales.csv à pasta data/raw."
        )

    dataframe = pd.read_csv(path)
    missing_columns = REQUIRED_COLUMNS.difference(dataframe.columns)

    if missing_columns:
        raise ValueError(f"Colunas ausentes: {sorted(missing_columns)}")

    return dataframe


def save_current_figure(filename: str) -> None:
    """Salva a figura atual na pasta reports/figures."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / filename, dpi=300, bbox_inches="tight")
    plt.close()


def show_initial_overview(dataframe: pd.DataFrame) -> None:
    """Exibe informações gerais, estatísticas e valores ausentes."""
    print("\n=== VISÃO GERAL ===")
    print(f"Linhas: {dataframe.shape[0]:,}")
    print(f"Colunas: {dataframe.shape[1]}")

    print("\nPrimeiras linhas:")
    print(dataframe.head())

    print("\nTipos de dados e valores não nulos:")
    dataframe.info()

    print("\nEstatísticas descritivas:")
    print(dataframe.describe(include="all").T)

    print("\nValores ausentes por coluna:")
    print(dataframe.isna().sum().sort_values(ascending=False))

    print("\nIntervalo de anos:")
    print("Ano mais antigo:", dataframe["Year"].min())
    print("Ano mais recente:", dataframe["Year"].max())


def analyze_top_games(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Retorna os dez jogos com maiores vendas globais."""
    return dataframe.nlargest(10, "Global_Sales")[
        ["Name", "Platform", "Year", "Genre", "Publisher", "Global_Sales"]
    ]


def analyze_genres(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Agrupa vendas globais por gênero e cria gráfico."""
    genre_sales = (
        dataframe.groupby("Genre", as_index=False)["Global_Sales"]
        .sum()
        .sort_values("Global_Sales", ascending=False)
    )

    plt.figure()
    plt.bar(genre_sales["Genre"], genre_sales["Global_Sales"], edgecolor="black")
    plt.title("Vendas globais por gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Vendas (milhões de unidades)")
    plt.xticks(rotation=75, ha="right")
    save_current_figure("vendas_globais_por_genero.png")

    return genre_sales


def analyze_platforms(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Identifica as quinze plataformas com maiores vendas globais."""
    platform_sales = (
        dataframe.groupby("Platform", as_index=False)["Global_Sales"]
        .sum()
        .sort_values("Global_Sales", ascending=False)
        .head(15)
    )

    plt.figure()
    plt.bar(
        platform_sales["Platform"],
        platform_sales["Global_Sales"],
        edgecolor="black",
    )
    plt.title("Top 15 plataformas por vendas globais")
    plt.xlabel("Plataforma")
    plt.ylabel("Vendas (milhões de unidades)")
    plt.xticks(rotation=75, ha="right")
    save_current_figure("top_15_plataformas.png")

    return platform_sales


def analyze_publishers(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Identifica as quinze editoras com maiores vendas globais."""
    publisher_sales = (
        dataframe.dropna(subset=["Publisher"])
        .groupby("Publisher", as_index=False)["Global_Sales"]
        .sum()
        .sort_values("Global_Sales", ascending=False)
        .head(15)
    )

    plt.figure()
    plt.bar(
        publisher_sales["Publisher"],
        publisher_sales["Global_Sales"],
        edgecolor="black",
    )
    plt.title("Top 15 editoras por vendas globais")
    plt.xlabel("Editora")
    plt.ylabel("Vendas (milhões de unidades)")
    plt.xticks(rotation=75, ha="right")
    save_current_figure("top_15_editoras.png")

    return publisher_sales


def analyze_sales_over_time(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Agrupa as vendas por ano e cria gráficos temporais."""
    sales_by_year = (
        dataframe.dropna(subset=["Year"])
        .groupby("Year", as_index=False)[
            ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]
        ]
        .sum()
        .sort_values("Year")
    )

    plt.figure()
    plt.plot(sales_by_year["Year"], sales_by_year["Global_Sales"])
    plt.title("Vendas globais por ano")
    plt.xlabel("Ano")
    plt.ylabel("Vendas (milhões de unidades)")
    save_current_figure("vendas_globais_por_ano.png")

    plt.figure()
    for column, label in [
        ("NA_Sales", "América do Norte"),
        ("EU_Sales", "Europa"),
        ("JP_Sales", "Japão"),
        ("Other_Sales", "Outras regiões"),
    ]:
        plt.plot(sales_by_year["Year"], sales_by_year[column], label=label)

    plt.title("Vendas por região ao longo dos anos")
    plt.xlabel("Ano")
    plt.ylabel("Vendas (milhões de unidades)")
    plt.legend()
    save_current_figure("vendas_regionais_por_ano.png")

    return sales_by_year


def analyze_regional_sales(dataframe: pd.DataFrame) -> pd.Series:
    """Calcula a participação total de vendas de cada região."""
    regional_sales = dataframe[
        ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
    ].sum()

    plt.figure()
    plt.pie(regional_sales, labels=regional_sales.index, autopct="%1.1f%%")
    plt.title("Participação das vendas por região")
    save_current_figure("participacao_vendas_por_regiao.png")

    return regional_sales.sort_values(ascending=False)


def analyze_missing_years(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Resume os registros que não possuem ano de lançamento."""
    missing_year = dataframe[dataframe["Year"].isna()]

    return (
        missing_year.groupby("Platform")["Global_Sales"]
        .agg(quantidade="count", vendas_globais="sum")
        .sort_values("vendas_globais", ascending=False)
        .head(15)
        .reset_index()
    )


def main() -> None:
    """Executa a análise exploratória completa."""
    dados_games = load_data()
    show_initial_overview(dados_games)

    print("\n=== TOP 10 JOGOS ===")
    print(analyze_top_games(dados_games).to_string(index=False))

    print("\n=== VENDAS POR GÊNERO ===")
    print(analyze_genres(dados_games).to_string(index=False))

    print("\n=== TOP 15 PLATAFORMAS ===")
    print(analyze_platforms(dados_games).to_string(index=False))

    print("\n=== TOP 15 EDITORAS ===")
    print(analyze_publishers(dados_games).to_string(index=False))

    analyze_sales_over_time(dados_games)

    print("\n=== VENDAS POR REGIÃO ===")
    print(analyze_regional_sales(dados_games).to_string())

    print("\n=== REGISTROS SEM ANO DE LANÇAMENTO ===")
    print(analyze_missing_years(dados_games).to_string(index=False))

    print(f"\nGráficos salvos em: {FIGURES_DIR}")


if __name__ == "__main__":
    main()
