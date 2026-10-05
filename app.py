import os



import matplotlib.pyplot as plt

import numpy as np

import pandas as pd

import plotly.express as px

import plotly.graph_objects as go

import seaborn as sns

import streamlit as st

from matplotlib.colors import LinearSegmentedColormap





# ============================================================

# 1. CONFIGURAÇÃO DA PÁGINA

# ============================================================



st.set_page_config(

    page_title="Dados Climáticos no Brasil",

    page_icon="🌦️",

    layout="wide",

    initial_sidebar_state="expanded",

)





# ============================================================

# 2. CORES — para mudar a cor do dashboard, altere só aqui

# ============================================================



COR_PRIMARIA = "#0E7490"         # azul-petróleo: abas, bordas, botões, scatter

COR_PRIMARIA_ESCURA = "#0B4F6C"  # azul-marinho: topo do cabeçalho, hover, média móvel

COR_CLARA = "#A5D4E0"            # azul claro (apoio)

COR_TEMP = "#E8743B"             # temperatura  -> laranja

COR_CHUVA = "#2B7BBA"            # chuva        -> azul

COR_EVENTO = "#C0392B"           # eventos extremos -> vermelho

COR_DESTAQUE = COR_PRIMARIA_ESCURA





# ============================================================

# 3. ESTILO VISUAL

# ============================================================



