import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import math 

# VOTAÇOES 2012

#Coletando dados do csv da Votacoes_2012
votacao_doismiledoze = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_python\Análise_2012\votacao_candidato-municipio_2012_rj.csv', sep=';', encoding='latin1')

'''olhando as colunas de primeira, temos o seguinte resultado: Index(['sg_uf', 'nm_municipio', 'cd_cargo', 'ds_cargo', 'nr_candidato',
'nm_candidato', 'nm_urna_candidato', 'sg_partido','ds_composicao_coligacao', 'nr_turno', 'ds_sit_totalizacao','dt_ult_totalizacao', 'sg_ue', 'sq_candidato',
'nm_tipo_destinacao_votos', 'sq_eleicao_divulga', 'pc_votos_validos','qt_votos_nom_validos', 'qt_votos_concorrentes'], dtype='object')'''

#Contando os cargos
vt = votacao_doismiledoze['ds_cargo'].value_counts()
print('A quantidade de cargos e de pessoas concorrendo no cargo são:', vt) #ds_cargo Vereador: 19377, Prefeito: 364

#Somando a quantidade de votos e fazendo a média
votacao = math.fsum(votacao_doismiledoze['qt_votos_nom_validos'])
print('A quantidade total de votos totais de 2012 foi de:', votacao) #Quantidade total de votos é de 16179697.0

media_votos = votacao // 2
print('A média dos votos é de:', media_votos) #A média é de 8089848.0

#Calculando o Outlier
outlier1 = votacao_doismiledoze['qt_votos_nom_validos']
sns.boxplot(outlier1)
plt.show()

# ELEITORES 2012

#Coletando dados do csv de Eleitores_2012
eleitores_doismiledoze = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2012\Eleitorado por Município - 20-09-2012.csv', sep=';', encoding='latin1')

#Mudando o nome das colunas
eleitores_doismiledoze.columns = ['Cod_Municipio','Nome_Municipio','Qtd_Locais', 'Qtd_Secoes', 'Qtd_Eleitores']
print(eleitores_doismiledoze.columns)

#Somando os valores
eleitores = math.fsum(eleitores_doismiledoze['Qtd_Eleitores'])
print('A quantidade total de eleitores de 2012 foi de:', eleitores) #Quantidade total de eleitores é 11893309.0

#Calculando o Outlier
outlier2 = eleitores_doismiledoze['Qtd_Eleitores']
sns.boxplot(outlier2)
plt.show()

#GRÁFICO COMPARATIVO 2012

Eleitores_Aptos_2012 = {'Eleitores': eleitores}
Media_Votos_Recebidos_2012 = {'Media': media_votos}

df = {'Eleitores_Aptos': [i for i in Eleitores_Aptos_2012.values()],
      'Media_Votos_Recebidos': [i for i in Media_Votos_Recebidos_2012.values()]}

pd.DataFrame(df).plot.bar(color=['yellow', 'pink'], ec='k', alpha=0.6)
plt.xticks(rotation=360, fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Comparação', fontsize=13)
plt.ylabel('Número', fontsize=13)
plt.show()
