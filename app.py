import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# =========================================================
# CONFIGURAÇÃO
# =========================================================

st.set_page_config(
    page_title="Dados Climáticos no Brasil",
    page_icon="🌦️",
    layout="wide"
)


# =========================================================
# LEITURA DA BASE
# =========================================================

@st.cache_data
def carregar_dados():
    df = pd.read_csv("dados/simulacao_clima_brasil(1).csv")
    df["data"] = pd.to_datetime(df["data"])

    return df


df = carregar_dados()


# =========================================================
# TÍTULO
# =========================================================

st.title("🌦️ Dados Climáticos no Brasil")

st.markdown(
    """
    **Disciplina:** Linguagem de Programação — Análise e Visualização de Dados com Python

    **Professor:** Alexandre Neves Louzada

    **Aluno:** Wilson da Silva Prata Junior
    """
)

st.write(
    """
    Este projeto apresenta uma análise dos dados climáticos do Brasil
    entre 2015 e 2024, considerando temperatura, chuva, umidade,
    velocidade do vento, eventos extremos e níveis de alerta.
    """
)


# =========================================================
# FILTROS
# =========================================================

st.sidebar.header("🔎 Filtros")

st.sidebar.write(
    "Selecione os critérios para explorar os dados."
)


# Ano
anos = sorted(df["ano"].unique())

ano_opcoes = ["Todos"] + [str(ano) for ano in anos]

ano_selecionado = st.sidebar.selectbox(
    "Ano",
    ano_opcoes
)


# Mês
meses_nomes = {
    1: "Jan",
    2: "Fev",
    3: "Mar",
    4: "Abr",
    5: "Mai",
    6: "Jun",
    7: "Jul",
    8: "Ago",
    9: "Set",
    10: "Out",
    11: "Nov",
    12: "Dez"
}

mes_opcoes = ["Todos"] + list(meses_nomes.values())

mes_selecionado = st.sidebar.selectbox(
    "Mês",
    mes_opcoes
)


# Região
regioes = sorted(df["regiao"].unique())

regiao_opcoes = ["Todas"] + regioes

regiao_selecionada = st.sidebar.selectbox(
    "Região",
    regiao_opcoes
)


# Estado
estados = sorted(df["uf"].unique())

estado_opcoes = ["Todos"] + estados

estado_selecionado = st.sidebar.selectbox(
    "Estado",
    estado_opcoes
)


# Cidade
cidades = sorted(df["cidade"].unique())

cidade_opcoes = ["Todas"] + cidades

cidade_selecionada = st.sidebar.selectbox(
    "Cidade",
    cidade_opcoes
)


# Nível de alerta
alertas = sorted(df["nivel_alerta"].unique())

alerta_opcoes = ["Todos"] + alertas

alerta_selecionado = st.sidebar.selectbox(
    "Nível de alerta",
    alerta_opcoes
)


# =========================================================
# APLICAÇÃO DOS FILTROS
# =========================================================

df_filtrado = df.copy()


if ano_selecionado != "Todos":
    df_filtrado = df_filtrado[
        df_filtrado["ano"] == int(ano_selecionado)
    ]


if mes_selecionado != "Todos":

    mes_numero = [
        numero
        for numero, nome in meses_nomes.items()
        if nome == mes_selecionado
    ][0]

    df_filtrado = df_filtrado[
        df_filtrado["mes"] == mes_numero
    ]


if regiao_selecionada != "Todas":
    df_filtrado = df_filtrado[
        df_filtrado["regiao"] == regiao_selecionada
    ]


if estado_selecionado != "Todos":
    df_filtrado = df_filtrado[
        df_filtrado["uf"] == estado_selecionado
    ]


if cidade_selecionada != "Todas":
    df_filtrado = df_filtrado[
        df_filtrado["cidade"] == cidade_selecionada
    ]


if alerta_selecionado != "Todos":
    df_filtrado = df_filtrado[
        df_filtrado["nivel_alerta"] == alerta_selecionado
    ]


# =========================================================
# QUANTIDADE DE REGISTROS
# =========================================================

st.caption(
    f"Registros encontrados: {len(df_filtrado)}"
)


# =========================================================
# VERIFICAÇÃO
# =========================================================

if len(df_filtrado) == 0:

    st.warning(
        "Nenhum registro foi encontrado com os filtros selecionados."
    )

    st.stop()


# =========================================================
# KPIs
# =========================================================

st.header("📌 Indicadores climáticos")


temperatura_media = (
    df_filtrado["temperatura_media"].mean()
)


chuva_total = (
    df_filtrado["chuva_mm"].sum()
)


cidade_mais_quente = (
    df_filtrado
    .groupby("cidade")["temperatura_media"]
    .mean()
    .idxmax()
)


