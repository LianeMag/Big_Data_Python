import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import math 

# VOTAÇOES 2018

#Coletando dados do csv da Votacoes_2018
votacao_doismiledezoito = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2018\votacao_candidato-municipio_2018_rj.csv', sep=';', encoding='latin1')

#Contando os cargos
vt = votacao_doismiledezoito['ds_cargo'].value_counts()
print('A quantidade de cargos e de pessoas concorrendo no cargo são:', vt) #ds_cargo Deputado Estadual:206264, Deputado Federal:96232, Senador:1380, Presidente:1196, Governador:920

#Somando a quantidade de votos e fazendo a média
votacao = math.fsum(votacao_doismiledezoito['qt_votos_nom_validos'])
print('A quantidade total de votos totais de 2018 foi de:', votacao) #Quantidade total de votos é de 44439124.0

media_votos = votacao // 5
print('A média dos votos é de:', media_votos) #A média é de 8887824.0

#Calculando o Outlier
outlier1 = votacao_doismiledezoito['qt_votos_nom_validos']
sns.boxplot(outlier1)
plt.show()

# ELEITORES 2018

#Coletando dados do csv de Eleitores_2018
eleitores_doismiledezoito = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2018\Eleitorado por Município - 02-09-2018.csv', sep=';', encoding='latin1')

'''olhando as colunas de primeira, os nomes podem melhorar, vamos tratá-los.'''

#Mudando o nome das colunas
eleitores_doismiledezoito.columns = ['Cod_Municipio','Nome_Municipio','Qtd_Locais', 'Qtd_Secoes', 'Qtd_Eleitores']
print(eleitores_doismiledezoito.columns) 

#Somando os valores 
eleitores = math.fsum(eleitores_doismiledezoito['Qtd_Eleitores'])
print('A quantidade total de eleitores de 2018 foi de:', eleitores) #Quantidade total de eleitores é 12408340.0

#Calculando o Outlier
outlier2 = eleitores_doismiledezoito['Qtd_Eleitores']
sns.boxplot(outlier2)
plt.show()

#GRÁFICO COMPARATIVO 2018

Eleitores_Aptos_2018 = {'Eleitores': eleitores}
Media_Votos_Recebidos_2018 = {'Media': media_votos}

df = {'Eleitores_Aptos': [i for i in Eleitores_Aptos_2018.values()],
      'Media_Votos_Recebidos': [i for i in Media_Votos_Recebidos_2018.values()]}

pd.DataFrame(df).plot.bar(color=['yellow', 'pink'], ec='k', alpha=0.6)
plt.xticks(rotation=360, fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Comparação', fontsize=13)
plt.ylabel('Número', fontsize=13)
plt.show()


