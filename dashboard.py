import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(layout='wide', page_title="Homicídios no Ceará")

# Função para carregar dados com cache
@st.cache_data
def load_data():
    url = 'https://www.sspds.ce.gov.br/wp-content/uploads/sites/24/2025/03/CVLI_2009-2024.xlsx'
    df = pd.read_excel(url)
    df["Data"] = pd.to_datetime(df['Data'])  # manter como datetime
    return df

# Carrega os dados
df = load_data()

# Agrupar homicídios por mês
homicides_month = df.groupby(pd.Grouper(key='Data', freq='M')).size().reset_index(name='num_homicides')

# Formatar mês/ano para o eixo X
homicides_month['MesAno'] = homicides_month['Data'].dt.strftime('%m/%Y')

# Gráfico de linha contínuo
fig_homicides_month = px.line(
    homicides_month,
    x='MesAno',
    y='num_homicides',
    markers=True,
    title='Homicídios Mensais (2009-2024)'
)

# Layout do gráfico para melhor visualização
fig_homicides_month.update_layout(
    xaxis_title="Mês/Ano",
    yaxis_title="Número de Homicídios",
    xaxis_tickangle=-45
)

# Exibir gráfico no Streamlit
st.plotly_chart(fig_homicides_month, use_container_width=True)


