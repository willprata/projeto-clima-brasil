# Dados Climáticos no Brasil

## Descrição do projeto

Este projeto apresenta uma análise de dados climáticos do Brasil entre 2015 e 2024, utilizando Python para tratamento, análise e visualização dos dados.

A análise considera informações relacionadas à temperatura, chuva, umidade, velocidade do vento, eventos extremos e níveis de alerta.

O projeto também apresenta um dashboard interativo desenvolvido com Streamlit, permitindo explorar os dados por diferentes filtros.

## Objetivos

- Analisar os dados climáticos do Brasil.
- Realizar a limpeza e preparação dos dados.
- Criar indicadores climáticos.
- Identificar padrões temporais e sazonais.
- Comparar regiões e estados.
- Analisar eventos extremos.
- Apresentar os resultados por meio de gráficos.
- Desenvolver um dashboard interativo.

## Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit
- NumPy
- GitHub

## Base de dados

A base utilizada no projeto é:

`simulacao_clima_brasil(1).csv`

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

- Temperatura média ao longo do tempo
- Chuva total ao longo do tempo
- Volume de chuva por estado
- Temperatura média por região
- Eventos extremos ao longo do tempo
- Temperatura média por mês e ano
- Relação entre temperatura e chuva
- Correlação entre temperatura e chuva
- Média móvel da temperatura

## Dashboard

O dashboard desenvolvido com Streamlit possui filtros para:

- Ano
- Mês
- Região
- Estado
- Cidade
- Nível de alerta

Os indicadores apresentados no dashboard incluem:

- Temperatura média
- Chuva total
- Cidade mais quente
- Estado mais chuvoso
- Total de eventos extremos
- Umidade média

## Estrutura do projeto

```text
projeto-g1/
├── app.py
├── requirements.txt
├── README.md
├── index.html
├── dados/
│   └── simulacao_clima_brasil(1).csv
├── database/
├── imagens/
└── notebooks/