estado_mais_chuvoso = (
    df_filtrado
    .groupby("uf")["chuva_mm"]
    .sum()
    .idxmax()
)


total_eventos = (
    df_filtrado["eventos_extremos"].sum()
)


umidade_media = (
    df_filtrado["umidade"].mean()
)


col1, col2, col3 = st.columns(3)

col1.metric(
    "🌡️ Temperatura média",
    f"{temperatura_media:.2f} °C"
)

col2.metric(
    "🌧️ Chuva total",
    f"{chuva_total:,.2f} mm"
)

col3.metric(
    "🔥 Cidade mais quente",
    cidade_mais_quente
)


col4, col5, col6 = st.columns(3)

col4.metric(
    "💧 Estado mais chuvoso",
    estado_mais_chuvoso
)

col5.metric(
    "⚠️ Eventos extremos",
    f"{total_eventos:,.0f}"
)

col6.metric(
    "💨 Umidade média",
    f"{umidade_media:.2f}%"
)


# =========================================================
# ANÁLISE TEMPORAL
# =========================================================

st.header("📈 Análise temporal")

col1, col2 = st.columns(2)


# Temperatura por ano
with col1:

    temperatura_ano = (
        df_filtrado
        .groupby("ano")["temperatura_media"]
        .mean()
    )

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(
        temperatura_ano.index,
        temperatura_ano.values,
        marker="o"
    )

    ax.set_title(
        "Temperatura média ao longo do tempo"
    )

    ax.set_xlabel("Ano")
    ax.set_ylabel("Temperatura média (°C)")

    ax.grid(True)

    st.pyplot(fig)


# Chuva por ano
with col2:

    chuva_ano = (
        df_filtrado
        .groupby("ano")["chuva_mm"]
        .sum()
    )

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(
        chuva_ano.index,
        chuva_ano.values
    )

    ax.set_title(
        "Chuva total ao longo do tempo"
    )

    ax.set_xlabel("Ano")
    ax.set_ylabel("Chuva total (mm)")

    ax.grid(axis="y")

    st.pyplot(fig)


# =========================================================
# COMPARAÇÕES
# =========================================================

st.header("🌎 Comparações")

col1, col2 = st.columns(2)