CSS = """

<style>

.stApp { background: #f3f6f9; color: #18334a; }

header[data-testid="stHeader"] { background: #f3f6f9 !important; }

div[data-testid="stToolbar"] { background: transparent !important; }

.block-container { max-width: 1450px; padding-top: 3.8rem; padding-bottom: 3rem; }



/* SIDEBAR */

section[data-testid="stSidebar"] { background: #e8eff4; border-right: 1px solid #d3dde5; }

section[data-testid="stSidebar"] .sidebar-title {

    color: #18334a !important; font-size: 1.12rem; font-weight: 800; margin-bottom: 0.25rem;

}

section[data-testid="stSidebar"] .sidebar-caption {

    color: #5a6b79 !important; font-size: 0.82rem; line-height: 1.45; margin-bottom: 1rem;

}

section[data-testid="stSidebar"] .stSelectbox label { color: #18334a !important; font-weight: 700 !important; }

section[data-testid="stSidebar"] div[data-baseweb="select"] > div {

    background: #ffffff !important; border: 1px solid #c5d2dc !important; border-radius: 8px !important;

}

section[data-testid="stSidebar"] div[data-baseweb="select"] span { color: #18334a !important; }

section[data-testid="stSidebar"] div[data-baseweb="select"] svg { fill: #5a6b79 !important; }

section[data-testid="stSidebar"] [data-baseweb="popover"] { background: #ffffff !important; }



/* CABEÇALHO */

.dashboard-title { color: #10283c; font-size: 2.55rem; line-height: 1.15; font-weight: 800; margin-bottom: 0.3rem; }

.dashboard-subtitle { color: #5a6b79; font-size: 1rem; margin-bottom: 0.65rem; }

.academic-line { color: #3d5163; font-size: 0.86rem; line-height: 1.6; margin-bottom: 1rem; }

.intro-box {

    background: #ffffff; border: 1px solid #d3dde5; border-left: 4px solid __PRIM__;

    border-radius: 10px; padding: 0.95rem 1.15rem; color: #3d5163; margin-bottom: 1rem;

    box-shadow: 0 2px 8px rgba(35, 45, 39, 0.05);

}



/* BANNER */

.hero {

    background: linear-gradient(120deg, __ESC__ 0%, __PRIM__ 100%);

    border-radius: 14px; padding: 1.7rem 2rem; margin-bottom: 1.1rem;

    box-shadow: 0 6px 18px rgba(11, 79, 108, 0.25);

}

.hero .hero-kicker {

    display: inline-block; background: rgba(255, 255, 255, 0.18); color: #ffffff;

    font-size: 0.78rem; font-weight: 800; letter-spacing: 0.12em;

    padding: 0.25rem 0.75rem; border-radius: 999px; margin-bottom: 0.7rem;

}

.hero .dashboard-title { color: #ffffff; }

.hero .dashboard-subtitle { color: #ffffff; opacity: 0.92; font-size: 1.05rem; }

.hero .academic-line {

    color: #ffffff; font-size: 0.95rem; margin: 0.9rem 0 0 0; padding-top: 0.8rem;

    border-top: 1px solid rgba(255, 255, 255, 0.28);

}



.hero .hero-stats { display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 1rem; }

.hero .hero-stat {

    background: rgba(255, 255, 255, 0.14); border: 1px solid rgba(255, 255, 255, 0.22);

    border-radius: 10px; padding: 0.55rem 1rem; min-width: 112px;

}

.hero .hero-stat b { display: block; color: #ffffff; font-size: 1.25rem; font-weight: 800; line-height: 1.2; }

.hero .hero-stat span {

    color: #e3f3f8; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 700;

}



/* CARTÕES DE DESTAQUE */

.insight {

    background: #ffffff; border: 1px solid #d3dde5; border-radius: 12px; padding: 1rem 1.1rem;

    box-shadow: 0 3px 12px rgba(16, 40, 60, 0.07); min-height: 150px;

}

.insight .i-label { font-size: 0.72rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em; color: #5a6b79; }

.insight .i-value { font-size: 1.6rem; font-weight: 800; line-height: 1.2; margin: 0.35rem 0; }

.insight .i-note { font-size: 0.82rem; line-height: 1.4; color: #5a6b79; }

.conclusao {

    background: #ffffff; border: 1px solid #d3dde5; border-top: 4px solid __PRIM__; border-radius: 12px;

    padding: 1.1rem 1.2rem; box-shadow: 0 3px 12px rgba(16, 40, 60, 0.07); min-height: 200px;

}

.conclusao .c-titulo { color: __PRIM__; font-size: 0.78rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.5rem; }

.conclusao .c-texto { color: #3d5163; font-size: 0.95rem; line-height: 1.6; }



/* EFEITO AO PASSAR O MOUSE */

.insight, .conclusao, div[data-testid="stMetric"], .stPlotlyChart {

    position: relative;

    transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;

}

/* área invisível sob o cartão: evita "tremer" quando o mouse está na borda de baixo */

.insight::after, .conclusao::after, div[data-testid="stMetric"]::after {

    content: ""; position: absolute; left: 0; right: 0; bottom: -6px; height: 6px;

}

.insight:hover, .conclusao:hover, div[data-testid="stMetric"]:hover {

    transform: translateY(-4px);

    box-shadow: 0 12px 26px rgba(16, 40, 60, 0.16);

    border-color: __PRIM__;

}

/* gráficos só ganham destaque (sem subir, para não atrapalhar o zoom e o tooltip) */

.stPlotlyChart:hover {

    box-shadow: 0 8px 22px rgba(16, 40, 60, 0.14) !important;

    border-color: __PRIM__ !important;

}



div[data-testid="stImage"] img {

    background: #ffffff; border: 1px solid #d3dde5; border-radius: 10px; padding: 8px;

    box-shadow: 0 3px 12px rgba(16, 40, 60, 0.07);

}



/* SEÇÕES */

.section-kicker {

    color: __PRIM__; font-size: 0.75rem; font-weight: 800; text-transform: uppercase;

    letter-spacing: 0.1em; margin-top: 0.4rem;

}

.section-heading { margin-top: 0.5rem; color: #18334a; font-size: 1.4rem; font-weight: 800; margin-bottom: 0.75rem; }

h1, h2, h3, h4 { color: #18334a !important; }

p, li { color: #3d5163; }

.stCaption { color: #5a6b79 !important; }

hr { border-color: #d3dde5; }



/* KPIs */

div[data-testid="stMetric"] {

    background: #ffffff; border: 1px solid #d3dde5; border-top: 3px solid __PRIM__;

    border-radius: 10px; padding: 15px; box-shadow: 0 3px 10px rgba(35, 45, 39, 0.06); min-height: 108px;

}

div[data-testid="stMetric"] label {

    color: #5a6b79 !important; font-size: 0.74rem !important; font-weight: 800 !important;

    text-transform: uppercase; letter-spacing: 0.04em;

}

div[data-testid="stMetric"] div[data-testid="stMetricValue"] {

    color: #18334a !important; font-size: 1.42rem !important; font-weight: 800 !important;

}



/* ABAS */

.stTabs [data-baseweb="tab-list"] {
    display: flex;
    gap: 12px;
    background: transparent;
    padding: 8px 2px 12px 2px;
    border: none;
    overflow-x: auto;
}

.stTabs [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-border"] {
    display: none !important;
}

.stTabs [data-baseweb="tab"],
.stTabs [role="tab"] {
    min-height: 48px !important;
    background: #ffffff !important;
    border: 1px solid #d3dde5 !important;
    border-top: 4px solid __PRIM__ !important;
    border-radius: 10px !important;
    color: #35566b !important;
    padding: 8px 16px !important;
    font-weight: 700 !important;
    box-shadow: 0 3px 12px rgba(16, 40, 60, 0.07);
    transition: transform 0.18s ease, box-shadow 0.18s ease,
                border-color 0.18s ease, background 0.18s ease;
}

.stTabs [data-baseweb="tab"] p,
.stTabs [role="tab"] p {
    color: #35566b !important;
    font-weight: 700 !important;
}

.stTabs [data-baseweb="tab"]:hover,
.stTabs [role="tab"]:hover {
    transform: translateY(-3px);
    background: #f2fafc !important;
    border-color: __PRIM__ !important;
    border-top-color: __PRIM__ !important;
    box-shadow: 0 10px 22px rgba(16, 40, 60, 0.14);
    cursor: pointer;
}

.stTabs [data-baseweb="tab"][aria-selected="true"],
.stTabs [role="tab"][aria-selected="true"] {
    background: __PRIM__ !important;
    border-color: __PRIM__ !important;
    border-top-color: __PRIM__ !important;
    color: #ffffff !important;
    box-shadow: 0 6px 16px rgba(14, 116, 144, 0.20);
}

.stTabs [data-baseweb="tab"][aria-selected="true"] p,
.stTabs [role="tab"][aria-selected="true"] p {
    color: #ffffff !important;
}

.stTabs [data-baseweb="tab-panel"] {
    margin-top: 8px;
    padding-top: 4px;
}

/* GRÁFICOS */

.stPlotlyChart {

    background: #ffffff !important; border: 1px solid #d3dde5 !important; border-radius: 10px;

    padding: 8px; box-shadow: 0 3px 12px rgba(35, 45, 39, 0.07);

}



/* TABELA */

div[data-testid="stDataFrame"] { border: 1px solid #d3dde5; border-radius: 10px; background: #ffffff; }



/* CONTAINERS DE INTERPRETAÇÃO E CONCLUSÃO */

div[data-testid="stVerticalBlockBorderWrapper"] {

    background: #ffffff; border: 1px solid #d3dde5; border-left: 4px solid __PRIM__;

    border-radius: 10px; box-shadow: 0 2px 8px rgba(35, 45, 39, 0.05);

}



.stDownloadButton button {

    background: __PRIM__; color: #ffffff; border: 1px solid __ESC__; border-radius: 8px; font-weight: 700;

}

.stDownloadButton button:hover { background: __ESC__; color: #ffffff; }

</style>

"""



st.markdown(

    CSS.replace("__PRIM__", COR_PRIMARIA).replace("__ESC__", COR_PRIMARIA_ESCURA),

    unsafe_allow_html=True,

)





def html(texto):

    st.markdown(texto, unsafe_allow_html=True)





# ============================================================

# 4. CAMINHO DA BASE

# ============================================================



PASTA_DADOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dados")



