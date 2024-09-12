import streamlit as st
import plotly.express as px
from dataset import dados
from utils import *

# streamlit run app.py

st.set_page_config(layout='wide')
st.title('Dashboard de Loteria :ticket:')

contar_combinacoes_por_colunas('Dados/jogos.xlsx')

aba1, aba2 = st.tabs(['Dataset', 'Resultados'])
with aba1:
    st.dataframe(dados)
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        contagem_8_7, contagem_7_8 = contar_combinacoes_por_colunas(
            'Dados/jogos.xlsx')
        st.write(f"Combinacões com 8 pares e 7 ímpares: {contagem_8_7}")
        st.write(f"Combinacões com 7 pares e 8 ímpares: {contagem_7_8}")

        st.title("Verificação de Combinação de 15 Números")
        entrada_combinacao = st.text_input(
            "Digite sua combinação de 15 números separados por vírgula (ex: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)")
        if entrada_combinacao:
            try:
                # Converter a entrada do usuário para uma lista de números inteiros
                combinacao_usuario = list(
                    map(int, entrada_combinacao.split(',')))

                # Verificar se a combinação tem exatamente 15 números
                if len(combinacao_usuario) != 15:
                    st.error("A combinação deve conter exatamente 15 números.")
                else:
                    # Verificar se a combinação já foi usada
                    combinacao_usada = verificar_combinacao(
                        'Dados/jogos.xlsx', combinacao_usuario)

                    if combinacao_usada:
                        st.write("Essa combinação já foi usada.")
                    else:
                        st.write("Essa combinação ainda não foi usada.")

            except ValueError:
                st.error(
                    "Por favor, insira apenas números inteiros separados por vírgula.")
            except Exception as e:
                st.error(f"Erro ao processar o arquivo: {e}")

    with coluna2:
        total_numeros = 25  # Total de números disponíveis
        numeros_escolhidos = 15
        probabilidade = calcular_probabilidade_acerto(
            total_numeros, numeros_escolhidos)
        probabilidade_atual = calcular_probabilidade_sem_combinacoes_utilizadas(
            probabilidade, 'Dados/jogos.xlsx')

        st.write(f"A probabilidade de acertar a combinação específica é: {
                 probabilidade:,}")
        st.write(f"Probabilidade de acerto sem repetição é de: {
                 probabilidade_atual:,}")
