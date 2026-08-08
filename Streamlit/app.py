import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import matplotlib
matplotlib.rcParams['font.family'] = 'sans-serif'
import plotly.express as px
import plotly.graph_objects as go
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 
# CSS CUSTOMIZADO
# 
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');

    .block-container {
        padding-top: 3.5rem !important;
        padding-bottom: 3rem !important;
        max-width: 1200px;
    }

    /* Sidebar limpa */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f3460 0%, #16213e 100%);
    }
    section[data-testid="stSidebar"] .stMarkdown h1,
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3,
    section[data-testid="stSidebar"] .stMarkdown p,
    section[data-testid="stSidebar"] label {
        color: #e0e0e0 !important;
    }
    section[data-testid="stSidebar"] .stRadio label,
    section[data-testid="stSidebar"] .stRadio label span,
    section[data-testid="stSidebar"] .stRadio label p,
    section[data-testid="stSidebar"] [role="radio"],
    section[data-testid="stSidebar"] [role="radio"] span,
    section[data-testid="stSidebar"] [role="radio"] p,
    section[data-testid="stSidebar"] [data-testid="stRadio"] label,
    section[data-testid="stSidebar"] [data-testid="stRadio"] label span,
    section[data-testid="stSidebar"] [data-testid="stRadio"] label p {
        color: #ffffff !important;
    }

    /* Filtros - Expander compacto */
    [data-testid="stExpander"] details summary {
        background: linear-gradient(135deg, #e67e22 0%, #f39c12 100%);
        color: white !important;
        border-radius: 10px;
        font-weight: 600;
        font-size: 0.9rem;
        padding: 8px 16px;
    }
    [data-testid="stExpander"] details summary p {
        color: white !important;
    }
    [data-testid="stExpander"] details [data-testid="stExpanderDetails"] {
        padding: 10px 12px !important;
    }

    /* Multiselect tags - laranja */
    [data-baseweb="tag"] {
        background-color: #e67e22 !important;
    }
    [data-baseweb="tag"] span {
        color: white !important;
    }

    /* Compactar checkboxes e widgets dentro do expander */
    [data-testid="stExpander"] .stCheckbox {
        margin-bottom: -10px !important;
        padding-top: 0 !important;
    }
    [data-testid="stExpander"] .stMultiSelect,
    [data-testid="stExpander"] .stSlider {
        margin-bottom: -15px !important;
    }

    /* Banner topo */
    .banner {
        background: linear-gradient(135deg, #0f3460 0%, #1a5276 50%, #0f3460 100%);
        border-radius: 16px;
        padding: 30px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(15, 52, 96, 0.3);
    }
    .banner h1 {
        color: #ffffff !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
        margin: 0;
    }
    .banner p {
        color: #aed6f1 !important;
        font-size: 0.9rem;
        margin: 8px 0 0 0;
    }

    /* Títulos */
    h1 {
        font-weight: 700 !important;
        color: #1a1a2e !important;
        font-size: 1.8rem !important;
    }
    h2 {
        font-weight: 600 !important;
        color: #16213e !important;
        font-size: 1.4rem !important;
    }
    h3 {
        font-weight: 600 !important;
        color: #0f3460 !important;
        font-size: 1.1rem !important;
    }

    /* Métricas */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 12px;
        padding: 18px 16px;
        border-left: 4px solid #0f3460;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    [data-testid="stMetric"] label {
        font-size: 0.8rem !important;
        color: #495057 !important;
        font-weight: 600 !important;
    }
    [data-testid="stMetric"] [data-testid="stMetricValue"] {
        font-size: 1.6rem !important;
        font-weight: 700 !important;
        color: #1a1a2e !important;
    }

    /* Botões */
    .stButton > button {
        background: linear-gradient(135deg, #0f3460 0%, #1a5276 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 28px;
        font-weight: 600;
        font-size: 0.95rem;
        width: 100%;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #1a5276 0%, #0f3460 100%);
        box-shadow: 0 4px 12px rgba(15, 52, 96, 0.4);
        transform: translateY(-1px);
    }

    /* Sliders */
    .stSlider > div > div > div {
        background: #0f3460 !important;
    }

    /* Dataframes */
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }

    /* Cards de risco */
    .risk-card {
        border-radius: 16px;
        padding: 28px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .risk-high {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
        color: white;
    }
    .risk-moderate {
        background: linear-gradient(135deg, #feca57 0%, #ff9f43 100%);
        color: white;
    }
    .risk-low {
        background: linear-gradient(135deg, #48dbfb 0%, #0abde3 100%);
        color: white;
    }
    .risk-card h2 {
        color: white !important;
        font-size: 1.6rem !important;
        margin-bottom: 8px;
    }
    .risk-card p {
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
    }

    /* Divisores */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, #dee2e6, transparent);
        margin: 1.5rem 0;
    }

    /* Alertas */
    div[data-testid="stAlert"] {
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6c757d;
        font-size: 0.8rem;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid #e9ecef;
    }

    /* ====== PÁGINA SOBRE A ONG ====== */

    .hero {
        background: linear-gradient(135deg, #0f3460 0%, #1a5276 40%, #0f3460 100%);
        border-radius: 20px;
        padding: 50px 40px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 8px 30px rgba(15, 52, 96, 0.3);
    }
    .hero h1 {
        color: #ffffff !important;
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        margin: 0 0 12px 0;
    }
    .hero p {
        color: #aed6f1 !important;
        font-size: 1.05rem;
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.7;
    }

    .sobre-card {
        background: #ffffff;
        border-radius: 14px;
        padding: 28px;
        margin: 12px 0;
        border-left: 5px solid #0f3460;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    }
    .sobre-card h3 {
        margin-top: 0;
        margin-bottom: 12px;
    }
    .sobre-card p {
        color: #495057;
        line-height: 1.7;
        font-size: 0.92rem;
        margin: 0;
    }

    .mvv-card {
        border-radius: 14px;
        padding: 24px;
        text-align: center;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        height: 100%;
    }
    .mvv-card .icone {
        font-size: 2.5rem;
        margin-bottom: 10px;
    }
    .mvv-card h3 {
        margin: 0 0 8px 0;
    }
    .mvv-card p {
        color: #495057;
        font-size: 0.88rem;
        line-height: 1.6;
        margin: 0;
    }
    .mvv-missao {
        background: linear-gradient(135deg, #e8f4f8 0%, #d1ecf1 100%);
        border-top: 5px solid #0f3460;
    }
    .mvv-visao {
        background: linear-gradient(135deg, #fef9e7 0%, #fceabb 100%);
        border-top: 5px solid #f39c12;
    }
    .mvv-valores {
        background: linear-gradient(135deg, #fdedec 0%, #fadbd8 100%);
        border-top: 5px solid #e74c3c;
    }

    .timeline-item {
        display: flex;
        gap: 16px;
        margin-bottom: 20px;
    }
    .timeline-marker {
        flex-shrink: 0;
        width: 48px;
        height: 48px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.3rem;
        color: white;
    }
    .timeline-content {
        flex: 1;
        background: #f8f9fa;
        border-radius: 12px;
        padding: 16px 20px;
        border-left: 3px solid #0f3460;
    }
    .timeline-content h4 {
        margin: 0 0 6px 0;
        color: #0f3460;
        font-size: 1rem;
    }
    .timeline-content p {
        margin: 0;
        color: #6c757d;
        font-size: 0.85rem;
        line-height: 1.5;
    }

    .ind-table {
        width: 100%;
        border-collapse: collapse;
    }
    .ind-table td {
        padding: 12px 16px;
        border-bottom: 1px solid #e9ecef;
    }
    .ind-table td:first-child {
        font-weight: 700;
        color: #0f3460;
        width: 120px;
    }
    .ind-table td:last-child {
        color: #495057;
    }

    .pedra-card {
        text-align: center;
        padding: 20px 16px;
        border-radius: 14px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        height: 100%;
    }
    .pedra-card h4 {
        margin: 8px 0 4px 0;
    }
    .pedra-card .faixa {
        font-size: 0.8rem;
        color: #6c757d;
        margin-bottom: 8px;
    }
    .pedra-card .desc {
        font-size: 0.78rem;
        color: #495057;
        line-height: 1.5;
    }

    .impacto-numero {
        text-align: center;
        padding: 24px 12px;
    }
    .impacto-numero .numero {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0f3460;
    }
    .impacto-numero .label {
        font-size: 0.82rem;
        color: #6c757d;
        margin-top: 4px;
    }

    /* ====== EXPLICAÇÃO DOS GRÁFICOS ====== */
    .chart-explicacao {
        background: linear-gradient(135deg, #fff8f0 0%, #fef0e0 100%);
        border-left: 4px solid #e67e22;
        border-radius: 10px;
        padding: 14px 18px;
        margin: 10px 0 30px 0;
        font-size: 0.85rem;
        color: #1a1a2e;
        line-height: 1.6;
    }
    .chart-explicacao strong {
        color: #e67e22;
    }

    /* ====== MÉTRICAS DESTAQUE ====== */
    .metric-destaque {
        display: flex;
        gap: 30px;
        justify-content: center;
        margin: 15px 0 25px 0;
        flex-wrap: wrap;
    }
    .metric-box {
        padding: 22px 50px;
        border-radius: 14px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.12);
    }
    .metric-box .label {
        font-size: 0.82rem;
        font-weight: 600;
        margin-bottom: 6px;
    }
    .metric-box .valor {
        font-size: 2rem;
        font-weight: 800;
    }
    .metric-azul {
        background: linear-gradient(135deg, #0f3460 0%, #1a5276 100%);
    }
    .metric-azul .label {
        color: #aed6f1;
    }
    .metric-azul .valor {
        color: #ffffff;
    }
    .metric-laranja {
        background: linear-gradient(135deg, #e67e22 0%, #f39c12 100%);
    }
    .metric-laranja .label {
        color: #fff5e6;
    }
    .metric-laranja .valor {
        color: #ffffff;
    }

    /* Espaçador entre gráficos */
    .chart-spacer {
        height: 40px;
    }
</style>
""", unsafe_allow_html=True)

# 
# CONFIGURAÇÃO DA PÁGINA
# 
st.set_page_config(
    page_title="Passos Mágicos — Predição de Risco",
    page_icon=os.path.join(BASE_DIR, 'passos-magicos-icon.ico'),
    layout="wide"
)

# 
# FUNÇÕES AUXILIARES
# 
@st.cache_data

@st.cache_data
def carregar_dados():
    # Resolve o caminho do CSV a partir da localização do app.py
    # Funciona tanto local (Windows) quanto no Streamlit Cloud (Linux)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_csv = os.path.join(base_dir, '..', 'Dataset', 'bd_consolid_22_23_24.csv')
    df = pd.read_csv(caminho_csv, sep=';', na_values=['—'], encoding='utf-8')
    return df

def padronizar_colunas(col):
    col = col.strip().lower()
    substituicoes = {
        'á': 'a', 'â': 'a', 'ã': 'a', 'à': 'a',
        'é': 'e', 'ê': 'e', 'í': 'i',
        'ó': 'o', 'ô': 'o', 'õ': 'o',
        'ú': 'u', 'û': 'u', 'ç': 'c',
        ' ': '_', '/': '_', 'º': '', '¹': '1', '²': '2', '³': '3'
    }
    for orig, novo in substituicoes.items():
        col = col.replace(orig, novo)
    col = col.replace('(', '').replace(')', '')
    while '__' in col:
        col = col.replace('__', '_')
    return col

@st.cache_resource
def treinar_modelo():
    df = carregar_dados()
    df.columns = [padronizar_colunas(c) for c in df.columns]

    cols_numericas = ['iaa', 'ieg', 'ips', 'ida', 'matem', 'portug',
                      'ingles', 'inde', 'ipv', 'ian', 'ipp']
    for col in cols_numericas:
        if col in df.columns:
            df[col] = df[col].astype(str).str.replace(',', '.', regex=False)
            df[col] = pd.to_numeric(df[col], errors='coerce')

    cols_int = ['ano', 'ano_nasc', 'idade', 'ano_ingresso', 'cg', 'cf',
                'ct', 'n_av', 'defas']
    for col in cols_int:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df[col] = df[col].astype('Int64')

    df = df.dropna(subset=['ra'])
    colunas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
    for col in colunas_numericas:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].median())

    df['risco_defasagem'] = (df['defas'] < 0).astype(int)

    mapa_instituicao = {
        'Escola Pública': 'Escola Pública', 'Pública': 'Escola Pública',
        'Concluiu o 3º EM': 'Escola Pública',
        'Bolsista Universitário *Formado (a)': 'Bolsista',
        'Bolsista Universitário *Formado (a': 'Bolsista',
        'Privada *Parcerias com Bolsa 100%': 'Bolsista',
        'Privada - Programa de Apadrinhamento': 'Bolsista',
        'Privada - Programa de apadrinhamento': 'Bolsista',
        'Privada - Pagamento por *Empresa Parceira': 'Bolsista',
        'Privada': 'Escola Privada', 'Escola JP II': 'Escola Privada',
        'Rede Decisão': 'Escola Privada',
    }
    df['instituicao_padronizada'] = df['instituicao_de_ensino'].map(
        mapa_instituicao).fillna(df['instituicao_de_ensino'])

    df['instituicao_padronizada'] = df['instituicao_padronizada'].replace(
        'Nenhuma das opções acima', np.nan)

    features_numericas = ['iaa', 'ieg', 'ips', 'ida', 'ipv']
    features_categoricas = ['pedra', 'instituicao_padronizada']

    features_numericas = [f for f in features_numericas if f in df.columns]
    features_categoricas = [f for f in features_categoricas if f in df.columns]

    df_modelo = df.copy()
    df_modelo = df_modelo.dropna(subset=features_categoricas)
    for col in features_categoricas:
        df_modelo[col] = df_modelo[col].astype(str)

    df_modelo = pd.get_dummies(df_modelo, columns=features_categoricas,
                               prefix=features_categoricas, drop_first=True)

    cols_dummies = [c for c in df_modelo.columns
                    if any(c.startswith(f + '_') for f in features_categoricas)]
    features_finais = features_numericas + cols_dummies

    treino = df_modelo[df_modelo['ano'].isin([2022, 2023])]
    X_treino = treino[features_finais]
    y_treino = treino['risco_defasagem']

    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('modelo', RandomForestClassifier(
            n_estimators=200, max_depth=10, min_samples_split=5,
            class_weight='balanced', random_state=42))
    ])
    pipeline.fit(X_treino, y_treino)

    return pipeline, features_finais

# 
# MAPEAMENTO DE NOMES DE FEATURES PARA EXIBIÇÃO
# 
def nome_feature_legivel(nome):
    mapa = {
        'iaa': 'IAA (Autoavaliação)',
        'ieg': 'IEG (Engajamento)',
        'ips': 'IPS (Psicossocial)',
        'ida': 'IDA (Desempenho)',
        'ipv': 'IPV (Ponto de Virada)',
        'instituicao_padronizada_Bolsista': 'Instituição: Bolsista',
        'instituicao_padronizada_Escola Privada': 'Instituição: Escola Privada',
        'instituicao_padronizada_Escola Pública': 'Instituição: Escola Pública',
    }
    if nome in mapa:
        return mapa[nome]
    if nome.startswith('pedra_'):
        return f'Pedra: {nome[6:]}'
    return nome.replace('_', ' ').title()

# 
# PALETA DE CORES
# 
PAleta_AZUL = ['#08306b', '#2171b5', '#4292c6', '#6baed6',
               '#9ecae1', '#c6dbef', '#deebf7', '#525252',
               '#737373', '#969696', '#bdbdbd', '#d9d9d9',
               '#252525', '#000000', '#08519c']

# 
# SIDEBAR — LIMPA, APENAS NAVEGAÇÃO
# 
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding:20px 0;'>
        <h1 style='color:#ffffff !important; font-size:1.8rem; font-weight:700; margin:0;'>Associação Passos Mágicos</h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    pagina = st.radio("Navegação", [
        "ℹ️ Sobre a Passos Mágicos",
        "📊 Predições e Indicadores",
        "📈 Métricas do Modelo"
    ])

# 
# CARREGAR MODELO
# 
with st.spinner("Carregando modelo..."):
    pipeline, features_modelo = treinar_modelo()

# 
# PÁGINA 1 — SOBRE A PASSOS MÁGICOS
# 
if pagina == "ℹ️ Sobre a Passos Mágicos":
    st.markdown("")

    # ====== LOGO ======
    col_esq, col_centro, col_dir = st.columns([2, 1, 2])
    with col_centro:
        st.image(os.path.join(BASE_DIR, 'Passos-magicos-logo.png'), use_container_width=True)
    st.markdown("")

    # ====== NÚMEROS DE IMPACTO ======
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="impacto-numero">
            <div class="numero">20+</div>
            <div class="label">Anos de atuação</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="impacto-numero">
            <div class="numero">3</div>
            <div class="label">Anos de dados</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="impacto-numero">
            <div class="numero">100%</div>
            <div class="label">Foco no aluno</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="impacto-numero">
            <div class="numero">6</div>
            <div class="label">Indicadores educacionais</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ====== HISTÓRIA ======
    st.subheader("📖 Nossa História")
    st.markdown("")

    st.markdown("""
    <div class="timeline-item">
        <div class="timeline-marker" style="background:#08306b;">🌱</div>
        <div class="timeline-content">
            <h4>O Início</h4>
            <p>A Associação Passos Mágicos nasceu do desejo de promover a
            transformação social através da educação de crianças e jovens em
            situação de vulnerabilidade. Com trabalho voluntário e muita
            dedicação, a ONG iniciou suas atividades oferecendo apoio
            pedagógico complementar.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="timeline-item">
        <div class="timeline-marker" style="background:#2171b5;">📚</div>
        <div class="timeline-content">
            <h4>Crescimento e Estruturação</h4>
            <p>Com o passar dos anos, a organização expandiu seu escopo,
            incorporando acompanhamento psicossocial, apoio à inserção em
            escolas privadas via programas de bolsas e parcerias com empresas.
            Desenvolveu também um sistema próprio de indicadores para
            mensurar o desenvolvimento de cada aluno.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="timeline-item">
        <div class="timeline-marker" style="background:#4292c6;">📊</div>
        <div class="timeline-content">
            <h4>Decisão por Dados</h4>
            <p>A Passos Mágicos passou a utilizar dados e indicadores
            educacionais de forma sistemática, coletando informações anuais
            sobre desempenho acadêmico, engajamento e desenvolvimento
            psicossocial de cada aluno. Esses dados permitem identificar
            tendências, intervir precocemente e mensurar o impacto das
            ações ao longo do tempo.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="timeline-item">
        <div class="timeline-marker" style="background:#6baed6;">🚀</div>
        <div class="timeline-content">
            <h4>Inovação com IA</h4>
            <p>Em 2024, a ONG deu um passo adiante: a utilização de
            inteligência artificial para prever riscos de defasagem escolar.
            Este projeto, desenvolvido no Datathon, aplica machine learning
            aos dados históricos para identificar alunos que precisam de
            intervenção antes que a defasagem se consolide.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ====== MISSÃO, VISÃO E VALORES ======
    st.subheader("🎯 Missão, Visão e Valores")
    st.markdown("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="mvv-card mvv-missao">
            <div class="icone">🎯</div>
            <h3>Missão</h3>
            <p>Nossa missão é transformar a vida de jovens e crianças,
            oferecendo ferramentas para levá-los a melhores oportunidades
            de vida.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="mvv-card mvv-visao">
            <div class="icone">💡</div>
            <h3>Visão</h3>
            <p>Nossa visão é viver em um Brasil no qual todas as crianças
            e jovens têm iguais oportunidades para realizarem seus sonhos
            e são agentes transformadores de suas próprias vidas.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="mvv-card mvv-valores">
            <div class="icone">❤️</div>
            <h3>Valores</h3>
            <p>Empatia, amor ao aprendizado, poder em acreditar em si e no
            próximo, pertencimento, gratidão, busca pelo saber, educação que
            transforma e ajuda a transformar, aprender a aprender.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ====== INDICADORES EDUCACIONAIS ======
    st.subheader("📊 Indicadores Educacionais")
    st.markdown("A Passos Mágicos desenvolveu um sistema próprio de indicadores para acompanhar o desenvolvimento integral de cada aluno:")

    st.markdown("""
    <div class="sobre-card">
        <table class="ind-table">
            <tr>
                <td><b>INDE</b></td>
                <td>Índice de Desenvolvimento Educacional — indicador composto
                que sintetiza o desenvolvimento global do aluno.</td>
            </tr>
            <tr>
                <td><b>IAA</b></td>
                <td>Índice de Autoavaliação — como o aluno se percebe e
                avalia seu próprio desenvolvimento.</td>
            </tr>
            <tr>
                <td><b>IEG</b></td>
                <td>Índice de Engajamento — participação e frequência nas
                atividades propostas.</td>
            </tr>
            <tr>
                <td><b>IPS</b></td>
                <td>Índice Psicossocial — desenvolvimento emocional e
                social do aluno.</td>
            </tr>
            <tr>
                <td><b>IDA</b></td>
                <td>Índice de Desempenho Acadêmico — notas e desempenho
                escolar formal.</td>
            </tr>
            <tr>
                <td><b>IPV</b></td>
                <td>Índice do Ponto de Virada — identifica o momento em que
                o aluno começa a se transformar.</td>
            </tr>
            <tr>
                <td><b>IAN</b></td>
                <td>Índice de Assistência Pedagógica — apoio e
                acompanhamento recebido pela equipe.</td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ====== SISTEMA DE PEDRAS ======
    st.subheader("💎 Sistema de Classificação — Pedras")
    st.markdown("Cada aluno é classificado conforme seu INDE em um sistema de pedras que representa seu nível de desenvolvimento:")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="pedra-card" style="background:linear-gradient(135deg,#f8f9fa,#e9ecef); border-top:5px solid #bdc3c7;">
            <h4>Quartzo</h4>
            <div class="faixa">INDE até 3,0</div>
            <div class="desc">Necessita apoio intensivo e acompanhamento
            próximo da equipe pedagógica.</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="pedra-card" style="background:linear-gradient(135deg,#fdf2e9,#fae5d3); border-top:5px solid #d35400;">
            <h4>Ágata</h4>
            <div class="faixa">INDE 3,1 – 5,0</div>
            <div class="desc">Em desenvolvimento, necessita reforço
            em áreas específicas do aprendizado.</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="pedra-card" style="background:linear-gradient(135deg,#f4ecf7,#d7bde2); border-top:5px solid #8e44ad;">
            <h4>Ametista</h4>
            <div class="faixa">INDE 5,1 – 7,0</div>
            <div class="desc">Progresso consistente, pronto para
            novos desafios e maior autonomia.</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="pedra-card" style="background:linear-gradient(135deg,#fef9e7,#fceabb); border-top:5px solid #f1c40f;">
            <h4>Topázio</h4>
            <div class="faixa">INDE 7,1 – 10,0</div>
            <div class="desc">Excelente desempenho, referência
            e inspiração para os demais alunos.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ====== PARCERIAS ======
    st.subheader("🤝 Parcerias e Atuação")
    st.markdown("")

    st.markdown("""
    <div class="sobre-card">
        <h3>🏫 Escolas Públicas</h3>
        <p>A ONG atua em parceria com escolas públicas, oferecendo
        complementação educacional e acompanhamento pedagógico para alunos
        que precisam de apoio adicional além da escola regular.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sobre-card">
        <h3>🎓 Bolsas em Escolas Privadas</h3>
        <p>Através de programas de apadrinhamento e parcerias com instituições
        privadas, a Passos Mágicos proporciona acesso a educação de qualidade
        para alunos talentosos que não teriam condições de arcar com mensalidades.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sobre-card">
        <h3>🏢 Empresas Parceiras</h3>
        <p>Empresas que apoiam a ONG através de patrocínio, programas de
        voluntariado corporativo e financiamento de bolsas integrais para
        estudantes em todos os níveis de ensino.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ====== SOBRE O PROJETO ======
    st.subheader("🤖 Sobre Este Projeto")
    st.markdown("")

    st.markdown("""
    <div class="sobre-card">
        <h3>📊 Datathon — Predição de Risco</h3>
        <p>Este aplicativo foi desenvolvido como parte do Datathon, aplicando
        machine learning aos dados históricos da Passos Mágicos (2022–2024)
        para prever o risco de defasagem escolar. O modelo RandomForest
        identifica alunos com probabilidade de estar em fase abaixo da ideal,
        permitindo que a equipe pedagógica intervenha de forma proativa.</p>
        <br>
        <p><b>🎯 Objetivo:</b> Identificar precocemente alunos em risco para
        intervenção pedagógica antes que a defasagem se consolide.</p>
        <br>
        <p><b>📈 Resultado:</b> ROC-AUC de 0,77 e Average Precision de 0,83,
        garantindo que a grande maioria dos alunos em risco seja corretamente identificada.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div class='footer'>
    Desenvolvido por Katia Wilkomm • Datathon Passos Mágicos • 2024
    </div>
    """, unsafe_allow_html=True)

# 
# PÁGINA 2 — PREDIÇÕES E INDICADORES
# 
elif pagina == "📊 Predições e Indicadores":
    st.markdown("")
    st.markdown("""
    <h1 style='text-align: center; color: #0f3460; font-weight: 700; margin-bottom: 5px;'>📊 Predições e Indicadores</h1>
    <p style='text-align: center; color: #6c757d; font-size: 0.95rem; margin-bottom: 20px;'>Acompanhamento educacional e análise de risco de defasagem</p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ====== CARREGAR E PREPARAR DADOS ======
    df = carregar_dados()
    df.columns = [padronizar_colunas(c) for c in df.columns]

    cols_num = ['iaa', 'ieg', 'ips', 'ida', 'inde', 'ipv', 'ian', 'ipp']
    for col in cols_num:
        if col in df.columns:
            df[col] = df[col].astype(str).str.replace(',', '.', regex=False)
            df[col] = pd.to_numeric(df[col], errors='coerce')

    df['risco_defasagem'] = (df['defas'] < 0).astype(int)

    mapa_inst = {
        'Escola Pública': 'Escola Pública', 'Pública': 'Escola Pública',
        'Concluiu o 3º EM': 'Escola Pública',
        'Bolsista Universitário *Formado (a)': 'Bolsista',
        'Bolsista Universitário *Formado (a': 'Bolsista',
        'Privada *Parcerias com Bolsa 100%': 'Bolsista',
        'Privada - Programa de Apadrinhamento': 'Bolsista',
        'Privada - Programa de apadrinhamento': 'Bolsista',
        'Privada - Pagamento por *Empresa Parceira': 'Bolsista',
        'Privada': 'Escola Privada', 'Escola JP II': 'Escola Privada',
        'Rede Decisão': 'Escola Privada',
    }
    df['inst_pad'] = df['instituicao_de_ensino'].map(mapa_inst).fillna('Outros')

    df['inst_pad'] = df['inst_pad'].replace('Nenhuma das opções acima', 'Outros')

    # ====== PALETA AZUL / LARANJA / AMARELO ======
    cores_pedra = {
        'Quartzo': '#9ecae1',
        'Ágata': '#e67e22',
        'Ametista': '#08306b',
        'Topázio': '#f1c40f'
    }
    ordem_pedras = ['Quartzo', 'Ágata', 'Ametista', 'Topázio']

    cores_ind = ['#08306b', '#e67e22', '#f1c40f', '#2171b5', '#ff9f43']

    # ====== OPÇÕES DISPONÍVEIS PARA FILTROS ======
    anos_disp = sorted(df['ano'].dropna().unique().tolist())
    insts_disp = sorted(df['inst_pad'].dropna().unique().tolist())
    pedras_disp = sorted([p for p in df['pedra'].dropna().unique().tolist()])
    generos_disp = sorted(df['genero'].dropna().unique().tolist()) if 'genero' in df.columns else []

    # Defaults (sem filtro)
    anos_sel = anos_disp
    insts_sel = insts_disp
    pedras_sel = pedras_disp
    generos_sel = generos_disp
    fases_sel = None
    idade_min, idade_max = None, None
    ingresso_min, ingresso_max = None, None
    inde_min, inde_max = None, None

    # ====== FILTROS INTERATIVOS — UM ABAIXO DO OUTRO ======
    with st.expander("🎛️ Filtros Interativos", expanded=False):
        st.markdown("Marque os filtros que deseja aplicar:")

        # Ano
        c1, c2 = st.columns([1, 3])
        with c1:
            filtrar_ano = st.checkbox("Ano")
        with c2:
            if filtrar_ano:
                anos_sel = st.multiselect("Selecione os anos", anos_disp, default=anos_disp,
                                          label_visibility="collapsed")

        # Instituição
        c1, c2 = st.columns([1, 3])
        with c1:
            filtrar_inst = st.checkbox("Instituição")
        with c2:
            if filtrar_inst:
                insts_sel = st.multiselect("Selecione as instituições", insts_disp, default=insts_disp,
                                           label_visibility="collapsed")

        # Pedra
        c1, c2 = st.columns([1, 3])
        with c1:
            filtrar_pedra = st.checkbox("Pedra")
        with c2:
            if filtrar_pedra:
                pedras_sel = st.multiselect("Selecione as pedras", pedras_disp, default=pedras_disp,
                                           label_visibility="collapsed")

        # Gênero
        c1, c2 = st.columns([1, 3])
        with c1:
            filtrar_genero = st.checkbox("Gênero")
        with c2:
            if filtrar_genero and generos_disp:
                generos_sel = st.multiselect("Selecione os gêneros", generos_disp, default=generos_disp,
                                            label_visibility="collapsed")

        # Fase
        c1, c2 = st.columns([1, 3])
        with c1:
            filtrar_fase = st.checkbox("Fase")
        with c2:
            if filtrar_fase and 'fase' in df.columns:
                fases_disp = sorted([f for f in df['fase'].dropna().unique().tolist()])
                fases_sel = st.multiselect("Selecione as fases", fases_disp, default=fases_disp,
                                          label_visibility="collapsed")

        # Idade
        c1, c2 = st.columns([1, 3])
        with c1:
            filtrar_idade = st.checkbox("Idade")
        with c2:
            if filtrar_idade and 'idade' in df.columns:
                idade_min_val = int(df['idade'].min())
                idade_max_val = int(df['idade'].max())
                idade_min, idade_max = st.slider("Faixa de idade", idade_min_val, idade_max_val,
                                                  (idade_min_val, idade_max_val),
                                                  label_visibility="collapsed")

        # Ano de Ingresso
        c1, c2 = st.columns([1, 3])
        with c1:
            filtrar_ingresso = st.checkbox("Ano de Ingresso")
        with c2:
            if filtrar_ingresso and 'ano_ingresso' in df.columns:
                ingresso_min_val = int(df['ano_ingresso'].min())
                ingresso_max_val = int(df['ano_ingresso'].max())
                ingresso_min, ingresso_max = st.slider("Ano de ingresso", ingresso_min_val, ingresso_max_val,
                                                       (ingresso_min_val, ingresso_max_val),
                                                       label_visibility="collapsed")

        # Faixa de INDE
        c1, c2 = st.columns([1, 3])
        with c1:
            filtrar_inde = st.checkbox("Faixa de INDE")
        with c2:
            if filtrar_inde and 'inde' in df.columns:
                inde_min_val = float(df['inde'].min())
                inde_max_val = float(df['inde'].max())
                inde_min, inde_max = st.slider("Faixa de INDE", inde_min_val, inde_max_val,
                                                (inde_min_val, inde_max_val), 0.1,
                                                label_visibility="collapsed")

    # Aplicar filtros
    mask = df['ano'].isin(anos_sel) & df['inst_pad'].isin(insts_sel)
    if pedras_sel:
        mask &= df['pedra'].isin(pedras_sel)
    if generos_sel and 'genero' in df.columns:
        mask &= df['genero'].isin(generos_sel)
    if fases_sel is not None and 'fase' in df.columns:
        mask &= df['fase'].isin(fases_sel)
    if idade_min is not None and 'idade' in df.columns:
        mask &= (df['idade'] >= idade_min) & (df['idade'] <= idade_max)
    if ingresso_min is not None and 'ano_ingresso' in df.columns:
        mask &= (df['ano_ingresso'] >= ingresso_min) & (df['ano_ingresso'] <= ingresso_max)
    if inde_min is not None and 'inde' in df.columns:
        mask &= (df['inde'] >= inde_min) & (df['inde'] <= inde_max)

    df_f = df[mask]

    if len(df_f) == 0:
        st.warning("Nenhum registro encontrado com os filtros selecionados.")
    else:
        # ====== MÉTRICAS DESTAQUE ======
        pct_risco = df_f['risco_defasagem'].mean() * 100
        st.markdown(f"""
        <div class="metric-destaque">
            <div class="metric-box metric-azul">
                <div class="label">Total de Registros</div>
                <div class="valor">{len(df_f)}</div>
            </div>
            <div class="metric-box metric-laranja">
                <div class="label">% em Risco</div>
                <div class="valor">{pct_risco:.1f}%</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # ====== GRÁFICO 1: Risco por Ano ======
        st.subheader("Risco de Defasagem por Ano")
        risco_ano = df_f.groupby('ano')['risco_defasagem'].mean().reset_index()
        risco_ano['risco_pct'] = risco_ano['risco_defasagem'] * 100
        fig = px.bar(risco_ano, x='ano', y='risco_pct',
                     color='risco_pct',
                     color_continuous_scale=['#9ecae1', '#e67e22', '#f1c40f'],
                     text=risco_ano['risco_pct'].apply(lambda x: f'{x:.1f}%'),
                     labels={'ano': 'Ano', 'risko_pct': '% em Risco'})
        fig.update_layout(
            template='plotly_white', height=420, showlegend=False,
            margin=dict(l=20, r=20, t=20, b=20), coloraxis_showscale=False,
            hoverlabel=dict(bgcolor='#0f3460', font_size=12, font_color='white')
        )
        fig.update_traces(textposition='outside', textfont_size=12,
                          marker_line_color='#08306b', marker_line_width=1.5)
        fig.update_yaxes(range=[0, max(risco_ano['risco_pct'].max() * 1.2, 100)])
        fig.update_xaxes(type='category')
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        <div class="chart-explicacao">
            <strong>Sobre o gráfico:</strong> Mostra a proporção de alunos
            em risco de defasagem ao longo dos anos. Passe o mouse sobre as barras
            para ver os valores exatos.
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="chart-spacer"></div>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown('<div class="chart-spacer"></div>', unsafe_allow_html=True)

        # ====== GRÁFICO 2: Distribuição por Pedra ======
        st.subheader("Distribuição por Pedra")
        dist_pedra = df_f['pedra'].value_counts().reset_index()
        dist_pedra.columns = ['Pedra', 'Quantidade']
        dist_pedra['ordem'] = dist_pedra['Pedra'].apply(
            lambda x: ordem_pedras.index(x) if x in ordem_pedras else 99)
        dist_pedra = dist_pedra.sort_values('ordem')
        fig = px.pie(dist_pedra, values='Quantidade', names='Pedra',
                     color='Pedra', color_discrete_map=cores_pedra, hole=0.4)
        fig.update_traces(textposition='inside', textinfo='label+percent',
                         textfont_size=12, marker_line_color='white', marker_line_width=2)
        fig.update_layout(template='plotly_white', height=420, showlegend=True,
                          margin=dict(l=20, r=20, t=20, b=20),
                          hoverlabel=dict(bgcolor='#0f3460', font_size=12, font_color='white'))
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        <div class="chart-explicacao">
            <strong>Sobre o gráfico:</strong> Apresenta a distribuição dos alunos
            entre as pedras (Quartzo, Ágata, Ametista, Topázio). Clique em uma pedra
            na legenda para destacá-la.
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="chart-spacer"></div>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown('<div class="chart-spacer"></div>', unsafe_allow_html=True)

        # ====== GRÁFICO 3: Box INDE por Pedra ======
        st.subheader("Distribuição do INDE por Pedra")
        df_box = df_f.dropna(subset=['inde', 'pedra']).copy()
        if len(df_box) > 0:
            df_box['pedra_ordem'] = df_box['pedra'].apply(
                lambda x: ordem_pedras.index(x) if x in ordem_pedras else 99)
            df_box = df_box.sort_values('pedra_ordem')
            fig = px.box(df_box, x='pedra', y='inde', color='pedra',
                         color_discrete_map=cores_pedra,
                         labels={'pedra': 'Pedra', 'inde': 'INDE'})
            fig.update_layout(template='plotly_white', height=420,
                              showlegend=False, margin=dict(l=20, r=20, t=20, b=20),
                              hoverlabel=dict(bgcolor='#0f3460', font_size=12, font_color='white'))
            fig.update_traces(marker_size=6, line_width=1.5)
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        <div class="chart-explicacao">
            <strong>Sobre o gráfico:</strong> O boxplot mostra a dispersão do INDE
            dentro de cada pedra. A linha central é a mediana e os pontos fora da caixa
            representam alunos atípicos. Passe o mouse para ver estatísticas detalhadas.
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="chart-spacer"></div>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown('<div class="chart-spacer"></div>', unsafe_allow_html=True)

        # ====== GRÁFICO 4: Histograma do INDE ======
        st.subheader("Histograma do INDE")
        df_hist = df_f.dropna(subset=['inde']).copy()
        if len(df_hist) > 0:
            fig = px.histogram(df_hist, x='inde', nbins=30,
                               color_discrete_sequence=['#e67e22'], opacity=0.85,
                               labels={'inde': 'INDE'})
            fig.update_layout(template='plotly_white', height=420, showlegend=False,
                              margin=dict(l=20, r=20, t=20, b=20), bargap=0.05,
                              hoverlabel=dict(bgcolor='#0f3460', font_size=12, font_color='white'))
            fig.update_xaxes(title='INDE')
            fig.update_yaxes(title='Frequência')
            fig.update_traces(marker_line_color='#08306b', marker_line_width=1)
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        <div class="chart-explicacao">
            <strong>Sobre o gráfico:</strong> O histograma revela como o INDE está
            distribuído entre os alunos. Uma concentração à esquerda indica muitos alunos
            com baixo desenvolvimento. Use o zoom arrastando o mouse sobre uma faixa do eixo X.
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="chart-spacer"></div>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown('<div class="chart-spacer"></div>', unsafe_allow_html=True)

        # ====== GRÁFICO 5: Evolução dos Indicadores ======
        st.subheader("Evolução dos Indicadores por Ano")
        indicadores = ['ida', 'ieg', 'iaa', 'ips', 'ipv']
        indicadores = [i for i in indicadores if i in df_f.columns]

        if indicadores:
            df_evo = df_f.groupby('ano')[indicadores].mean().reset_index()
            df_evo_long = df_evo.melt(id_vars=['ano'], var_name='Indicador', value_name='Valor')
            df_evo_long = df_evo_long.dropna(subset=['Valor'])
            fig = px.line(df_evo_long, x='ano', y='Valor', color='Indicador',
                          markers=True, color_discrete_sequence=cores_ind[:len(indicadores)],
                          labels={'ano': 'Ano', 'Valor': 'Valor Médio'})
            fig.update_layout(template='plotly_white', height=480, hovermode='x unified',
                              margin=dict(l=20, r=20, t=20, b=20),
                              hoverlabel=dict(bgcolor='#0f3460', font_size=12, font_color='white'),
                              legend=dict(orientation="h", yanchor="bottom", y=1.02,
                                          xanchor="right", x=1))
            fig.update_traces(line_width=2.5, marker_size=9)
            fig.update_xaxes(type='category')
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("""
            <div class="chart-explicacao">
                <strong>Sobre o gráfico:</strong> Mostra a evolução dos indicadores
                ao longo dos anos. Quedas no IDA ou IEG sinalizam necessidade de intervenção.
                Passe o mouse para ver todos os indicadores de um ano e clique na legenda
                para mostrar/ocultar indicadores.
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="chart-spacer"></div>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown('<div class="chart-spacer"></div>', unsafe_allow_html=True)

        # ====== GRÁFICO 6: Heatmap Correlação ======
        st.subheader("Correlação entre Indicadores")
        cols_corr = [c for c in ['iaa', 'ieg', 'ips', 'ida', 'ipv', 'inde'] if c in df_f.columns]
        cols_corr = list(dict.fromkeys(cols_corr))
        if len(cols_corr) >= 2:
            corr = df_f[cols_corr].corr()
            fig, ax = plt.subplots(figsize=(8, 6))
            cmap = sns.color_palette("YlOrBr", as_cmap=True)
            sns.heatmap(corr, annot=True, fmt='.2f', cmap=cmap, center=0,
                        vmin=-1, vmax=1, square=True, linewidths=0.5, ax=ax,
                        annot_kws={'size': 9})
            ax.set_title('Matriz de Correlação', fontweight='bold', fontsize=12)
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

        st.markdown("""
        <div class="chart-explicacao">
            <strong>Sobre o gráfico:</strong> A matriz mostra como os indicadores se
            relacionam entre si. Valores próximos de 1 indicam correlação forte — quando
            um sobe, o outro também tende a subir. O INDE costuma ter alta correlação
            com IDA e IEG.
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="chart-spacer"></div>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown('<div class="chart-spacer"></div>', unsafe_allow_html=True)

        # ====== GRÁFICO 7: Radar por Pedra ======
        st.subheader("Radar: Indicadores por Pedra")
        radar_inds = [i for i in ['iaa', 'ieg', 'ips', 'ida', 'ipv'] if i in df_f.columns]
        if radar_inds and 'pedra' in df_f.columns:
            df_radar = df_f.groupby('pedra')[radar_inds].mean().reset_index()
            df_radar = df_radar[df_radar['pedra'].isin(ordem_pedras)]
            if len(df_radar) > 0:
                fig = go.Figure()
                for _, row in df_radar.iterrows():
                    fig.add_trace(go.Scatterpolar(
                        r=row[radar_inds].values,
                        theta=[i.upper() for i in radar_inds],
                        fill='toself', name=row['pedra'],
                        line=dict(color=cores_pedra.get(row['pedra'], '#6c757d'), width=2.5)
                    ))
                fig.update_layout(
                    polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
                    template='plotly_white', height=420,
                    margin=dict(l=20, r=20, t=20, b=20),
                    hoverlabel=dict(bgcolor='#0f3460', font_size=12, font_color='white'),
                    legend=dict(orientation="h", yanchor="bottom", y=-0.15,
                                xanchor="center", x=0.5)
                )
                st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        <div class="chart-explicacao">
            <strong>Sobre o gráfico:</strong> Compara o perfil de indicadores de cada
            pedra em formato de radar. Polígonos maiores indicam desenvolvimento mais amplo.
            Clique nas pedras da legenda para mostrar/ocultar cada perfil.
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="chart-spacer"></div>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown('<div class="chart-spacer"></div>', unsafe_allow_html=True)

        # ====== GRÁFICO 8: Scatter IDA vs INDE ======
        st.subheader("IDA vs INDE")
        df_scatter = df_f.dropna(subset=['ida', 'inde', 'pedra']).copy()
        if len(df_scatter) > 0:
            fig = px.scatter(df_scatter, x='ida', y='inde', color='pedra',
                             color_discrete_map=cores_pedra, opacity=0.7,
                             labels={'ida': 'IDA (Desempenho)', 'inde': 'INDE',
                                     'pedra': 'Pedra'})
            fig.update_layout(template='plotly_white', height=420,
                              margin=dict(l=20, r=20, t=20, b=20),
                              hoverlabel=dict(bgcolor='#0f3460', font_size=12, font_color='white'))
            fig.update_traces(marker_size=7, marker_line_width=0.5)
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        <div class="chart-explicacao">
            <strong>Sobre o gráfico:</strong> Mostra a relação entre desempenho
            acadêmico (IDA) e o índice global (INDE). Pontos acima da diagonal
            representam alunos com INDE acima do esperado. Use o zoom e as ferramentas
            de seleção para explorar grupos específicos.
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="chart-spacer"></div>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown('<div class="chart-spacer"></div>', unsafe_allow_html=True)

        # ====== GRÁFICO 9: Média por Instituição ======
        st.subheader("Média de Indicadores por Instituição")
        inst_inds = [c for c in ['inde', 'ida', 'ieg', 'ips', 'iaa'] if c in df_f.columns]
        if inst_inds:
            df_inst = df_f.groupby('inst_pad')[inst_inds].mean().reset_index()
            df_inst_long = df_inst.melt(id_vars=['inst_pad'], var_name='Indicador',
                                        value_name='Valor')
            df_inst_long = df_inst_long.dropna(subset=['Valor'])
            fig = px.bar(df_inst_long, x='inst_pad', y='Valor', color='Indicador',
                         barmode='group',
                         color_discrete_sequence=cores_ind[:len(inst_inds)],
                         labels={'inst_pad': 'Instituição', 'Valor': 'Valor Médio'})
            fig.update_layout(template='plotly_white', height=420,
                              margin=dict(l=20, r=20, t=20, b=20),
                              hoverlabel=dict(bgcolor='#0f3460', font_size=12, font_color='white'),
                              legend=dict(orientation="h", yanchor="bottom", y=1.02,
                                          xanchor="right", x=1))
            fig.update_traces(marker_line_width=1)
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("""
            <div class="chart-explicacao">
                <strong>Sobre o gráfico:</strong> Compara a média dos indicadores
                entre os tipos de instituição. Diferenças significativas sugerem que o
                tipo de escola influencia o desenvolvimento. Passe o mouse sobre as barras
                e clique na legenda para filtrar.
            </div>
            """, unsafe_allow_html=True)

# 
# PÁGINA 3 — MÉTRICAS DO MODELO
# 
elif pagina == "📈 Métricas do Modelo":
    st.markdown("")
    st.title("📈 Métricas e Avaliação do Modelo")
    st.markdown("---")
    st.subheader("Configuração do Modelo")
    st.markdown("""
    - **Algoritmo:** RandomForestClassifier
    - **class_weight:** balanced
    - **n_estimators:** 200
    - **max_depth:** 10
    - **Divisão:** Treino 2022–2023 | Teste 2024
    - **Variável-alvo:** `defas < 0` (risco de defasagem)
    - **Features:** IAA, IEG, IPS, IDA, IPV, Pedra e Instituição
    """)
    st.markdown("---")
    st.subheader("Métricas de Performance")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("ROC-AUC", "0.77")
    with col2:
        st.metric("Recall (Risco)", "0.64")
    with col3:
        st.metric("Precision (Risco)", "0.79")
    with col4:
        st.metric("Average Precision", "0.83")
    st.markdown("---")
    st.subheader("Top 10 Features Mais Importantes")
    importances = pipeline.named_steps['modelo'].feature_importances_
    feat_imp = pd.DataFrame({
        'feature': features_modelo,
        'importance': importances
    }).sort_values('importance', ascending=False).head(15)
    feat_imp['feature_legivel'] = feat_imp['feature'].apply(nome_feature_legivel)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=feat_imp, x='importance', y='feature_legivel',
                palette=PAleta_AZUL, ax=ax)
    ax.set_xlabel('Importância')
    ax.set_ylabel('Feature')
    sns.despine()
    st.pyplot(fig)
    plt.close()
    st.markdown("---")
    st.subheader("Considerações Finais")
    st.markdown("""
    O modelo foi treinado com dados de 2022–2023 e testado em 2024, atingindo
    ROC-AUC de 0,77, Recall de 0,64 e Average Precision de 0,83. A priorização
    do Recall é adequada ao contexto educacional, onde não identificar um aluno
    em risco é mais custoso do que gerar um falso positivo. As features `fase`
    e `fase_ideal` foram removidas por vazamento de dados. A feature `ipp` foi
    excluída por inconsistência nos registros de 2022 (todos com valor 0).
    As variáveis mais influentes foram IDA, IPV, Pedra (Topázio) e IEG. Como
    limitações, destacam-se a ausência de ajuste de hiperparâmetros, validação
    cruzada temporal, otimização de threshold e dados socioeconômicos.
    """)