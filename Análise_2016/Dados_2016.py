import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import math 

# VOTAÇOES 2016

#Coletando dados do csv da Votacoes_2016
votacao_doismiledezesseis = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2016\votacao_candidato-municipio_2016_rj.csv', sep=';', encoding='latin1')

#Contando os cargos
vt = votacao_doismiledezesseis['ds_cargo'].value_counts()
print('A quantidade de cargos e de pessoas concorrendo no cargo são:', vt) #ds_cargo Vereador:19801, Prefeito:398

#Somando a quantidade de votos e fazendo a média
votacao = math.fsum(votacao_doismiledezesseis['qt_votos_nom_validos'])
print('A quantidade total de votos totais de 2016 foi de:', votacao) #Quantidade total de votos é de 15805468.0

media_votos = votacao // 2
print('A média dos votos é de:', media_votos) #A média é de 7902734.0

#Calculando o Outlier
outlier1 = votacao_doismiledezesseis['qt_votos_nom_validos']
sns.boxplot(outlier1)
plt.show()

# ELEITORES 2016

#Coletando dados do csv de Eleitores_2016
eleitores_doismiledezesseis = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2016\Eleitorado por Município - 11.07.2016.csv', sep=';', encoding='latin1')

#Mudando o nome das colunas
eleitores_doismiledezesseis.columns = ['Cod_Municipio','Nome_Municipio','Qtd_Locais', 'Qtd_Secoes', 'Qtd_Eleitores']
print(eleitores_doismiledezesseis.columns) 

#Somando os valores 
eleitores = math.fsum(eleitores_doismiledezesseis['Qtd_Eleitores'])
print('A quantidade total de eleitores de 2016 foi de:', eleitores) #Quantidade total de eleitores é 12414879.0

#Calculando o Outlier
outlier2 = eleitores_doismiledezesseis['Qtd_Eleitores']
sns.boxplot(outlier2)
plt.show()

#GRÁFICO COMPARATIVO 2016

Eleitores_Aptos_2016 = {'Eleitores': eleitores}
Media_Votos_Recebidos_2016 = {'Media': media_votos}

df = {'Eleitores_Aptos': [i for i in Eleitores_Aptos_2016.values()],
      'Media_Votos_Recebidos': [i for i in Media_Votos_Recebidos_2016.values()]}

pd.DataFrame(df).plot.bar(color=['yellow', 'pink'], ec='k', alpha=0.6)
plt.xticks(rotation=360, fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Comparação', fontsize=13)
plt.ylabel('Número', fontsize=13)
plt.show()
