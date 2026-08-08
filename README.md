# 🔮 Predição de Risco de Defasagem Escolar — Associação Passos Mágicos

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
