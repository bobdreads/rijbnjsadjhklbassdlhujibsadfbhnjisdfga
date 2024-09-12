import pandas as pd
import math
from math import comb


def contar_combinacoes_por_colunas(arquivo_excel):
    # Ler o arquivo Excel
    df = pd.read_excel(arquivo_excel)

    # Ignorar as duas primeiras colunas (Número do sorteio e Data)
    # Seleciona todas as colunas a partir da terceira
    df_numeros = df.iloc[:, 2:]

    # Contadores para as combinações desejadas
    contagem_8_pares_7_impares = 0
    contagem_7_pares_8_impares = 0

    def eh_par(numero):
        return numero % 2 == 0

    # Iterar sobre as linhas do DataFrame filtrado
    for index, row in df_numeros.iterrows():
        # Extrair todos os números da linha como uma lista
        numeros = row.values.tolist()

        # Contar números pares e ímpares
        pares = sum(eh_par(num) for num in numeros)
        impares = len(numeros) - pares

        # Contar as combinações conforme o critério
        if pares == 8 and impares == 7:
            contagem_8_pares_7_impares += 1
        elif pares == 7 and impares == 8:
            contagem_7_pares_8_impares += 1

    return contagem_8_pares_7_impares, contagem_7_pares_8_impares


def calcular_probabilidade_acerto(total_numeros, numeros_escolhidos):
    # Determina o número de pares e ímpares
    pares = math.ceil(total_numeros / 2)   # Arredonda para cima
    impares = math.floor(total_numeros / 2)  # Arredonda para baixo

    # Calcula o número de combinações possíveis para os números pares
    combinacoes_pares = math.comb(pares, numeros_escolhidos // 2)

    # Calcula o número de combinações possíveis para os números ímpares
    combinacoes_impares = math.comb(
        impares, numeros_escolhidos - (numeros_escolhidos // 2))

    # A probabilidade de acertar uma combinação específica é o inverso do número de combinações possíveis
    combinacoes_possiveis = combinacoes_pares * combinacoes_impares

    return combinacoes_possiveis


def calcular_probabilidade_sem_combinacoes_utilizadas(probabilidade, arquivo_excel):
    # Ler o arquivo Excel
    df = pd.read_excel(arquivo_excel)

    # Ignorar as duas primeiras colunas (Número do sorteio e Data)
    # Seleciona todas as colunas a partir da terceira
    df_combinacoes = df.iloc[:, 2:]

    # Coletar todas as combinações de 15 números da planilha
    combinacoes_utilizadas = [frozenset(row)
                              for _, row in df_combinacoes.iterrows()]

    # Universo de 25 números (1 a 25)
    universo = set(range(1, 26))

    # Calcular a quantidade de combinações já utilizadas
    combinacoes_utilizadas_unicas = set(combinacoes_utilizadas)
    qtd_combinacoes_utilizadas = len(combinacoes_utilizadas_unicas)

    # Calcular a quantidade de combinações restantes válidas
    combinacoes_validas = probabilidade - qtd_combinacoes_utilizadas

    # Calcular a probabilidade de uma nova combinação estar entre as combinações restantes válidas

    return combinacoes_validas


def verificar_combinacao(arquivo_excel, combinacao_usuario):
    # Ler o arquivo Excel
    df = pd.read_excel(arquivo_excel)

    # Ignorar as duas primeiras colunas (Número do sorteio e Data)
    # Seleciona todas as colunas a partir da terceira
    df_combinacoes = df.iloc[:, 2:]

    # Coletar todas as combinações da planilha
    combinacoes_utilizadas = set(frozenset(row)
                                 for _, row in df_combinacoes.iterrows())

    # Converter a combinação do usuário para um frozenset
    combinacao_usuario_set = frozenset(combinacao_usuario)

    # Verificar se a combinação do usuário está nas combinações utilizadas
    if combinacao_usuario_set in combinacoes_utilizadas:
        return True
    else:
        return False