CAMINHO_DADOS = None

for nome_arquivo in ("simulacao_clima_brasil.csv", "simulacao_clima_brasil(1).csv"):

    candidato = os.path.join(PASTA_DADOS, nome_arquivo)

    if os.path.exists(candidato):

        CAMINHO_DADOS = candidato

        break



if CAMINHO_DADOS is None:

    st.error("Arquivo da base não encontrado na pasta 'dados'.")

    st.stop()





# ============================================================

# 5. LEITURA E PREPARAÇÃO DOS DADOS

# ============================================================



MESES_ORDEM = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]





@st.cache_data

def carregar_dados(caminho):

    df = pd.read_csv(caminho)



    df["data"] = pd.to_datetime(df["data"], errors="coerce")

    df = df.dropna(subset=["data"]).copy()  # datas inválidas quebrariam o resample



    df["ano"] = df["data"].dt.year

    df["mes_numero"] = df["data"].dt.month

    df["mes_nome"] = df["mes_numero"].map(dict(enumerate(MESES_ORDEM, start=1)))



    df["estacao"] = df["mes_numero"].map(

        {

            12: "Verão", 1: "Verão", 2: "Verão",

            3: "Outono", 4: "Outono", 5: "Outono",

            6: "Inverno", 7: "Inverno", 8: "Inverno",

            9: "Primavera", 10: "Primavera", 11: "Primavera",

        }

    )

    return df





df = carregar_dados(CAMINHO_DADOS)





# ============================================================

# 6. BARRA LATERAL — FILTROS (região → estado → cidade em cascata)

# ============================================================



st.sidebar.markdown(

    '<div class="sidebar-title">🔎 Filtros de pesquisa</div>',

    unsafe_allow_html=True,

)

st.sidebar.markdown(

    '<div class="sidebar-caption">Selecione os critérios para explorar os dados climáticos.</div>',

    unsafe_allow_html=True,

)



anos = sorted(df["ano"].dropna().unique().astype(int))

ano_filtro = st.sidebar.selectbox("Ano", ["Todos"] + anos)

mes_filtro = st.sidebar.selectbox("Mês", ["Todos"] + MESES_ORDEM)



regioes = sorted(df["regiao"].dropna().unique())

regiao_filtro = st.sidebar.selectbox("Região", ["Todas"] + regioes)

base_regiao = df if regiao_filtro == "Todas" else df[df["regiao"] == regiao_filtro]



estados = sorted(base_regiao["uf"].dropna().unique())

estado_filtro = st.sidebar.selectbox("Estado", ["Todos"] + estados)

base_estado = base_regiao if estado_filtro == "Todos" else base_regiao[base_regiao["uf"] == estado_filtro]



cidades = sorted(base_estado["cidade"].dropna().unique())

cidade_filtro = st.sidebar.selectbox("Cidade", ["Todas"] + cidades)



alertas = sorted(df["nivel_alerta"].dropna().unique())

alerta_filtro = st.sidebar.selectbox("Nível de alerta", ["Todos"] + alertas)





# ============================================================

# 7. APLICAÇÃO DOS FILTROS

# ============================================================



df_filtrado = df.copy()



if ano_filtro != "Todos":

    df_filtrado = df_filtrado[df_filtrado["ano"] == ano_filtro]

if mes_filtro != "Todos":

    df_filtrado = df_filtrado[df_filtrado["mes_nome"] == mes_filtro]

if regiao_filtro != "Todas":

    df_filtrado = df_filtrado[df_filtrado["regiao"] == regiao_filtro]

if estado_filtro != "Todos":

    df_filtrado = df_filtrado[df_filtrado["uf"] == estado_filtro]

if cidade_filtro != "Todas":

    df_filtrado = df_filtrado[df_filtrado["cidade"] == cidade_filtro]

if alerta_filtro != "Todos":

    df_filtrado = df_filtrado[df_filtrado["nivel_alerta"] == alerta_filtro]



if df_filtrado.empty:

    st.warning(

        "Nenhum registro encontrado com os filtros selecionados. "

        "Ajuste os filtros na barra lateral."

    )

    st.stop()





# ============================================================

# 8. CABEÇALHO PRINCIPAL

# ============================================================



stats = [

    (f"{len(df_filtrado):,}".replace(",", "."), "registros"),

    (df_filtrado["cidade"].nunique(), "cidades"),

    (df_filtrado["uf"].nunique(), "estados"),

]

stats_html = "".join(f'<div class="hero-stat"><b>{v}</b><span>{r}</span></div>' for v, r in stats)



html(

    '<div class="hero">'

    '<div class="hero-kicker">PAINEL DE ANÁLISE</div>'

    '<div class="dashboard-title">🌦️ Dados Climáticos no Brasil</div>'

    '<div class="dashboard-subtitle">Análise de dados climáticos simulados do Brasil — período de 2015 a 2024</div>'

    '<div class="academic-line">🎓 Linguagem de Programação — Análise e Visualização de Dados com Python '

    '&nbsp; | &nbsp; 👨‍🏫 Prof. Alexandre Neves Louzada &nbsp; | &nbsp; 👤 Wilson da Silva Prata Junior</div>'

    f'<div class="hero-stats">{stats_html}</div>'

    '</div>'

)

html(

    '<div class="intro-box">Este dashboard apresenta uma análise de dados climáticos simulados do Brasil, '

    "considerando temperatura, chuva, umidade, velocidade do vento, eventos extremos e níveis de alerta. Eventos extremos e mudanças climáticas impactam agricultura, abastecimento de água, energia, saúde pública e qualidade de vida; monitorar indicadores ajuda a identificar padrões, períodos críticos e tendências.</div>"

)







# ============================================================

# 9. KPIs

# ============================================================



html('<div class="section-heading">Principais indicadores climáticos</div>')



temperatura_media = df_filtrado["temperatura_media"].mean()

chuva_total = df_filtrado["chuva_mm"].sum()

