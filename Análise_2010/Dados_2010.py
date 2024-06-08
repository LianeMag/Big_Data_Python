import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import math 

# VOTAÇOES 2010

#Coletando dados do csv da Votacoes_2010
votacao_doismiledez = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2010\votacao_candidato_munzona_2010_RJ.csv', 
                                  sep=';', encoding='latin1')

print(votacao_doismiledez.columns) 
'''olhando as colunas de primeira, temos o seguinte resultado: Index(['DT_GERACAO', 'HH_GERACAO', 'ANO_ELEICAO', 'CD_TIPO_ELEICAO','NM_TIPO_ELEICAO', 'NR_TURNO', 'CD_ELEICAO', 'DS_ELEICAO', 'DT_ELEICAO','TP_ABRANGENCIA',
 'SG_UF', 'SG_UE','NM_UE', 'CD_MUNICIPIO','NM_MUNICIPIO', 'NR_ZONA', 'CD_CARGO', 'DS_CARGO', 'SQ_CANDIDATO','NR_CANDIDATO', 'NM_CANDIDATO', 'NM_URNA_CANDIDATO',
'NM_SOCIAL_CANDIDATO', 'CD_SITUACAO_CANDIDATURA','DS_SITUACAO_CANDIDATURA', 'CD_DETALHE_SITUACAO_CAND','DS_DETALHE_SITUACAO_CAND', 'TP_AGREMIACAO', 'NR_PARTIDO', 'SG_PARTIDO',
'NM_PARTIDO', 'SQ_COLIGACAO', 'NM_COLIGACAO', 'DS_COMPOSICAO_COLIGACAO','CD_SIT_TOT_TURNO', 'DS_SIT_TOT_TURNO', 'ST_VOTO_EM_TRANSITO','QT_VOTOS_NOMINAIS'],dtype='object')'''

#Contando os cargos
vt = votacao_doismiledez['DS_CARGO'].value_counts()
print('A quantidade de cargos e de pessoas concorrendo no cargo são:', vt) #DS_CARGO Deputado Estadual=168132, Deputado Federal=114193, Senador=887, Governador=1578

#Somando a quantidade de votos e fazendo a média
votacao = math.fsum(votacao_doismiledez['QT_VOTOS_NOMINAIS'])
print('A quantidade total de votos totais de 2010 foi de:', votacao) #Quantidade total de votos é de 37582897.0

media_votos = votacao // 4
print('A média dos votos é de:', media_votos) #A média é de 9395724.0

#Calculando o Outlier
outlier1 = votacao_doismiledez['QT_VOTOS_NOMINAIS']
sns.boxplot(outlier1)
plt.show()

# ELEITORES 2010

#Coletando dados do csv de Eleitores_2010
eleitores_doismiledez = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2010\Eleitorado por Município - 23-09-2010 (1).csv', sep=';', encoding='latin1')

'''olhando as colunas de primeira, temos o seguinte resultado: Index(['Cod Municipio', 'Municipio', 
'Qtd Locais SUM', 'Qtd Secoes SUM','Qtd Eleitores SUM'],dtype='object'), os nomes podem melhorar, vamos tratá-los.'''

#Mudando o nome das colunas
eleitores_doismiledez.columns = ['Cod_Municipio','Nome_Municipio','Qtd_Locais', 'Qtd_Secoes', 'Qtd_Eleitores']
print(eleitores_doismiledez.columns) 

#Somando os valores 
eleitores = math.fsum(eleitores_doismiledez['Qtd_Eleitores'])
print('A quantidade total de eleitores de 2010 foi de:', eleitores) #Quantidade total de eleitores é 11589763.0

#Calculando o Outlier
outlier2 = eleitores_doismiledez['Qtd_Eleitores']
sns.boxplot(outlier2)
plt.show()

#GRÁFICO COMPARATIVO 2010

Eleitores_Aptos_2010 = {'Eleitores': eleitores}
Media_Votos_Recebidos_2010 = {'Media': votacao}

df = {'Eleitores_Aptos': [i for i in Eleitores_Aptos_2010.values()],
      'Media_Votos_Recebidos': [i for i in Media_Votos_Recebidos_2010.values()]}

pd.DataFrame(df).plot.bar(color=['yellow', 'pink'], ec='k', alpha=0.6)
plt.xticks(rotation=360, fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Comparação', fontsize=13)
plt.ylabel('Número', fontsize=13)
plt.show()