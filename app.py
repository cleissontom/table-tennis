import pandas as pd
import psycopg2
import streamlit as st

# 🔹 Configuração da conexão (troque pelos seus dados)
DB_HOST = st.secrets["db"]["host"]
DB_NAME = st.secrets["db"]["dbname"]
DB_USER = st.secrets["db"]["user"]
DB_PASS = st.secrets["db"]["password"]
DB_PORT = st.secrets["db"]["port"]

def get_data():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )
    df = pd.read_sql("SELECT * FROM resultados_base_teste", conn)
    conn.close()
    return df

st.title("Visualização de Tabela do Banco")
df = get_data()
st.dataframe(df)  # Exibe a tabela interativa
