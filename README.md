# 🔮 Predição de Risco de Defasagem Escolar — Associação Passos Mágicos

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

> Projeto desenvolvido para o **Datathon da PosTech** (Pós-graduação em Data Analytics), aplicando Machine Learning e Data Analytics aos dados educacionais da Associação Passos Mágicos (2022–2024) para identificar precocemente alunos em risco de defasagem escolar.

**Autora:** Katia Wilkomm  
**Instituição:** PosTech — Data Analytics  
**Case:** Associação Passos Mágicos

---

## 📋 Sumário

- [1. Descrição Geral](#1-descrição-geral)
- [2. Tecnologias Utilizadas](#2-tecnologias-utilizadas)
- [3. Pré-requisitos](#3-pré-requisitos)
- [4. Como Executar o Projeto](#4-como-executar-o-projeto)
- [5. Estrutura do Projeto](#5-estrutura-do-projeto)
- [6. Funcionalidades](#6-funcionalidades)
- [7. Limitações Conhecidas](#7-limitações-conhecidas)
- [8. Contribuição](#8-contribuição)
- [9. Licença](#9-licença)
- [10. Considerações Finais](#10-considerações-finais)

---

## 1. Descrição Geral

A **Associação Passos Mágicos** é uma ONG fundada em 1992 que atua há mais de 30 anos na transformação social de crianças e jovens em situação de vulnerabilidade, oferecendo educação de qualidade, apoio psicológico/psicopedagógico e ampliação da visão de mundo.

### Problema abordado

A defasagem escolar — quando o aluno está em fase abaixo da ideal para sua idade — é um indicador crítico que pode comprometer toda a trajetória de desenvolvimento do estudante. O desafio é **identificar precocemente quais alunos estão em risco de defasagem**, permitindo que a equipe pedagógica intervenha antes que o atraso se consolide.

### Objetivo do projeto

Desenvolver um **modelo preditivo** capaz de calcular a probabilidade de um aluno entrar em risco de defasagem, e disponibilizá-lo em uma **aplicação web interativa** (Streamlit) acessível à equipe pedagógica da ONG, sem necessidade de conhecimento técnico em programação ou Data Science.

### Entregas do projeto

- [x] Notebook Python com análise exploratória, limpeza e modelo preditivo
- [x] Aplicação Streamlit com deploy no Community Cloud
- [x] Apresentação de storytelling (PPT/PDF)
- [x] Código-fonte versionado no GitHub
- [x] Vídeo de apresentação (até 5 minutos)

---

## 2. Tecnologias Utilizadas

| Tecnologia | Versão Sugerida | Propósito no Projeto |
|---|---|---|
| **Python** | 3.10+ | Linguagem base para processamento e modelagem |
| **Pandas** | 2.0.0+ | Manipulação, limpeza e estruturação de dados tabulares |
| **NumPy** | 1.24.0+ | Operações matemáticas e suporte a arrays multidimensionais |
| **Scikit-Learn** | 1.2.0+ | Implementação do RandomForest, StandardScaler e Pipeline |
| **Matplotlib** | 3.7+ | Geração de gráficos estáticos para análise exploratória |
| **Seaborn** | 0.12+ | Visualizações estatísticas (heatmaps, boxplots, regplots) |
| **Plotly** | 5.15.0+ | Gráficos interativos para o dashboard Streamlit |
| **Streamlit** | 1.25.0+ | Desenvolvimento e deploy da interface web |
| **Joblib** | 1.3.0+ | Persistência do modelo treinado (`pipeline.pkl`) e features |

---

## 3. Pré-requisitos

Antes de executar o projeto, certifique-se de ter os seguintes itens instalados e configurados:

### Requisitos de sistema

- **Python 3.10** ou superior
- **pip** (gerenciador de pacotes do Python)
- **Git** (para clonar o repositório)
- **Virtualenv** ou **conda** (recomendado para isolamento de ambiente)

### Arquivos necessários

Os seguintes arquivos devem estar presentes na estrutura de pastas:

| Arquivo | Local | Descrição |
|---|---|---|
| `bd_consolid_22_23_24.csv` | `Dataset/` | Base de dados consolidada da Passos Mágicos (2022–2024) |
| `Passos-magicos-logo.png` | Raiz do projeto | Logo da ONG para a aplicação Streamlit |
| `passos-magicos-icon.ico` | Raiz do projeto | Ícone exibido na aba do navegador |

> ⚠️ **Atenção:** O dataset contém dados sensíveis de alunos. Certifique-se de seguir as diretrizes da **LGPD (Lei Geral de Proteção de Dados)** ao manipular, armazenar e compartilhar essas informações.

---

## 4. Como Executar o Projeto
### Passo 1: Criar e ativar o ambiente virtual  
bash # Windows python -m venv venv venv\Scripts\activate

### Passo 2: Instalar as dependências
pip install --upgrade pip
pip install -r requirements.txt

### Passo 4: Preparar o dataset
mkdir -p Dataset
cp [caminho_do_arquivo]/bd_consolid_22_23_24.csv Dataset/

### Passo 5: Executar o notebook do modelo preditivo
datathon_passos_magicos.ipynbExecute todas as células na ordem. Ao final, os arquivos pipeline.pkl e features.pkl serão gerados na raiz do projeto.

### Passo 6: Executar a aplicação Streamlit
streamlit run app.py

### Passo 7: Deploy no Streamlit Community Cloud (opcional)
Acesse share.streamlit.io
Conecte sua conta do GitHub
Selecione o repositório e o arquivo app.py
Configure o ambiente Python e instale as dependências
Clique em Deploy



## 5. Estrutura do Projeto
```text
datathon_fase_5/
├── Dataset/
│   └── bd_consolid_22_23_24.csv
├── Notebook/
│   └── datathon_passos_magicos.ipynb
├── Streamlit/
│   ├── app.py
│   ├── Passos-magicos-logo.png
│   └── passos-magicos-icon.ico
├── requirements.txt
└── README.md

Descrição dos arquivos

|Arquivo / Pasta|Descrição|
|---|---|
|Dataset/|Contém o arquivo CSV com os dados consolidados de 2022, 2023 e 2024|
|Notebook/|Notebook Jupyter com toda a análise exploratória, respostas às 11 perguntas de negócio e desenvolvimento do modelo|
|app.py|Código-fonte da aplicação Streamlit com 3 páginas, CSS customizado e gráficos interativos|
|pipeline.pkl|Objeto Pipeline serializado (StandardScaler + RandomForestClassifier)|
|features.pkl|Lista de nomes das features utilizadas no treinamento|
|requirements.txt|Lista de bibliotecas Python necessárias para executar o projeto|