chuva_media = df_filtrado["chuva_mm"].mean()

cidade_mais_quente = df_filtrado.groupby("cidade")["temperatura_media"].mean().idxmax()

estado_mais_chuvoso = df_filtrado.groupby("uf")["chuva_mm"].sum().idxmax()

estado_chuva_media = df_filtrado.groupby("uf")["chuva_mm"].mean().idxmax()

total_eventos = df_filtrado["eventos_extremos"].sum()

umidade_media = df_filtrado["umidade"].mean()



k1, k2, k3 = st.columns(3)

filtrado = len(df_filtrado) != len(df)





def delta_texto(valor, media_brasil, unidade):

    if not filtrado:

        return None

    return f"{valor - media_brasil:+.2f}".replace(".", ",") + f" {unidade} vs. média Brasil"





k1.metric(

    "🌡️ Temperatura média",

    f"{temperatura_media:.2f} °C",

    delta=delta_texto(temperatura_media, df["temperatura_media"].mean(), "°C"),

    delta_color="off",

)

k2.metric(

    "🌧️ Volume total de chuva",

    f"{chuva_total:,.2f} mm".replace(",", "X").replace(".", ",").replace("X", "."),

    help="Soma geral da chuva no período filtrado. Média mensal por registro: "

    + f"{chuva_media:.1f} mm.".replace(".", ","),

)

k3.metric("🔥 Cidade mais quente", cidade_mais_quente)



k4, k5, k6 = st.columns(3)

k4.metric(

    "💧 Estado mais chuvoso",

    estado_mais_chuvoso,

    help="Maior soma de chuva. Estados com mais cidades na base somam mais; "

    f"pela média mensal por registro, o líder é {estado_chuva_media}.",

)

k5.metric("⚠️ Eventos extremos", f"{total_eventos:,.0f}".replace(",", "."))

k6.metric(

    "💨 Umidade média",

    f"{umidade_media:.2f}%",

    delta=delta_texto(umidade_media, df["umidade"].mean(), "p.p."),

    delta_color="off",

)





# ============================================================

# 10. FUNÇÕES DE GRÁFICO

# ============================================================



P90_CHUVA = df["chuva_mm"].quantile(0.90)





def indice_vulnerabilidade(d):

    """Média de 3 razões em relação ao Brasil (1,00 = média nacional)."""

    g = d.groupby("regiao")

    tabela = pd.DataFrame(

        {

            "Eventos extremos (média)": g["eventos_extremos"].mean(),

            "% em alerta Alto/Crítico": g["nivel_alerta"].apply(lambda x: x.isin(["Alto", "Crítico"]).mean() * 100),

            "% com chuva intensa": g["chuva_mm"].apply(lambda x: (x >= P90_CHUVA).mean() * 100),

        }

    )

    base = pd.Series(

        {

            "Eventos extremos (média)": df["eventos_extremos"].mean(),

            "% em alerta Alto/Crítico": df["nivel_alerta"].isin(["Alto", "Crítico"]).mean() * 100,

            "% com chuva intensa": (df["chuva_mm"] >= P90_CHUVA).mean() * 100,

        }

    )

    tabela["Índice"] = (tabela / base).mean(axis=1)

    return tabela.sort_values("Índice")





def br(valor, casas=2):

    return f"{valor:.{casas}f}".replace(".", ",")





def clarear(hex_cor, fator=0.6):

    r, g, b = (int(hex_cor[i:i + 2], 16) for i in (1, 3, 5))

    return "#%02x%02x%02x" % tuple(int(c + (255 - c) * fator) for c in (r, g, b))





def fmt_num(v):

    texto = f"{v:,.0f}" if abs(v) >= 100 else f"{v:,.1f}"

    return texto.replace(",", "X").replace(".", ",").replace("X", ".")





def destacar_maximo(fig, cor):

    """Barra de maior valor na cor cheia e rotulada; as demais em tom claro."""

    for tr in fig.data:

        if tr.type != "bar":

            continue

        valores = list(tr.x if tr.orientation == "h" else tr.y)

        if max(valores) - min(valores) <= 0.15 * max(valores):

            continue  # diferença pequena: destacar o máximo exageraria o que pode ser ruído

        i = valores.index(max(valores))

        tr.marker.color = [cor if k == i else clarear(cor) for k in range(len(valores))]

        tr.text = [fmt_num(v) if k == i else "" for k, v in enumerate(valores)]

        tr.textposition = "outside"

        tr.cliponaxis = False





def estilizar_grafico(fig, cor_unica=True, cor=COR_PRIMARIA):

    eixo = dict(

        gridcolor="#e3e9ee",

        zerolinecolor="#cfd8df",

        linecolor="#cfd8df",

        tickfont=dict(color="#5a6b79"),

        title_font=dict(color="#5a6b79"),

    )

    fig.update_layout(

        template="plotly_white",

        paper_bgcolor="#ffffff",

        plot_bgcolor="#ffffff",

        font=dict(color="#3d5163", size=12),

        title=dict(font=dict(color="#18334a", size=16)),

        margin=dict(l=55, r=25, t=65, b=50),

        xaxis=eixo,

        yaxis=eixo,

        legend=dict(bgcolor="rgba(255,255,255,0.9)", font=dict(color="#3d5163")),

    )



    # cor_unica=False é usado quando o gráfico tem várias séries

    # que precisam de cores diferentes (ex.: média móvel).

    if cor_unica:

        fig.update_traces(marker_color=cor, selector=dict(type="bar"))

        fig.update_traces(

            marker_color=cor,

            line=dict(color=cor),

            selector=dict(type="scatter"),

        )

    return fig





def mostrar(fig, altura, cor_unica=True, cor=COR_PRIMARIA):

    fig.update_layout(
        height=altura,
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="#ffffff",
            bordercolor=COR_PRIMARIA,
            font=dict(color="#18334a", size=12),
        ),
    )

    estilizar_grafico(fig, cor_unica, cor)

    if cor_unica:

        destacar_maximo(fig, cor)

    st.plotly_chart(fig, use_container_width=True)





