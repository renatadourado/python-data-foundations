# Ambientes virtuais

Ambientes virtuais isolam as bibliotecas de cada projeto.

## Python puro

```bash
python -m venv .venv
```

Ativação no Windows:

```bash
.venv\Scripts\activate
```

Desativação:

```bash
deactivate
```

## Anaconda

```bash
conda create --name python-data-foundations python
conda activate python-data-foundations
conda deactivate
```

## Dependências

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```
