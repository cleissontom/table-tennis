import pandas as pd
import psycopg2
import streamlit as st
from sqlalchemy import create_engine


# 🔹 Configuração da conexão (troque pelos seus dados)
DB_HOST = st.secrets["db"]["host"]
DB_NAME = st.secrets["db"]["dbname"]
DB_USER = st.secrets["db"]["user"]
DB_PASS = st.secrets["db"]["password"]
DB_PORT = st.secrets["db"]["port"]

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")


def color_rows(row):
    return ['background-color: #f2f2f2' if row.name % 2 == 0 else 'background-color: #ffffff'] * len(row)




st.header('Resultado Geral')
nome_tabela = 'vw_total_geral'
df = pd.read_sql(f"SELECT * FROM {nome_tabela} ;", engine)
st.dataframe(df,hide_index=True)


st.subheader('Resultado ultimos dias')
nome_tabela = 'vw_ultimos_resultados_diarios'
df = pd.read_sql(f"SELECT * FROM {nome_tabela} ;", engine)
st.dataframe(df,hide_index=True)

st.subheader('Resultado ultimas apostas')
nome_tabela = 'vw_ultimos_resultados'
df = pd.read_sql(f"SELECT * FROM {nome_tabela} ;", engine)
st.markdown(
    df.to_html(),
    unsafe_allow_html=True
)