# ============================================================

# 11. ANÁLISES

# ============================================================



st.markdown("---")



tab_temporal, tab_comparacoes, tab_sazonal, tab_relacoes, tab_alertas, tab_dados = st.tabs(

    [

        "📈 Análise temporal",

        "🌎 Comparações",

        "📅 Análise sazonal",

        "🌡️ Relações climáticas",

        "🚨 Alertas, vento e umidade",

        "📋 Base de dados",

    ]

)





# ---------- 11.1 ANÁLISE TEMPORAL ----------



with tab_temporal:

    st.subheader("Evolução dos indicadores ao longo do tempo")



    temperatura_ano = df_filtrado.groupby("ano", as_index=False)["temperatura_media"].mean()

    chuva_por_ano = df_filtrado.groupby("ano", as_index=False)["chuva_mm"].mean()

    eventos_por_ano = df_filtrado.groupby("ano", as_index=False)["eventos_extremos"].sum()



    col_a, col_b = st.columns(2)



    with col_a:

        fig = px.line(

            temperatura_ano, x="ano", y="temperatura_media", markers=True,

            title="Temperatura média ao longo do tempo",

            labels={"ano": "Ano", "temperatura_media": "Temperatura média (°C)"},

        )

        fig.add_hline(

            y=temperatura_ano["temperatura_media"].mean(),

            line_dash="dot", line_color="#5a6b79",

            annotation_text="Média do período", annotation_position="bottom right",

        )

        mostrar(fig, 360, cor=COR_TEMP)

        amplitude = temperatura_ano["temperatura_media"].agg(["min", "max"])

        texto_tendencia = ""

        if len(temperatura_ano) > 1:

            inclinacao = np.polyfit(temperatura_ano["ano"], temperatura_ano["temperatura_media"], 1)[0]

            texto_tendencia = f" Tendência linear: {br(inclinacao, 3).replace('-', '−') if inclinacao < 0 else '+' + br(inclinacao, 3)} °C por ano."

        st.caption(

            f"⚠️ Eixo vertical ampliado: a variação entre os anos é de apenas "

            f"{br(amplitude['max'] - amplitude['min'])} °C." + texto_tendencia

        )



    with col_b:

        fig = px.bar(

            chuva_por_ano, x="ano", y="chuva_mm",

            title="Chuva média mensal por ano",

            labels={"ano": "Ano", "chuva_mm": "Chuva média mensal (mm)"},

        )

        mostrar(fig, 360, cor=COR_CHUVA)



    fig = px.bar(

        eventos_por_ano, x="ano", y="eventos_extremos",

        title="Eventos extremos ao longo do tempo",

        labels={"ano": "Ano", "eventos_extremos": "Total de eventos extremos"},

    )

    mostrar(fig, 360, cor=COR_EVENTO)





# ---------- 11.2 COMPARAÇÕES ----------



with tab_comparacoes:

    col_a, col_b = st.columns(2)



    with col_a:

        modo_chuva = st.radio(

            "Medida", ["Volume total", "Média mensal por registro"], horizontal=True, key="modo_chuva"

        )

        agregacao = "sum" if modo_chuva == "Volume total" else "mean"

        chuva_estado = (

            df_filtrado.groupby("uf", as_index=False)["chuva_mm"].agg(agregacao)

            .sort_values("chuva_mm", ascending=True)

        )

        fig = px.bar(

            chuva_estado, x="chuva_mm", y="uf", orientation="h",

            title=f"Chuva por estado ({modo_chuva.lower()})",

            labels={"uf": "Estado", "chuva_mm": "Chuva (mm)"},

        )

        mostrar(fig, 470, cor=COR_CHUVA)



    with col_b:

        temperatura_regiao = (

            df_filtrado.groupby("regiao", as_index=False)["temperatura_media"].mean()

            .sort_values("temperatura_media", ascending=True)

        )

        fig = px.bar(

            temperatura_regiao, x="temperatura_media", y="regiao", orientation="h",

            title="Temperatura média por região",

            labels={"regiao": "Região", "temperatura_media": "Temperatura média (°C)"},

        )

        mostrar(fig, 470, cor=COR_TEMP)



    eventos_regiao = (

        df_filtrado.groupby("regiao", as_index=False)["eventos_extremos"].mean()

        .sort_values("eventos_extremos", ascending=False)

    )

    fig = px.bar(

        eventos_regiao, x="regiao", y="eventos_extremos",

        title="Eventos extremos médios por cidade/mês, por região",

        labels={"regiao": "Região", "eventos_extremos": "Média de eventos extremos"},

    )

    mostrar(fig, 360, cor=COR_EVENTO)





    st.subheader("Vulnerabilidade climática por região")

    vulnerab = indice_vulnerabilidade(df_filtrado).reset_index()

    fig = px.bar(

        vulnerab, x="Índice", y="regiao", orientation="h",

        title="Índice de vulnerabilidade climática (1,00 = média do Brasil)",

        labels={"regiao": "Região"},

    )

    fig.add_vline(x=1, line_dash="dot", line_color="#5a6b79", annotation_text="Média do Brasil")

    mostrar(fig, 360, cor=COR_EVENTO)

    st.caption(

        "Índice próprio: média de três razões em relação ao Brasil — eventos extremos médios, % de registros em "

        "alerta Alto/Crítico e % com chuva intensa (≥ P90). Acima de 1,00 = vulnerabilidade acima da média nacional."

    )





# ---------- 11.3 ANÁLISE SAZONAL ----------



