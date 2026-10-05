import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# LEITURA DOS DADOS
# =========================

df = pd.read_csv("dados/simulacao_clima_brasil(1).csv")

df["data"] = pd.to_datetime(df["data"])

# =========================
# TÍTULO E DESCRIÇÃO
# =========================

st.title("Dados Climáticos no Brasil")

st.write("**Disciplina:** Linguagem de Programação — Análise e Visualização de Dados com Python")
st.write("**Professor:** Alexandre Neves Louzada")
st.write("**Aluno:** Wilson da Silva Prata Junior")


st.write(
    "Este projeto apresenta uma análise dos dados climáticos do Brasil "
    "entre 2015 e 2024, considerando temperatura, chuva, umidade e "
    "eventos extremos."
)

# =========================
# FILTROS
# =========================

st.sidebar.header("Filtros")

anos = sorted(df["ano"].unique())
regioes = sorted(df["regiao"].unique())
estados = sorted(df["uf"].unique())
cidades = sorted(df["cidade"].unique())
alertas = sorted(df["nivel_alerta"].unique())

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

meses_opcoes = list(meses_nomes.values())

ano_selecionado = st.sidebar.multiselect(
    "Ano",
    anos,
    default=anos
)

mes_selecionado = st.sidebar.multiselect(
    "Mês",
    meses_opcoes,
    default=meses_opcoes
)

regiao_selecionada = st.sidebar.multiselect(
    "Região",
    regioes,
    default=regioes
)

estado_selecionado = st.sidebar.multiselect(
    "Estado",
    estados,
    default=estados
)

cidade_selecionada = st.sidebar.multiselect(
    "Cidade",
    cidades,
    default=cidades
)

alerta_selecionado = st.sidebar.multiselect(
    "Nível de alerta",
    alertas,
    default=alertas
)

meses_selecionados_num = [
    numero
    for numero, nome in meses_nomes.items()
    if nome in mes_selecionado
]

# =========================
# APLICAÇÃO DOS FILTROS
# =========================

df_filtrado = df[
    (df["ano"].isin(ano_selecionado)) &
    (df["mes"].isin(meses_selecionados_num)) &
    (df["regiao"].isin(regiao_selecionada)) &
    (df["uf"].isin(estado_selecionado)) &
    (df["cidade"].isin(cidade_selecionada)) &
    (df["nivel_alerta"].isin(alerta_selecionado))
].copy()

# =========================
# KPIs
# =========================

st.subheader("Indicadores climáticos")

if len(df_filtrado) > 0:

    temperatura_media = df_filtrado["temperatura_media"].mean()

    chuva_total = df_filtrado["chuva_mm"].sum()

    cidade_mais_quente = (
        df_filtrado.groupby("cidade")["temperatura_media"]
        .mean()
        .idxmax()
    )

    estado_mais_chuvoso = (
        df_filtrado.groupby("uf")["chuva_mm"]
        .sum()
        .idxmax()
    )

    total_eventos = df_filtrado["eventos_extremos"].sum()

    umidade_media = df_filtrado["umidade"].mean()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Temperatura média",
        f"{temperatura_media:.2f} °C"
    )

    col2.metric(
        "Chuva total",
        f"{chuva_total:,.2f} mm"
    )

    col3.metric(
        "Cidade mais quente",
        cidade_mais_quente
    )

    col4, col5, col6 = st.columns(3)

    col4.metric(
        "Estado mais chuvoso",
        estado_mais_chuvoso
    )

    col5.metric(
        "Eventos extremos",
        f"{total_eventos:,.0f}"
    )

    col6.metric(
        "Umidade média",
        f"{umidade_media:.2f}%"
    )

else:

    st.warning(
        "Nenhum registro encontrado para os filtros selecionados."
    )

# =========================
# TABELA
# =========================

st.subheader("Dados climáticos")

st.write(
    f"Registros encontrados: {len(df_filtrado)}"
)

st.dataframe(
    df_filtrado,
    use_container_width=True
)

# =========================
# GRÁFICO 1
# TEMPERATURA AO LONGO DO TEMPO
# =========================

st.subheader("Temperatura média ao longo do tempo")

if len(df_filtrado) > 0:

    temperatura_ano = (
        df_filtrado
        .groupby("ano")["temperatura_media"]
        .mean()
    )

    fig, ax = plt.subplots(figsize=(10, 5))

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

# =========================
# GRÁFICO 2
# CHUVA AO LONGO DO TEMPO
# =========================

st.subheader("Chuva total ao longo do tempo")

