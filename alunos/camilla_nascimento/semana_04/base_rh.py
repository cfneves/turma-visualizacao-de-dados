
import pandas as pd

# 1. Caminho exato do seu arquivo CSV
CAMINHO = r'C:\Users\Milla\Documents\turma-visualizacao-de-dados\datasets\base_rh.csv'

# 2. Carregando os dados (A "Mágica" acontece aqui)
# sep=';' -> Porque o TOTVS usa ponto-e-vírgula
# encoding='cp1252' -> Para aceitar acentos (Produção, Gestão, etc)
# decimal=',' -> Para o Python entender que 1500,50 é um número

df = pd.read_csv(CAMINHO, sep=';', encoding='cp1252', decimal=',')
# 3. Verificando se os dados foram carregados corretamente
print(df.head())  # Mostra as primeiras linhas do DataFrame
print(df.info())  # Mostra informações sobre as colunas e tipos de dados
print(df.describe())  # Mostra estatísticas descritivas para colunas numéricas

# CONFIGURAÇÃO DE EXIBIÇÃO: Essas linhas removem os limites do terminal
pd.set_option('display.max_rows', 1000)    # Força mostrar até 1000 linhas
pd.set_option('display.max_columns', None) # Força mostrar todas as colunas
pd.set_option('display.width', None)       # Ajusta a largura para não quebrar a linha

# 1. Caminho do arquivo
CAMINHO = r'C:\Users\Milla\Documents\turma-visualizacao-de-dados\datasets\base_rh.csv'

# 2. Lendo o arquivo
df = pd.read_csv(CAMINHO, sep=';', encoding='cp1252', decimal=',')

# 3. Exibindo as 1000 linhas
print("--- RELATÓRIO COMPLETO: 1000 LINHAS ---")
print(df.head(1000))