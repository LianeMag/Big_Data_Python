import matplotlib.pyplot as plt
import pandas as pd
import math

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

#Gerando o Gráfico Geral

Eleitores_Aptos_2008 = {'Eleitores2008': eleitores2008}
Media_Votos_Recebidos_2008 = {'Media2008': media_votos2008}

Eleitores_Aptos_2010 = {'Eleitores2010': eleitores2010}
Media_Votos_Recebidos_2010 = {'Media2010': media_votos2010}

Eleitores_Aptos_2012 = {'Eleitores2012': eleitores2012}
Media_Votos_Recebidos_2012 = {'Media2012': media_votos2012}

Eleitores_Aptos_2014 = {'Eleitores2014': eleitores2014}
Media_Votos_Recebidos_2014 = {'Media2014': media_votos2014}

Eleitores_Aptos_2016 = {'Eleitores2016': eleitores2016}
Media_Votos_Recebidos_2016 = {'Media2016': media_votos2016}

Eleitores_Aptos_2018 = {'Eleitores2018': eleitores2018}
Media_Votos_Recebidos_2018 = {'Media2018': media_votos2018}

Eleitores_Aptos_2020 = {'Eleitores20200': eleitores2020}
Media_Votos_Recebidos_2020 = {'Media2020': media_votos2020}

df = {'Eleitores_Aptos_2008': [i for i in Eleitores_Aptos_2008.values()],
      'Media_Votos_Recebidos_2008': [i for i in Media_Votos_Recebidos_2008.values()],
      'Eleitores_Aptos_2010': [i for i in Eleitores_Aptos_2010.values()],
      'Media_Votos_Recebidos_2010': [i for i in Media_Votos_Recebidos_2010.values()],
      'Eleitores_Aptos_2012': [i for i in Eleitores_Aptos_2012.values()],
      'Media_Votos_Recebidos_2012': [i for i in Media_Votos_Recebidos_2012.values()],
      'Eleitores_Aptos_2014': [i for i in Eleitores_Aptos_2014.values()],
      'Media_Votos_Recebidos_2014': [i for i in Media_Votos_Recebidos_2014.values()],
      'Eleitores_Aptos_2016': [i for i in Eleitores_Aptos_2016.values()],
      'Media_Votos_Recebidos_2016': [i for i in Media_Votos_Recebidos_2016.values()],
      'Eleitores_Aptos_2018': [i for i in Eleitores_Aptos_2018.values()],
      'Media_Votos_Recebidos_2018': [i for i in Media_Votos_Recebidos_2018.values()],
      'Eleitores_Aptos_2020': [i for i in Eleitores_Aptos_2020.values()],
      'Media_Votos_Recebidos_2020': [i for i in Media_Votos_Recebidos_2020.values()]}

pd.DataFrame(df).plot.bar(color=['yellow', 'pink'], ec='k', alpha=0.6)
plt.xticks(rotation=360, fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Comparação Geral', fontsize=13)
plt.ylabel('Números', fontsize=13)
plt.show()