with tab_sazonal:

    tabela_mensal = df_filtrado.pivot_table(

        values="temperatura_media", index="mes_numero", columns="ano", aggfunc="mean"

    )

    tabela_mensal.index = [MESES_ORDEM[i - 1] for i in tabela_mensal.index]



    fig = px.imshow(

        tabela_mensal, text_auto=".1f", aspect="auto",

        color_continuous_scale=["#fdf3e9", "#f4b183", COR_TEMP],

        labels={"x": "Ano", "y": "Mês", "color": "Temperatura (°C)"},

        title="Temperatura média por mês e ano",

    )

    mostrar(fig, 520)



    ordem_estacoes = ["Verão", "Outono", "Inverno", "Primavera"]

    temperatura_estacao = df_filtrado.groupby("estacao", as_index=False)["temperatura_media"].mean()

    temperatura_estacao["ordem"] = temperatura_estacao["estacao"].map(

        {valor: indice for indice, valor in enumerate(ordem_estacoes)}

    )

    temperatura_estacao = temperatura_estacao.sort_values("ordem")



    fig = px.bar(

        temperatura_estacao, x="estacao", y="temperatura_media",

        title="Temperatura média por estação",

        labels={"estacao": "Estação", "temperatura_media": "Temperatura média (°C)"},

    )

    mostrar(fig, 360, cor=COR_TEMP)





    st.subheader("Períodos de seca e de chuva intensa")

    p10 = df["chuva_mm"].quantile(0.10)

    extremos_mes = (

        df_filtrado.assign(Seca=df_filtrado["chuva_mm"] <= p10, **{"Chuva intensa": df_filtrado["chuva_mm"] >= P90_CHUVA})

        .groupby("mes_numero")[["Seca", "Chuva intensa"]].mean().mul(100)

    )

    extremos_mes.index = [MESES_ORDEM[i - 1] for i in extremos_mes.index]

    fig = px.bar(

        extremos_mes, barmode="group",

        color_discrete_map={"Seca": COR_TEMP, "Chuva intensa": COR_CHUVA},

        title="Registros em seca e em chuva intensa, por mês do ano",

        labels={"value": "% dos registros", "index": "Mês", "variable": "Situação"},

    )

    mostrar(fig, 380, cor_unica=False)

    st.caption(

        f"Seca: chuva mensal ≤ {br(p10, 1)} mm (10% menores valores da base). Chuva intensa: ≥ {br(P90_CHUVA, 1)} mm "

        "(10% maiores). Perto de 10% em todos os meses indica que não há estação seca ou chuvosa definida."

    )





# ---------- 11.4 RELAÇÕES CLIMÁTICAS ----------



with tab_relacoes:

    col_a, col_b = st.columns([2, 1])



    with col_a:

        fig = px.scatter(

            df_filtrado, x="temperatura_media", y="chuva_mm", opacity=0.45,

            title="Relação entre temperatura média e chuva",

            labels={"temperatura_media": "Temperatura média (°C)", "chuva_mm": "Chuva (mm)"},

        )

        mostrar(fig, 420)



    with col_b:

        correlacao = df_filtrado["temperatura_media"].corr(df_filtrado["chuva_mm"])



        if pd.isna(correlacao):

            # Poucos registros ou valores constantes: não dá para calcular.

            st.metric("Correlação temperatura × chuva", "—")

            st.info("Não há dados suficientes para calcular a correlação com os filtros atuais.")

        else:

            st.metric("Correlação temperatura × chuva", f"{correlacao:.2f}")

            if abs(correlacao) < 0.3:

                forca = "fraca"

            elif abs(correlacao) < 0.7:

                forca = "moderada"

            else:

                forca = "forte"

            st.info(
                f"Interpretação: a correlação é {correlacao:.2f}, indicando uma relação linear {forca} "
                "entre temperatura média e chuva na seleção atual."
            )



    st.subheader("Série temporal avançada")



    serie = df_filtrado.set_index("data")["temperatura_media"].resample("MS").mean().dropna()

    media_movel = serie.rolling(3).mean()



    sdf = pd.DataFrame(

        {"Temperatura média mensal": serie, "Média móvel de 3 meses": media_movel}

    ).reset_index()



    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=sdf["data"], y=sdf["Temperatura média mensal"],

            mode="lines", name="Temperatura média mensal",

            line=dict(color=COR_TEMP),

        )

    )

    fig.add_trace(

        go.Scatter(

            x=sdf["data"], y=sdf["Média móvel de 3 meses"],

            mode="lines", name="Média móvel de 3 meses",

            line=dict(color=COR_DESTAQUE, dash="dash"),

        )

    )

    fig.update_layout(

        title="Temperatura mensal e média móvel de 3 meses",

        xaxis_title="Período",

        yaxis_title="Temperatura média (°C)",

    )

    mostrar(fig, 420, cor_unica=False)





    st.subheader("Matriz de correlação")



    variaveis = {

        "temperatura_media": "Temperatura", "chuva_mm": "Chuva", "umidade": "Umidade",

        "velocidade_vento": "Vento", "eventos_extremos": "Eventos extremos",

    }

    matriz = df_filtrado[list(variaveis)].corr().rename(index=variaveis, columns=variaveis)

    fig_c, ax = plt.subplots(figsize=(8, 4.6))

    sns.heatmap(

        matriz, annot=True, fmt=".2f", vmin=-1, vmax=1, linewidths=0.6, linecolor="#ffffff",

        cmap=LinearSegmentedColormap.from_list("corr", [COR_TEMP, "#ffffff", COR_PRIMARIA]),

        cbar_kws={"label": "Correlação"}, ax=ax,

    )

    ax.set_title("Correlação entre as variáveis climáticas", loc="left", fontsize=13, color="#18334a")

    st.pyplot(fig_c)

    plt.close(fig_c)

    st.caption("Valores próximos de 0 indicam ausência de relação linear; correlação não implica causalidade.")



    st.subheader("Temperatura e eventos extremos")

    fig = px.box(

        df_filtrado, x="eventos_extremos", y="temperatura_media",

        title="Temperatura média segundo a quantidade de eventos extremos",

        labels={"eventos_extremos": "Eventos extremos no registro", "temperatura_media": "Temperatura média (°C)"},

    )

    fig.update_xaxes(type="category", categoryorder="category ascending")

    fig.update_traces(marker_color=COR_EVENTO, line_color=COR_EVENTO)

    mostrar(fig, 400, cor_unica=False)

