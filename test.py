import streamlit as st
import pandas as pd

st.set_page_config(page_title="site de estoque")

with st.container():
    st.subheader("Seja bem vindo")
    st.title("CABOFÉ")
    st.write("Informações de contratos fechados pela Cabofé")
    st.write("Melhor café da região dos lagos [Clique aqui](https://www.abecafe.com.br/)")
@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela

with st.container():
    st.write("---")
    dados = carregar_dados()
    qtde_dias = st.selectbox("Selecione o produto", ["7D", "15D", "30D", "60D"])
    num_dias = int(qtde_dias.replace("D","" ))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x="Venda", y="Produtos")

