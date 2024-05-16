import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import math 

# VOTAÇOES 2020

#Coletando dados do csv da Votacoes_2020
votacao_doismilevinte = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_data_py\Big_data_py\Análise_2020\votacao_candidato-municipio_2020_rj.csv', sep=';', encoding='latin1')

#Contando os cargos
vt = votacao_doismilevinte['ds_cargo'].value_counts()
print('A quantidade de cargos e de pessoas concorrendo no cargo são:', vt) #ds_cargo Vereador:23080, Prefeito:531

#Somando a quantidade de votos e fazendo a média
votacao = math.fsum(votacao_doismilevinte['qt_votos_nom_validos'])
print('A quantidade total de votos totais de 2020 foi de:', votacao) #Quantidade total de votos é de 14629639.0

media_votos = 14629639.0 // 2
print('A média dos votos é de:', media_votos) #A média é de 7314819.0

#Calculando o Outlier
outlier1 = votacao_doismilevinte['qt_votos_nom_validos']
sns.boxplot(outlier1)
plt.show()

# ELEITORES 2020

#Coletando dados do csv de Eleitores_2020
eleitores_doismilevinte = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_data_py\Big_data_py\Análise_2020\202011051250_arq_160443.csv', sep=';', encoding='latin1')

#Mudando o nome das colunas
eleitores_doismilevinte.columns = ['Cod_Municipio','Nome_Municipio','Qtd_Locais', 'Qtd_Zonas', 'Qtd_Seções', 'Qtd_Eleitores']
print(eleitores_doismilevinte.columns) 

#Somando os valores 
eleitores = math.fsum(eleitores_doismilevinte['Qtd_Eleitores'])
print('A quantidade total de eleitores de 2020 foi de:', eleitores) #Quantidade total de eleitores é 12455812.

#Calculando o Outlier
outlier2 = eleitores_doismilevinte['Qtd_Eleitores']
sns.boxplot(outlier2)
plt.show()

#GRÁFICO COMPARATIVO 2020

Eleitores_Aptos_2020 = {'Eleitores': 12455812}
Media_Votos_Recebidos_2020 = {'Media': 7314819.0}

df = {'Eleitores_Aptos': [i for i in Eleitores_Aptos_2020.values()],
      'Media_Votos_Recebidos': [i for i in Media_Votos_Recebidos_2020.values()]}

pd.DataFrame(df).plot.bar(color=['yellow', 'pink'], ec='k', alpha=0.6)
plt.xticks(rotation=360, fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Comparação', fontsize=13)
plt.ylabel('Número', fontsize=13)
plt.show()


