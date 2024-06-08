import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import math 

# VOTAÇOES 2014

#Coletando dados do csv da Votacoes_2014
votacao_doismilequatorze = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2014\votacao_candidato-municipio_2014_rj.csv', sep=';', encoding='latin1')

'''olhando as colunas de primeira, temos o seguinte resultado: Index(['sg_uf', 'nm_municipio', 'cd_cargo', 'ds_cargo', 'nr_candidato',
'nm_candidato', 'nm_urna_candidato', 'sg_partido','ds_composicao_coligacao', 'nr_turno', 'ds_sit_totalizacao','dt_ult_totalizacao', 'sg_ue', 'sq_candidato',
'nm_tipo_destinacao_votos', 'sq_eleicao_divulga', 'pc_votos_validos','qt_votos_nom_validos', 'qt_votos_concorrentes'], dtype='object')'''

#Contando os cargos
vt = votacao_doismilequatorze['ds_cargo'].value_counts()
print('A quantidade de cargos e de pessoas concorrendo no cargo são:', vt) #ds_cargo Deputado Estadual:169188, Deputado Federal:87492, Presidente:1012, Senador:736, Governador:644

#Somando a quantidade de votos e fazendo a média
votacao = math.fsum(votacao_doismilequatorze['qt_votos_nom_validos'])
print('A quantidade total de votos totais de 2014 foi de:', votacao) #Quantidade total de votos é de 37960865.0

media_votos = votacao // 5
print('A média dos votos é de:', media_votos) #A média é de 7592173.0

#Calculando o Outlier
outlier1 = votacao_doismilequatorze['qt_votos_nom_validos']
sns.boxplot(outlier1)
plt.show()

# ELEITORES 2014

#Coletando dados do csv de Eleitores_2014
eleitores_doismilequatorze = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2014\Eleitorado por Município 12-08-2014.csv', sep=';', encoding='latin1')

'''olhando as colunas de primeira, os nomes podem melhorar, vamos tratá-los.'''

#Mudando o nome das colunas
eleitores_doismilequatorze.columns = ['Cod_Municipio','Nome_Municipio','Qtd_Locais', 'Qtd_Secoes', 'Qtd_Eleitores', 'Num', 'Num']
print(eleitores_doismilequatorze.columns) 

#Somando os valores 
eleitores = math.fsum(eleitores_doismilequatorze['Qtd_Eleitores'])
print('A quantidade total de eleitores de 2014 foi de:', eleitores) #Quantidade total de eleitores é 12141145.0

#Calculando o Outlier
outlier2 = eleitores_doismilequatorze['Qtd_Eleitores']
sns.boxplot(outlier2)
plt.show()

#GRÁFICO COMPARATIVO 2014

Eleitores_Aptos_2014 = {'Eleitores': eleitores}
Media_Votos_Recebidos_2014 = {'Media': votacao}

df = {'Eleitores_Aptos': [i for i in Eleitores_Aptos_2014.values()],
      'Media_Votos_Recebidos': [i for i in Media_Votos_Recebidos_2014.values()]}

pd.DataFrame(df).plot.bar(color=['yellow', 'pink'], ec='k', alpha=0.6)
plt.xticks(rotation=360, fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Comparação', fontsize=13)
plt.ylabel('Número', fontsize=13)
plt.show()
