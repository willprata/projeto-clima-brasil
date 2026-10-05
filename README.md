# Dados Climáticos no Brasil

## Descrição do projeto

Este projeto apresenta uma análise de dados climáticos do Brasil entre 2015 e 2024, utilizando Python para tratamento, análise e visualização dos dados.

A análise considera informações relacionadas à temperatura, chuva, umidade, velocidade do vento, eventos extremos e níveis de alerta.

A base de dados utilizada no projeto é simulada e foi fornecida para a realização da atividade. Portanto, os resultados representam os padrões presentes no conjunto de dados analisado e não medições reais do clima brasileiro.

O projeto também apresenta um dashboard interativo desenvolvido com Streamlit, permitindo explorar os dados por diferentes filtros e visualizar os principais indicadores climáticos.

## Objetivos

- Analisar os dados climáticos do Brasil.
- Realizar a limpeza e preparação dos dados.
- Criar indicadores climáticos.
- Identificar padrões temporais e sazonais.
- Comparar regiões e estados.
- Analisar eventos extremos.
- Investigar a relação entre temperatura e chuva.
- Apresentar os resultados por meio de gráficos e tabelas.
- Desenvolver um dashboard interativo.

## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- GitHub

## Base de dados

A base utilizada no projeto é:

`dados/simulacao_clima_brasil.csv`

Os dados abrangem o período de 2015 a 2024.

Entre as principais variáveis estão:

- Ano
- Mês
- Data
- Região
- Estado
- Cidade
- Temperatura média
- Temperatura máxima
- Temperatura mínima
- Chuva
- Umidade
- Velocidade do vento
- Eventos extremos
- Nível de alerta

## Análises realizadas

O projeto apresenta análises de:

- Temperatura média ao longo do tempo.
- Chuva média mensal por ano.
- Comparação de temperatura entre regiões.
- Comparação de volume de chuva entre estados.
- Identificação de eventos extremos.
- Eventos extremos por região.
- Análise sazonal.
- Temperatura média por mês e ano.
- Períodos de menor e maior volume de chuva.
- Relação entre temperatura e chuva.
- Correlação entre temperatura e chuva.
- Correlação entre variáveis climáticas.
- Média móvel da temperatura.
- Relação entre temperatura e eventos extremos.
- Análise dos níveis de alerta.
- Análise de umidade e velocidade do vento.
- Índice de vulnerabilidade climática por região.
- Tabela dinâmica para exploração dos dados.

## Dashboard

O dashboard desenvolvido com Streamlit possui filtros interativos para:

- Ano
- Mês
- Região
- Estado
- Cidade
- Nível de alerta

Os principais indicadores apresentados incluem:

- Temperatura média nacional
- Volume total de chuva
- Cidade mais quente
- Estado mais chuvoso
- Total de eventos extremos
- Média de umidade

O dashboard também apresenta:

- Análise temporal
- Comparações entre regiões e estados
- Análise sazonal
- Relações climáticas
- Análise de alertas, vento e umidade
- Tabela dinâmica dos dados
- Interpretações textuais
- Conclusão executiva

## Estrutura do projeto

```text
projeto-clima-brasil/
├── app.py
├── requirements.txt
├── README.md
├── index.html
├── dados/
│   └── simulacao_clima_brasil.csv
├── database/
│   └── .gitkeep
├── imagens/
│   └── .gitkeep
└── notebooks/
    └── analise_clima.ipynb