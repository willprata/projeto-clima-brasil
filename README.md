# 🌦️ Dados Climáticos no Brasil

### Painel Analítico de Dados Climáticos (2015–2024)

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4c72b0)](https://seaborn.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3f4f75?logo=plotly)](https://plotly.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-ff4b4b?logo=streamlit)](https://streamlit.io/)

**[📊 Dashboard no Streamlit](https://dados-climaticos-brasil.streamlit.app)**  
**[🌐 GitHub Pages](https://willprata.github.io/projeto-clima-brasil/)**  
**[💻 Repositório no GitHub](https://github.com/willprata/projeto-clima-brasil)**

---

## 📌 Visão Geral

Este projeto apresenta uma análise de dados climáticos do Brasil entre **2015 e 2024**, utilizando Python para tratamento, preparação, análise e visualização dos dados.

A base contém informações sobre temperatura, chuva, umidade, velocidade do vento, eventos extremos e níveis de alerta.

O projeto também conta com um **dashboard interativo desenvolvido com Streamlit**, permitindo explorar os dados por diferentes períodos, regiões, estados, cidades e níveis de alerta.

> ⚠️ **Observação:** a base utilizada é simulada. Portanto, os resultados representam os padrões presentes no conjunto de dados analisado e não devem ser interpretados como medições reais do clima brasileiro.

---

## 👨‍🎓 Identificação Acadêmica

**Disciplina:** Linguagem de Programação — Análise e Visualização de Dados com Python  
**Professor:** Alexandre Neves Louzada  
**Aluno:** Wilson da Silva Prata Junior

---

## 🎯 Objetivos

- Analisar os dados climáticos do Brasil.
- Realizar a limpeza e preparação dos dados.
- Criar indicadores climáticos.
- Identificar padrões temporais e sazonais.
- Comparar regiões e estados.
- Analisar eventos extremos.
- Avaliar a relação entre temperatura e chuva.
- Apresentar os resultados por meio de gráficos.
- Desenvolver um dashboard interativo.

---

## 📊 Principais Indicadores

Os principais KPIs calculados a partir da base foram:

| Indicador | Resultado |
|---|---:|
| Temperatura média nacional | **24,99 °C** |
| Chuva total | **470.175,10 mm** |
| Cidade com maior temperatura média | **Vila Velha** |
| Estado com maior volume de chuva | **RJ** |
| Total de eventos extremos | **8.918** |
| Umidade média | **66,41%** |

---

## 📈 Análises Realizadas

### Temperatura ao longo do tempo

Foi analisada a evolução da temperatura média anual entre 2015 e 2024.

O maior valor médio anual foi registrado em **2024, com aproximadamente 25,29 °C**.

### Chuva ao longo do tempo

Foi analisado o volume total anual de chuva.

O maior volume anual ocorreu em **2022, com 48.538,5 mm**, enquanto o menor ocorreu em **2018, com 45.040,3 mm**.

### Comparação entre estados

Foi realizada a comparação do volume total de chuva entre os estados da base.

O **Rio de Janeiro** apresentou o maior volume total de chuva.

### Comparação entre regiões

Foi analisada a temperatura média das regiões brasileiras presentes na base.

As diferenças entre as médias regionais foram pequenas.

### Eventos extremos

Foi analisada a quantidade de eventos extremos ao longo dos anos.

O maior total ocorreu em **2021, com 924 eventos**.

No período analisado, foram contabilizados **8.918 eventos extremos**.

### Análise sazonal

A análise mensal permitiu observar variações sazonais nas temperaturas.

Na base analisada, **janeiro apresentou a maior temperatura média mensal, com aproximadamente 25,53 °C**, enquanto **abril apresentou a menor, com aproximadamente 24,75 °C**.

### Temperatura × chuva

Foi analisada a relação entre temperatura média e volume de chuva.

A correlação calculada foi de **-0,01**, indicando que não foi observada uma relação linear relevante entre essas duas variáveis na base analisada.

---

## 🔎 Filtros do Dashboard

O dashboard permite filtrar os dados por:

- Ano
- Mês
- Região
- Estado
- Cidade
- Nível de alerta

Os filtros podem ser combinados para permitir uma análise mais específica dos dados.

---

## 📊 Visualizações

O projeto apresenta diferentes visualizações para facilitar a interpretação dos dados:

- Temperatura média ao longo do tempo.
- Chuva total ao longo do tempo.
- Volume de chuva por estado.
- Temperatura média por região.
- Eventos extremos ao longo dos anos.
- Heatmap de temperatura por mês e ano.
- Relação entre temperatura média e chuva.
- Correlação entre variáveis climáticas.
- Distribuição de eventos extremos.
- Análises de umidade, vento e níveis de alerta.
- Tabela dinâmica dos dados filtrados.

---

## 🖥️ Dashboard Interativo

O dashboard foi desenvolvido utilizando **Streamlit**.

Ele reúne os principais indicadores, filtros, gráficos e interpretações da análise em uma interface interativa.

### Acesso

**[📊 Abrir Dashboard no Streamlit](https://dados-climaticos-brasil.streamlit.app)**

---

## 📓 Notebook

O projeto possui um notebook de análise desenvolvido em Python, contendo as seguintes etapas:

1. Introdução
2. Contextualização climática
3. Explicação da base
4. Leitura dos dados
5. Limpeza e preparação
6. Engenharia de atributos
7. KPIs
8. Visualizações
9. Interpretação
10. Conclusão

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- GitHub

---

## 📁 Estrutura do Projeto

```text
projeto-clima-brasil/
├── app.py
├── requirements.txt
├── README.md
├── index.html
├── dados/
│   └── simulacao_clima_brasil.csv
├── database/
├── imagens/
└── notebooks/
    └── analise_clima.ipynb