# Temperatura por região
with col1:

    temperatura_regiao = (
        df_filtrado
        .groupby("regiao")["temperatura_media"]
        .mean()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(
        temperatura_regiao.index,
        temperatura_regiao.values
    )

    ax.set_title(
        "Temperatura média por região"
    )

    ax.set_xlabel("Região")
    ax.set_ylabel("Temperatura média (°C)")

    ax.tick_params(
        axis="x",
        rotation=30
    )

    ax.grid(axis="y")

    st.pyplot(fig)


# Chuva por estado
with col2:

    chuva_estado = (
        df_filtrado
        .groupby("uf")["chuva_mm"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(
        chuva_estado.index,
        chuva_estado.values
    )

    ax.set_title(
        "Volume de chuva por estado"
    )

    ax.set_xlabel("Estado")
    ax.set_ylabel("Chuva total (mm)")

    ax.tick_params(
        axis="x",
        rotation=45
    )

    ax.grid(axis="y")

    st.pyplot(fig)


# =========================================================
# EVENTOS EXTREMOS
# =========================================================

st.header("⚠️ Eventos extremos")

eventos_ano = (
    df_filtrado
    .groupby("ano")["eventos_extremos"]
    .sum()
)


fig, ax = plt.subplots(figsize=(10, 4))

ax.bar(
    eventos_ano.index,
    eventos_ano.values
)

ax.set_title(
    "Eventos extremos ao longo do tempo"
)

ax.set_xlabel("Ano")
ax.set_ylabel("Total de eventos extremos")

ax.grid(axis="y")

st.pyplot(fig)


# =========================================================
# ANÁLISE MENSAL
# =========================================================

st.header("📅 Análise mensal")

temperatura_mensal = (
    df_filtrado
    .pivot_table(
        values="temperatura_media",
        index="mes",
        columns="ano",
        aggfunc="mean"
    )
)

temperatura_mensal = temperatura_mensal.reindex(
    range(1, 13)
)

temperatura_mensal.index = [
    meses_nomes[numero]
    for numero in temperatura_mensal.index
]


fig, ax = plt.subplots(
    figsize=(12, 5)
)

sns.heatmap(
    temperatura_mensal,
    annot=True,
    fmt=".1f",
    ax=ax
)

ax.set_title(
    "Temperatura média por mês e ano"
)

ax.set_xlabel("Ano")
ax.set_ylabel("Mês")

st.pyplot(fig)


# =========================================================
# RELAÇÃO ENTRE TEMPERATURA E CHUVA
# =========================================================

st.header("🌡️ Relação entre temperatura e chuva")


fig, ax = plt.subplots(
    figsize=(10, 5)
)

ax.scatter(
    df_filtrado["temperatura_media"],
    df_filtrado["chuva_mm"],
    alpha=0.5,
    s=20
)

ax.set_title(
    "Relação entre temperatura média e chuva"
)

ax.set_xlabel(
    "Temperatura média (°C)"
)

ax.set_ylabel(
    "Chuva (mm)"
)

ax.grid(True)

st.pyplot(fig)


# =========================================================
# CORRELAÇÃO ESTATÍSTICA
# =========================================================

st.subheader(
    "Correlação entre temperatura e chuva"
)


correlacao = (
    df_filtrado["temperatura_media"]
    .corr(df_filtrado["chuva_mm"])
)


st.metric(
    "Correlação temperatura × chuva",
    f"{correlacao:.2f}"
)


if abs(correlacao) < 0.3:

    st.write(
        "A correlação indica uma relação linear fraca "
        "entre temperatura média e chuva."
    )

elif abs(correlacao) < 0.7:

    st.write(
        "A correlação indica uma relação linear moderada "
        "entre temperatura média e chuva."
    )

else:

    st.write(
        "A correlação indica uma relação linear forte "
        "entre temperatura média e chuva."
    )


# =========================================================
# SÉRIE TEMPORAL AVANÇADA
# =========================================================

st.header(
    "📊 Série temporal avançada"
)


serie_mensal = (
    df_filtrado
    .set_index("data")["temperatura_media"]
    .resample("MS")
    .mean()
)


media_movel = (
    serie_mensal
    .rolling(3)
    .mean()
)


fig, ax = plt.subplots(
    figsize=(12, 5)
)


ax.plot(
    serie_mensal.index,
    serie_mensal.values,
    label="Temperatura média mensal"
)


ax.plot(
    media_movel.index,
    media_movel.values,
    label="Média móvel de 3 meses"
)


ax.set_title(
    "Temperatura mensal e média móvel de 3 meses"
)

ax.set_xlabel("Período")

ax.set_ylabel(
    "Temperatura média (°C)"
)

ax.legend()

ax.grid(True)

st.pyplot(fig)


# =========================================================
# INTERPRETAÇÃO
# =========================================================

st.header(
    "📝 Interpretação dos resultados"
)


temperatura_ano = (
    df_filtrado
    .groupby("ano")["temperatura_media"]
    .mean()
)


chuva_ano = (
    df_filtrado
    .groupby("ano")["chuva_mm"]
    .sum()
)


eventos_ano = (
    df_filtrado
    .groupby("ano")["eventos_extremos"]
    .sum()
)


ano_mais_quente = (
    temperatura_ano.idxmax()
)


ano_mais_chuvoso = (
    chuva_ano.idxmax()
)


ano_mais_eventos = (
    eventos_ano.idxmax()
)


st.write(
    f"No período selecionado, o ano com maior temperatura "
    f"média foi **{ano_mais_quente}**."
)


st.write(
    f"O maior volume total de chuva foi registrado em "
    f"**{ano_mais_chuvoso}**."
)


st.write(
    f"O maior número de eventos extremos ocorreu em "
    f"**{ano_mais_eventos}**."
)


st.write(
    f"A cidade com maior temperatura média no período filtrado "
    f"foi **{cidade_mais_quente}**."
)


st.write(
    f"O estado com maior volume de chuva no período filtrado "
    f"foi **{estado_mais_chuvoso}**."
)


# =========================================================
# TABELA
# =========================================================

st.header(
    "📋 Tabela de dados"
)


st.write(
    "A tabela apresenta os registros correspondentes "
    "aos filtros selecionados."
)


st.dataframe(
    df_filtrado.head(100),
    use_container_width=True
)


# =========================================================
# DOWNLOAD
# =========================================================

csv_download = df_filtrado.to_csv(
    index=False
).encode("utf-8")


st.download_button(
    label="⬇️ Baixar dados filtrados",
    data=csv_download,
    file_name="dados_climaticos_filtrados.csv",
    mime="text/csv"
)


# =========================================================
# CONCLUSÃO EXECUTIVA
# =========================================================

st.header(
    "🎯 Conclusão executiva"
)


st.write(
    """
    A análise dos dados climáticos do Brasil entre 2015 e 2024
    permite observar variações de temperatura, chuva, umidade
    e eventos extremos ao longo do período.
    """
)


st.write(
    """
    Os filtros permitem comparar diferentes anos, meses, regiões,
    estados, cidades e níveis de alerta, facilitando a exploração
    dos dados.
    """
)


st.write(
    """
    Os indicadores e gráficos apresentados contribuem para a
    identificação de padrões temporais, diferenças regionais
    e relações entre as variáveis climáticas presentes na base.
    """
)