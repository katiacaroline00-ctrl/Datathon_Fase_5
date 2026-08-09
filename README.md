# 🔮 Predição de Risco de Defasagem Escolar — Associação Passos Mágicos


> Projeto desenvolvido para o **Datathon da PosTech** (Pós-graduação em Data Analytics), aplicando Machine Learning e Data Analytics aos dados educacionais da Associação Passos Mágicos (2022–2024) para identificar precocemente alunos em risco de defasagem escolar.

**Autora:** Katia Wilkomm  
**Instituição:** PosTech — Data Analytics  
**Case:** Associação Passos Mágicos   
**Vídeo de Apresentação:** https://youtu.be/ahwumbIUD1k 

---

## 📋 Sumário

[1. Descrição Geral](#1-descrição-geral)
[2. Tecnologias Utilizadas](#2-tecnologias-utilizadas)
[3. Pré-requisitos](#3-pré-requisitos)
[4. Como Executar o Projeto](#4-como-executar-o-projeto)
[5. Estrutura do Projeto](#5-estrutura-do-projeto)
[6. Funcionalidades](#6-funcionalidades)
[7. Considerações Finais](#7-consideracoes-finais)

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
Descrição dos arquivos

|Arquivo / Pasta|Descrição|
|---|---|
|Dataset/|Contém o arquivo CSV com os dados consolidados de 2022, 2023 e 2024|
|Notebook/|Notebook Jupyter com toda a análise exploratória, respostas às 11 perguntas de negócio e desenvolvimento do modelo|
|app.py|Código-fonte da aplicação Streamlit com 3 páginas, CSS customizado e gráficos interativos|
|pipeline.pkl|Objeto Pipeline serializado (StandardScaler + RandomForestClassifier)|
|features.pkl|Lista de nomes das features utilizadas no treinamento|
|requirements.txt|Lista de bibliotecas Python necessárias para executar o projeto|

## 6. Funcionalidades
### 6.1 Analise Exploratoria de Dados (11 Perguntas de Negocio)
O notebook responde as 11 perguntas definidas no enunciado do Datathon:
|#|Pergunta|Indicador|
|---|---|---|
|1|Qual e o perfil geral de defasagem dos alunos e como evolui ao longo dos anos?|IAN|
|2|O desempenho academico medio esta melhorando, estagnado ou caindo ao longo das fases e anos?|IDA|
|3|O grau de engajamento tem relacao direta com o desempenho e o ponto de virada?|IEG|
|4|As percepcoes dos alunos sobre si mesmos sao coerentes com seu desempenho real?|IAA|
|5|Ha padroes psicossociais que antecedem quedas de desempenho ou engajamento?|IPS|
|6|As avaliacoes psicopedagogicas confirmam ou contradizem a defasagem?|IPP|
|7|Quais comportamentos mais influenciam o Ponto de Virada ao longo do tempo?|IPV|
|8|Quais combinacoes de indicadores elevam mais a nota global (INDE)?|INDE|
|9|Quais padroes permitem identificar alunos em risco antes da queda no desempenho?|ML|
|10|Os indicadores mostram melhora consistente ao longo do ciclo nas diferentes fases?|Pedras|
|11|Insights adicionais (instituicao, genero, idade, tempo na ONG)|--|

### 6.2 Modelo Preditivo
Algoritmo: RandomForestClassifier  
Pipeline de pre-processamento:  
StandardScaler -> RandomForestClassifier  
Hiperparametros:  
|Parametro|Valor|Justificativa|
|---|---|---|
|n_estimators|200|Numero de arvores na floresta|
|max_depth|10|Profundidade maxima (controle de overfitting)|
|min_samples_split|5|Minimo de amostras para divisao de no|
|class_weight|balanced|Tratamento de desbalanceamento de classes|
|random_state|42|Reprodutibilidade|

Divisão dos dados:  
Treino: anos 2022 e 2023  
Teste: ano 2024 (divisao temporal para simular uso real)  
Variavel-alvo: risco_defasagem = (defas < 0).astype(int)  

Features utilizadas:
•	Numericas: IAA, IEG, IPS, IDA, IPV  
•	Categoricas: Pedra, Instituicao padronizada (one-hot encoding com drop_first=True)  
Features excluidas:  
•	fase e fase_ideal -> removidas por vazamento de dados (data leakage)  
•	ipp -> excluida por inconsistencia (todos os valores = 0 em 2022)  
Metricas de avaliacao (conjunto de teste - 2024):  
|Metrica|Valor|Interpretacao|
|---|---|---|
|ROC-AUC|**0,77**|Capacidade discriminativa satisfatoria|
|Recall (Risco)|**0,64**|64% dos alunos em risco corretamente identificados|
|Precision (Risco)|**0,79**|79% das predicoes de risco sao corretas|
|Average Precision|**0,83**|Desempenho robusto considerando desbalanceamento|

Features mais importantes:  
1.IDA - Desempenho Academico  
2.IPV - Ponto de Virada  
3.Pedra: Topazio - Categoria de maior desempenho  
4.IEG - Engajamento  

### 6.3 Aplicacao Streamlit

A aplicação possui 3 paginas acessíveis via sidebar: 
#### Pagina 1 - Sobre a Passos Magicos
'- Historia da ONG com timeline interativa  
'-Missao, Visao e Valores  
'-Tabela de indicadores educacionais (INDE, IAA, IEG, IPS, IDA, IPV, IAN, IPP)  
'-Sistema de classificacao por Pedras (Quartzo, Agata, Ametista, Topazio)  
'-Parcerias e atuacao (Escola Publica, Bolsas, Empresas Parceiras)  
#### Pagina 2 - Predições e Indicadores
'-Filtros interativos: ano, instituicao, pedra, genero, fase, idade, ano de ingresso, faixa de INDE  
'-Metricas de destaque: total de registros e % em risco  
'-9 graficos interativos (Plotly):   
##### 1. Risco de defasagem por ano (barras)
##### 2.Distribuicao por Pedra (donut chart)
##### 3.Boxplot do INDE por Pedra
##### 4.Histograma do INDE
##### 5.Evolucao dos indicadores por ano (linhas)
##### 6.Matriz de correlacao entre indicadores (heatmap)
##### 7.Radar de indicadores por Pedra
##### 8.Scatter IDA vs INDE
##### 9.Media de indicadores por instituicao (barras agrupadas)
#### Pagina 3 - Metricas do Modelo
'-Configuracao do modelo (algoritmo, hiperparametros, divisao treino/teste)  
'-Metricas de performance (ROC-AUC, Recall, Precision, Average Precision)  
'-Top 10 features mais importantes (grafico de barras)  
'-Considerações finais e limitações  

## 7.Considerações Finais
Este projeto foi desenvolvido como parte do Datathon da PosTech e tem como propósito contribuir com a missão da Associação Passos Mágicos de transformar a vida de crianças e jovens por meio da educação.

A solução entregue não é apenas um exercício acadêmico, mas uma ferramenta prática de apoio à decisão que coloca a ciência de dados a serviço da equipe pedagógica. Ao identificar precocemente alunos em risco de defasagem, a ONG pode direcionar seus recursos e intervenções de forma mais eficiente, potencializando o impacto de suas ações.

Licença: Este projeto é de uso acadêmico e não possui fins comerciais.






























