import streamlit as st
import pandas as pd

st.set_page_config(page_title="site de estoque")

# Função para carregar dados
@st.cache
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela

# Configurações iniciais da barra lateral
st.sidebar.title("Menu")
aba_selecionada = st.sidebar.radio("Selecione uma aba", ["Dashboard", "Gráficos de Café"])

# Carrega os dados
dados = carregar_dados()

if aba_selecionada == "Dashboard":
    with st.container():
        st.subheader("Seja bem vindo")
        st.title("CABOFÉ")
        st.write("Informações de contratos fechados pela Cabofé")
        st.write("Melhor café da região dos lagos [Clique aqui](https://www.abecafe.com.br/)")

    with st.container():
        st.write("---")
        qtde_dias = st.selectbox("Selecione o período", ["7D", "15D", "30D", "60D"])
        num_dias = int(qtde_dias.replace("D", ""))
        dados_filtrados = dados[-num_dias:]
        st.area_chart(dados_filtrados, x="Venda", y="Produtos")

elif aba_selecionada == "Gráficos de Café":
    st.title("Gráficos de Café")
    # Aqui você pode adicionar os gráficos específicos relacionados ao café
    # Por exemplo:
    st.write("Aqui estão os gráficos sobre café:")
    # Adicione seus gráficos relacionados ao café aqui

