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

nome_tabela = "resultados_base_teste"

# Agora usa engine no Pandas
df = pd.read_sql(f"SELECT * FROM {nome_tabela} ;", engine)

st.dataframe(df)