if len(df_filtrado) > 0:

    chuva_ano = (
        df_filtrado
        .groupby("ano")["chuva_mm"]
        .sum()
    )

    fig, ax = plt.subplots(figsize=(10, 5))

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

# =========================
# GRÁFICO 3
# CHUVA POR ESTADO
# =========================

st.subheader("Volume de chuva por estado")

if len(df_filtrado) > 0:

    chuva_estado = (
        df_filtrado
        .groupby("uf")["chuva_mm"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(12, 6))

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

# =========================
# GRÁFICO 4
# TEMPERATURA POR REGIÃO
# =========================

st.subheader("Temperatura média por região")

if len(df_filtrado) > 0:

    temperatura_regiao = (
        df_filtrado
        .groupby("regiao")["temperatura_media"]
        .mean()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(
        temperatura_regiao.index,
        temperatura_regiao.values
    )

    ax.set_title(
        "Temperatura média por região"
    )

    ax.set_xlabel("Região")
    ax.set_ylabel("Temperatura média (°C)")

    ax.grid(axis="y")

    st.pyplot(fig)

# =========================
# GRÁFICO 5
# EVENTOS EXTREMOS
# =========================

st.subheader("Eventos extremos ao longo do tempo")

if len(df_filtrado) > 0:

    eventos_ano = (
        df_filtrado
        .groupby("ano")["eventos_extremos"]
        .sum()
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(
        eventos_ano.index,
        eventos_ano.values
    )

    ax.set_title(
        "Eventos extremos ao longo do tempo"
    )

    ax.set_xlabel("Ano")
    ax.set_ylabel(
        "Total de eventos extremos"
    )

    ax.grid(axis="y")

    st.pyplot(fig)

# =========================
# GRÁFICO 6
# HEATMAP MENSAL
# =========================

st.subheader("Temperatura média por mês e ano")

if len(df_filtrado) > 0:

    temperatura_mensal = df_filtrado.pivot_table(
        values="temperatura_media",
        index="mes",
        columns="ano",
        aggfunc="mean"
    )

    temperatura_mensal = temperatura_mensal.reindex(
        range(1, 13)
    )

    temperatura_mensal.index = [
        meses_nomes[numero]
        for numero in temperatura_mensal.index
    ]

    fig, ax = plt.subplots(
        figsize=(12, 6)
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

# =========================
# GRÁFICO 7
# TEMPERATURA X CHUVA
# =========================

st.subheader(
    "Relação entre temperatura média e chuva"
)

if len(df_filtrado) > 0:

    fig, ax = plt.subplots(
        figsize=(10, 6)
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

# =========================
# ANÁLISE DE CORRELAÇÃO
# =========================

st.subheader("Correlação entre temperatura e chuva")

if len(df_filtrado) > 1:

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

# =========================
# ANÁLISE TEMPORAL AVANÇADA
# =========================

st.subheader(
    "Média móvel da temperatura"
)

if len(df_filtrado) > 0:

    serie_mensal = (
        df_filtrado
        .set_index("data")["temperatura_media"]
        .resample("MS")
        .mean()
    )

    media_movel = serie_mensal.rolling(
        3
    ).mean()

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
        "Evolução mensal da temperatura e média móvel"
    )

    ax.set_xlabel("Período")
    ax.set_ylabel(
        "Temperatura média (°C)"
    )

    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

# =========================
# INTERPRETAÇÃO
# =========================

st.subheader("Interpretação dos resultados")

if len(df_filtrado) > 0:

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

    ano_mais_quente = temperatura_ano.idxmax()
    ano_mais_chuvoso = chuva_ano.idxmax()
    ano_mais_eventos = eventos_ano.idxmax()

    st.write(
        f"No período selecionado, o ano com maior temperatura "
        f"média foi {ano_mais_quente}."
    )

    st.write(
        f"O maior volume total de chuva foi registrado em "
        f"{ano_mais_chuvoso}."
    )

    st.write(
        f"O maior número de eventos extremos ocorreu em "
        f"{ano_mais_eventos}."
    )

# =========================
# CONCLUSÃO EXECUTIVA
# =========================

st.subheader("Conclusão executiva")

st.write(
    "A análise dos dados climáticos permite observar variações "
    "de temperatura, chuva, umidade e eventos extremos ao longo "
    "do período analisado. Os filtros permitem comparar diferentes "
    "anos, meses, regiões, estados, cidades e níveis de alerta, "
    "facilitando a exploração dos dados."
)

st.write(
    "Os indicadores e gráficos apresentados ajudam a identificar "
    "padrões temporais, diferenças regionais e relações entre as "
    "variáveis climáticas presentes na base."
)