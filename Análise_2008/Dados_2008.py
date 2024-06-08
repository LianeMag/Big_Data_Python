import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import math 

# VOTAÇOES 2008

#Coletando dados do csv da Votacoes_2008
votacao_doismileoito = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2008\votacao_candidato_munzona_2008_RJ.csv', sep=';', encoding='latin1')

print(votacao_doismileoito.columns) 
'''olhando as colunas de primeira, temos o seguinte resultado: Index(['DT_GERACAO', 'HH_GERACAO', 'ANO_ELEICAO', 'CD_TIPO_ELEICAO','NM_TIPO_ELEICAO', 'NR_TURNO', 
'CD_ELEICAO', 'DS_ELEICAO', 'DT_ELEICAO','TP_ABRANGENCIA', 'SG_UF', 'SG_UE', 'NM_UE', 'CD_MUNICIPIO','NM_MUNICIPIO', 'NR_ZONA', 'CD_CARGO', 'DS_CARGO', 'SQ_CANDIDATO',
'NR_CANDIDATO', 'NM_CANDIDATO', 'NM_URNA_CANDIDATO','NM_SOCIAL_CANDIDATO', 'CD_SITUACAO_CANDIDATURA','DS_SITUACAO_CANDIDATURA', 'CD_DETALHE_SITUACAO_CAND',
'DS_DETALHE_SITUACAO_CAND', 'TP_AGREMIACAO', 'NR_PARTIDO', 'SG_PARTIDO','NM_PARTIDO', 'SQ_COLIGACAO', 'NM_COLIGACAO', 'DS_COMPOSICAO_COLIGACAO',
'CD_SIT_TOT_TURNO', 'DS_SIT_TOT_TURNO', 'ST_VOTO_EM_TRANSITO','QT_VOTOS_NOMINAIS'], dtype='object').'''

#Contando os cargos
vt = votacao_doismileoito['DS_CARGO'].value_counts()
print('A quantidade de cargos e de pessoas concorrendo no cargo são:', vt) #DS_CARGO Vereador: 115175 Prefeito: 2024

#Somando a quantidade de votos e fazendo a média
votacao = math.fsum(votacao_doismileoito['QT_VOTOS_NOMINAIS'])
print('A quantidade total de votantes de 2008 foi de:', votacao) #Quantidade total de votos é de 19792252.0

media_votos = votacao // 2
print('A média dos votos é:', media_votos) #A média é de 9896126.0

#Calculando o Outlier
outlier1 = votacao_doismileoito['QT_VOTOS_NOMINAIS']
sns.boxplot(outlier1)
plt.show()

# ELEITORES 2008

#Coletando dados do csv de Eleitores_2008
eleitores_doismileoito = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2008\Eleitorado­_Município_2008.csv', sep=';', encoding='latin1')

'''olhando as colunas de primeira, temos o seguinte resultado: Index(['Eleitorado por Município (Dados de 30_07_2008)', 
'ANGRA DOS REIS','69', '319', '107867'],dtype='object'), percebe-se que as colunas não tem nome e sim informações, então vamos trata-las'''

#Mudando o nome das colunas
eleitores_doismileoito.columns = ['Cod_Municipio','Nome_Municipio','Qtd_Locais', 'Qtd_Secoes', 'Qtd_Eleitores']
print(eleitores_doismileoito.columns) 

#Somando os valores
eleitores = math.fsum(eleitores_doismileoito['Qtd_Eleitores'])
print('A quantidade total de eleitores de 2008 foi de:', eleitores) #Quantidade total de eleitores é 11259334.0

#Calculando o Outlier
outlier2 = eleitores_doismileoito['Qtd_Eleitores']
sns.boxplot(outlier2)
plt.show()

#GRÁFICO COMPARATIVO 2008

Eleitores_Aptos_2008 = {'Eleitores': eleitores}
Media_Votos_Recebidos_2008 = {'Media': media_votos}

df = {'Eleitores_Aptos': [i for i in Eleitores_Aptos_2008.values()],
      'Media_Votos_Recebidos': [i for i in Media_Votos_Recebidos_2008.values()]}

pd.DataFrame(df).plot.bar(color=['yellow', 'pink'], ec='k', alpha=0.6)
plt.xticks(rotation=360, fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Comparação', fontsize=13)
plt.ylabel('Número', fontsize=13)
plt.show()