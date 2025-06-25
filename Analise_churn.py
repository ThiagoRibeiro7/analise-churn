#Passo 1: Importando a base de dados
import pandas as pd

tabela = pd.read_csv("telecom_users.csv")

# Passo 2: Visualizando a base de dados
tabela = tabela.drop("Unnamed: 0", axis=1)
display(tabela)
# - Entendendo quais as informações estão disponíveis
# - Descobrir os problemas da base de dados

# Passo 3: Tratamento de dados
# - Valores que estão reconhecidos de forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# - Valores vazios
# deletando as colunas vazias
# axis = 0 _> linha ou axis = 1 _> coluna
tabela = tabela.dropna(how="all", axis=1)
# deletando as linhas vazias
tabela = tabela.dropna(how="any", axis=0)

print(tabela.info())

# Passo 4: Análise Inicial
# Como estão os nossos cancelamentos?
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# Passo 5: Análise Mais completa
# comparar cada coluna da minha tabela com a coluna de cancelamento
import plotly.express as px
# etapa 1: criar o gráfico
# percorrendo toda a tabela fazendo a relação com o churn
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    # etapa 2: exibir o gráfico
    grafico.show()

# Com algumas linhas de código é feita uma análise de churn (saída) dos cliente em comparação com cada coluna da tabela
# Conclusão no ReadMe
