import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np

#ARQUIVOS

#2008

votacao_doismileoito = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2008\votacao_candidato_munzona_2008_RJ.csv',
                                    sep=';', encoding='latin1')
vt2008 = votacao_doismileoito['DS_CARGO'].value_counts()
votacao2008 = math.fsum(votacao_doismileoito['QT_VOTOS_NOMINAIS'])
media_votos2008 = votacao2008 // 2

eleitores_doismileoito = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2008\Eleitorado­_Município_2008.csv', 
                                     sep=';', encoding='latin1')
eleitores_doismileoito.columns = ['Cod_Municipio','Nome_Municipio','Qtd_Locais', 'Qtd_Secoes', 'Qtd_Eleitores']
eleitores2008 = math.fsum(eleitores_doismileoito['Qtd_Eleitores'])

#2010

votacao_doismiledez = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2010\votacao_candidato_munzona_2010_RJ.csv', 
                                  sep=';', encoding='latin1')
vt2010 = votacao_doismiledez['DS_CARGO'].value_counts()
votacao2010 = math.fsum(votacao_doismiledez['QT_VOTOS_NOMINAIS'])
media_votos2010 = votacao2010 // 4

eleitores_doismiledez = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2010\Eleitorado por Município - 23-09-2010 (1).csv',
                                     sep=';', encoding='latin1')
eleitores_doismiledez.columns = ['Cod_Municipio','Nome_Municipio','Qtd_Locais', 'Qtd_Secoes', 'Qtd_Eleitores']
eleitores2010 = math.fsum(eleitores_doismiledez['Qtd_Eleitores'])

#2012

votacao_doismiledoze = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_python\Análise_2012\votacao_candidato-municipio_2012_rj.csv', 
                                   sep=';', encoding='latin1')
vt = votacao_doismiledoze['ds_cargo'].value_counts()
votacao2012 = math.fsum(votacao_doismiledoze['qt_votos_nom_validos'])
media_votos2012 = votacao2012 // 2

eleitores_doismiledoze = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2012\Eleitorado por Município - 20-09-2012.csv', 
                                     sep=';', encoding='latin1')
eleitores_doismiledoze.columns = ['Cod_Municipio','Nome_Municipio','Qtd_Locais', 'Qtd_Secoes', 'Qtd_Eleitores']
eleitores2012 = math.fsum(eleitores_doismiledoze['Qtd_Eleitores'])

#2014

votacao_doismilequatorze = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2014\votacao_candidato-municipio_2014_rj.csv', 
                                       sep=';', encoding='latin1')
vt = votacao_doismilequatorze['ds_cargo'].value_counts()
votacao2014 = math.fsum(votacao_doismilequatorze['qt_votos_nom_validos'])
media_votos2014 = votacao2014 // 5

eleitores_doismilequatorze = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2014\Eleitorado por Município 12-08-2014.csv', 
                                         sep=';', encoding='latin1')
eleitores_doismilequatorze.columns = ['Cod_Municipio','Nome_Municipio','Qtd_Locais', 'Qtd_Secoes', 'Qtd_Eleitores', 'Num', 'Num']
eleitores2014 = math.fsum(eleitores_doismilequatorze['Qtd_Eleitores'])

#2016

votacao_doismiledezesseis = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2016\votacao_candidato-municipio_2016_rj.csv', 
                                        sep=';', encoding='latin1')
vt2016 = votacao_doismiledezesseis['ds_cargo'].value_counts()
votacao2016 = math.fsum(votacao_doismiledezesseis['qt_votos_nom_validos'])
media_votos2016 = votacao2016 // 2


eleitores_doismiledezesseis = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2016\Eleitorado por Município - 11.07.2016.csv', 
                                          sep=';', encoding='latin1')
eleitores_doismiledezesseis.columns = ['Cod_Municipio','Nome_Municipio','Qtd_Locais', 'Qtd_Secoes', 'Qtd_Eleitores']
eleitores2016 = math.fsum(eleitores_doismiledezesseis['Qtd_Eleitores'])

#2018

votacao_doismiledezoito = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2018\votacao_candidato-municipio_2018_rj.csv', 
                                      sep=';', encoding='latin1')
vt2018 = votacao_doismiledezoito['ds_cargo'].value_counts()
votacao2018 = math.fsum(votacao_doismiledezoito['qt_votos_nom_validos'])
media_votos2018 = votacao2018 // 5

eleitores_doismiledezoito = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2018\Eleitorado por Município - 02-09-2018.csv', 
                                        sep=';', encoding='latin1')
eleitores_doismiledezoito.columns = ['Cod_Municipio','Nome_Municipio','Qtd_Locais', 'Qtd_Secoes', 'Qtd_Eleitores']
eleitores2018 = math.fsum(eleitores_doismiledezoito['Qtd_Eleitores'])

#2020

votacao_doismilevinte = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2020\votacao_candidato-municipio_2020_rj.csv', 
                                    sep=';', encoding='latin1')
vt2020 = votacao_doismilevinte['ds_cargo'].value_counts()
votacao2020 = math.fsum(votacao_doismilevinte['qt_votos_nom_validos'])
media_votos2020 = votacao2020 // 2

eleitores_doismilevinte = pd.read_csv(r'C:\Users\Liane\Documents\GitHub\Big_Data_Python\Análise_2020\202011051250_arq_160443.csv', 
                                      sep=';', encoding='latin1')
eleitores_doismilevinte.columns = ['Cod_Municipio','Nome_Municipio','Qtd_Locais', 'Qtd_Zonas', 'Qtd_Seções', 'Qtd_Eleitores']
eleitores2020 = math.fsum(eleitores_doismilevinte['Qtd_Eleitores'])

#Gerando a regressão linear

X = np.array([eleitores2008, eleitores2010, eleitores2012, eleitores2014, eleitores2016, eleitores2018, eleitores2020]) #Var independente Eleitores
y = np.array([media_votos2008, media_votos2010, media_votos2012, media_votos2014, media_votos2016, media_votos2018, media_votos2020]) #Var dependente Média Votos

#Calcula a r. linear simples
c_a, inter = np.polyfit(X, y, 1)

#Coeficientes da regressão
print(f'Coeficiente Angular: {c_a}')
print(f'Intercepto: {inter}')

#Cria previsões usando a equação da regressão

y_pred = c_a * X + inter
print(y_pred)

plt.scatter(X, y, label='Dados')
plt.plot(X, y_pred, color='Pink', linewidth=2, label='Linha de Regressão')
plt.xlabel('Eleitores Anuais (X)')
plt.ylabel('Média Votos Anuais (y)')
plt.legend()
plt.title('Regressão Linear das Eleições')
plt.grid(True)
plt.show()