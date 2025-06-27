# Previsão de Churn em Empresa de TeleCom

- Descrição do Problema: A empresa em que trabalho atua no setor de telecomunicações e oferece serviços como internet e telefone. Nos últimos anos, identificamos um índice de churn (evasão de clientes) superior a 26%, o que representa uma perda financeira significativa — somando-se a milhões de reais por ano.

A retenção de clientes se tornou uma prioridade estratégica da empresa, e por isso desenvolvemos esse projeto com foco em identificar padrões e prever quais clientes estão propensos a cancelar os serviços.

- Objetivo: Desenvolver um modelo de machine learning capaz de prever o churn de clientes, com o objetivo de antecipar cancelamentos e orientar ações proativas de retenção.

- Dados Utilizados: Histórico de clientes dos últimos anos / Dados Demográficos / Tipo de Contrato / Tipo de Serviço / Estado Civil / Forma de Pagamento/ Etc.

- Metodologia: Análise exploratória de dados (EDA) / Limpeza e tratamento de dados / Feature Engineering / Modelagem preditiva / Avaliação de desempenho / Geração de insights para o time de negócio.   

- Tecnologias Utilizadas: Python (Pandas / Plotly.express)

Com algumas linhas de código, consegui plotar gráficos que fazem uma relação do churn para cada um dos tipos de dados utilizados, e fazendo a análise tem-se a conclusão:
- Resultados e Ações:
- Clientes com contrato mensal tem MUITO mais chance de cancelar:
    - Podemos fazer promoções para o cliente ir para o contrato anual
- Familias maiores tendem a cancelar menos do que famílias menores
    - Podemos fazer promoções pra pessoa pegar uma linha adicional de telefone
- MesesComoCliente baixos tem MUITO cancelamento. Clientes com pouco tempo como cliente tendem a cancelar muito
    - A primeira experiência do cliente na operadora pode ser ruim
    - Talvez a captação de clientes tá trazendo clientes desqualificados
    - Ideia: a gente pode criar incentivo pro cara ficar mais tempo como cliente
- Quanto mais serviços o cliente tem, menos chance dele cancelar
    - podemos fazer promoções com mais serviços pro cliente
 - Tem alguma coisa no nosso serviço de Fibra que tá fazendo os clientes cancelarem
    - Agir sobre a fibra
- Clientes no boleto tem MUITO mais chance de cancelar, então temos que fazer alguma ação para eles irem para as outras formas de pagamento