# ---------- 11.5 ALERTAS, VENTO E UMIDADE ----------



ORDEM_ALERTA = ["Baixo", "Médio", "Alto", "Crítico"]

CORES_ALERTA = {"Baixo": COR_CLARA, "Médio": "#F2C14E", "Alto": COR_TEMP, "Crítico": COR_EVENTO}



with tab_alertas:

    c1, c2 = st.columns(2)



    with c1:

        dist = (

            df_filtrado.groupby("nivel_alerta").size().reindex(ORDEM_ALERTA).dropna()

            .rename("registros").rename_axis("nivel_alerta").reset_index()

        )

        fig = px.bar(

            dist, x="nivel_alerta", y="registros", color="nivel_alerta",

            color_discrete_map=CORES_ALERTA, text_auto=True,

            title="Registros por nível de alerta",

            labels={"nivel_alerta": "Nível de alerta", "registros": "Registros"},

        )

        fig.update_layout(showlegend=False)

        mostrar(fig, 380, cor_unica=False)



    with c2:

        ev = (

            df_filtrado.groupby("nivel_alerta")["eventos_extremos"].mean().reindex(ORDEM_ALERTA).dropna()

            .rename("media").rename_axis("nivel_alerta").reset_index()

        )

        fig = px.bar(

            ev, x="nivel_alerta", y="media", color="nivel_alerta",

            color_discrete_map=CORES_ALERTA, text_auto=".2f",

            title="Eventos extremos médios por nível de alerta",

            labels={"nivel_alerta": "Nível de alerta", "media": "Eventos extremos (média)"},

        )

        fig.update_layout(showlegend=False)

        mostrar(fig, 380, cor_unica=False)



    c3, c4 = st.columns(2)



    for coluna, (variavel, nome, cor) in zip(

        (c3, c4),

        [("velocidade_vento", "Velocidade do vento", COR_PRIMARIA), ("umidade", "Umidade (%)", COR_CHUVA)],

    ):

        with coluna:

            fig = px.box(

                df_filtrado, x="regiao", y=variavel, points=False,

                title=f"{nome} por região",

                labels={"regiao": "Região", variavel: nome},

            )

            fig.update_traces(marker_color=cor, line_color=cor)

            mostrar(fig, 400, cor_unica=False)





# ---------- 11.6 BASE DE DADOS ----------



with tab_dados:

    st.subheader("Tabela dinâmica")

    p1, p2, p3, p4 = st.columns(4)

    linhas = p1.selectbox("Linhas", ["regiao", "uf", "cidade", "ano", "estacao", "nivel_alerta"])

    colunas_pv = p2.selectbox("Colunas", ["ano", "estacao", "regiao", "nivel_alerta"])

    valor_pv = p3.selectbox("Valor", ["temperatura_media", "chuva_mm", "umidade", "velocidade_vento", "eventos_extremos"])

    agregacao_pv = p4.selectbox("Agregação", ["mean", "sum", "max", "min", "count"])

    if linhas == colunas_pv:

        st.info("Escolha dimensões diferentes para linhas e colunas.")

    else:

        pivo = df_filtrado.pivot_table(index=linhas, columns=colunas_pv, values=valor_pv, aggfunc=agregacao_pv)

        st.dataframe(pivo.round(2), use_container_width=True)



    st.subheader("Exploração dos dados filtrados")



    colunas = [

        "ano", "mes", "data", "regiao", "uf", "cidade",

        "temperatura_media", "temperatura_maxima", "temperatura_minima",

        "chuva_mm", "umidade", "velocidade_vento",

        "eventos_extremos", "nivel_alerta",

    ]

    colunas = [c for c in colunas if c in df_filtrado.columns]  # evita KeyError



    st.dataframe(df_filtrado[colunas], use_container_width=True, height=420)



    csv = df_filtrado[colunas].to_csv(index=False).encode("utf-8")

    st.download_button(

        "⬇️ Baixar dados filtrados em CSV",

        data=csv,

        file_name="dados_climaticos_filtrados.csv",

        mime="text/csv",

    )





# ============================================================

# 12. INTERPRETAÇÃO DOS RESULTADOS

# ============================================================



st.markdown("---")

html('<div class="section-heading">💡 Principais resultados</div>')



ano_temp = int(df_filtrado.groupby("ano")["temperatura_media"].mean().idxmax())

ano_chuva = int(df_filtrado.groupby("ano")["chuva_mm"].mean().idxmax())

ano_eventos = int(df_filtrado.groupby("ano")["eventos_extremos"].sum().idxmax())



def cartao(rotulo, valor, nota, cor):

    return (

        f'<div class="insight" style="border-left: 5px solid {cor};">'

        f'<div class="i-label">{rotulo}</div>'

        f'<div class="i-value" style="color: {cor};">{valor}</div>'

        f'<div class="i-note">{nota}</div></div>'

    )





cartoes = [

    ("Ano mais quente", ano_temp, "Maior temperatura média no período filtrado.", COR_TEMP),

    ("Ano com maior chuva média", ano_chuva, "Maior chuva média mensal do período.", COR_CHUVA),

    ("Ano com mais eventos", ano_eventos, "Maior número de eventos extremos.", COR_EVENTO),

    ("Cidade mais quente", cidade_mais_quente, "Maior temperatura média no período filtrado.", COR_TEMP),

    ("Estado mais chuvoso", estado_mais_chuvoso, "Maior volume total de chuva no período filtrado.", COR_CHUVA),

]

for coluna, dados in zip(st.columns(5), cartoes):

    coluna.markdown(cartao(*dados), unsafe_allow_html=True)





# ============================================================

# 13. CONCLUSÃO EXECUTIVA

# ============================================================



st.markdown("---")

html('<div class="section-heading">🎯 Conclusão executiva</div>')



# números da base completa (independentes dos filtros)

temp_ano_all = df.groupby("ano")["temperatura_media"].mean()

temp_reg_all = df.groupby("regiao")["temperatura_media"].mean()

temp_mes_all = df.groupby("mes_numero")["temperatura_media"].mean()

chuva_uf_media = df.groupby("uf")["chuva_mm"].mean()

uf_soma = df.groupby("uf")["chuva_mm"].sum().idxmax()

eventos_alerta = df.groupby("nivel_alerta")["eventos_extremos"].mean()

corr_abs = df[["temperatura_media", "chuva_mm", "umidade", "velocidade_vento", "eventos_extremos"]].corr().abs()

r_te = df["temperatura_media"].corr(df["eventos_extremos"])

r_tchuva = df["temperatura_media"].corr(df["chuva_mm"])

tendencia_all = np.polyfit(temp_ano_all.index, temp_ano_all.values, 1)[0]

vuln_all = indice_vulnerabilidade(df)

nota_vuln = (

    f" A região com maior índice de vulnerabilidade (metodologia própria) é {vuln_all.index[-1]} "

    f"({br(vuln_all['Índice'].iloc[-1])}), mas a diferença para as demais é pequena."

)

r_max = max(corr_abs.iloc[i, j] for i in range(5) for j in range(5) if i != j)

n_reg = f"{len(df):,}".replace(",", ".")



if uf_soma != chuva_uf_media.idxmax():

    nota_soma = (

        f" {uf_soma} lidera na soma apenas por ter {df[df['uf'] == uf_soma]['cidade'].nunique()} "

        "cidades na amostra; por isso as comparações usam médias, não totais."

    )

else:

    nota_soma = " As comparações usam médias, e não totais, para não favorecer estados com mais cidades."



conclusoes = [

    (

        "Panorama",

        f"Entre {df['ano'].min()} e {df['ano'].max()}, a base reúne {n_reg} registros de "

        f"{df['cidade'].nunique()} cidades em {df['uf'].nunique()} estados. A temperatura média foi de "

        f"{br(df['temperatura_media'].mean())} °C e a chuva média mensal, de {br(df['chuva_mm'].mean(), 1)} mm. "

        f"Entre os anos, a temperatura variou apenas de {br(temp_ano_all.min())} a {br(temp_ano_all.max())} °C, "

        f"e {temp_ano_all.idxmax()} foi o ano mais quente. A tendência linear é de {'+' if tendencia_all >= 0 else '−'}{br(abs(tendencia_all), 3)} °C por ano.",

    ),

    (

        "Diferenças regionais",

        f"As regiões diferem pouco em temperatura: de {br(temp_reg_all.min())} °C ({temp_reg_all.idxmin()}) "

        f"a {br(temp_reg_all.max())} °C ({temp_reg_all.idxmax()}). Em chuva, o estado com maior média mensal é "

        f"{chuva_uf_media.idxmax()} ({br(chuva_uf_media.max(), 1)} mm)." + nota_soma + nota_vuln,

    ),

    (
        "Relações e sazonalidade",
        f"Não foi observada uma relação linear relevante entre temperatura média e chuva: "
        f"a correlação calculada foi de {br(r_tchuva)}. "
        f"A temperatura média mensal oscila entre {br(temp_mes_all.min(), 1)} e "
        f"{br(temp_mes_all.max(), 1)} °C ao longo do ano. "
        "Não foi observada diferença consistente na média de eventos extremos entre os níveis de alerta.",
    ),
    (
        "Limitações",

        "A base é simulada, então os resultados descrevem os dados fornecidos, e não o clima real do país. "

        "A ausência de padrões e as diferenças pequenas entre regiões são compatíveis com valores gerados de forma "

        "aleatória. Rankings como \"cidade mais quente\" devem ser lidos com cautela: a diferença entre as "

        "primeiras colocadas é de décimos de grau.",

    ),

]



st.caption("Conclusão calculada sobre a base completa, sem os filtros da barra lateral.")



for i in range(0, len(conclusoes), 2):

    for coluna, (titulo, texto) in zip(st.columns(2), conclusoes[i:i + 2]):

        coluna.markdown(

            f'<div class="conclusao"><div class="c-titulo">{titulo}</div>'

            f'<div class="c-texto">{texto}</div></div>',

            unsafe_allow_html=True,

        )





# ============================================================

# 14. SOBRE OS DADOS E A METODOLOGIA

# ============================================================



st.markdown("---")

html('<div class="section-heading">🧪 Sobre os dados e a metodologia</div>')



cidades_por_uf = df.groupby("uf")["cidade"].nunique()



with st.container(border=True):

    st.markdown(

        f"- **Base:** {n_reg} registros, {df['cidade'].nunique()} cidades, {df['uf'].nunique()} estados e "

        f"{df['regiao'].nunique()} regiões, de {df['data'].min():%m/%Y} a {df['data'].max():%m/%Y} "

        f"({len(df) // df['cidade'].nunique()} registros por cidade). "

        f"Valores ausentes: {int(df.isna().sum().sum())}; linhas duplicadas: {int(df.duplicated().sum())}.\n"

        f"- **Natureza dos dados:** simulados, fornecidos na disciplina. Não representam medições reais.\n"

        f"- **Médias, não somas:** os estados têm de {cidades_por_uf.min()} a {cidades_por_uf.max()} cidades na base. "

        "Somar chuva ou eventos favoreceria quem tem mais cidades, por isso as comparações usam a média por registro (cidade-mês).\n"

        "- **Escalas:** gráficos com diferenças pequenas usam eixo ampliado e avisam disso. "

        "O destaque na barra de maior valor só aparece quando a diferença entre o maior e o menor passa de 15%.\n"

        "- **Correlação não implica causalidade.**"

    )
