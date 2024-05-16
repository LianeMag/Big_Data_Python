import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


Eleitores_Aptos_2008 = {'Eleitores': 11259334.0}
Media_Votos_Recebidos_2008 = {'Media': 9896126.0}

Eleitores_Aptos_2010 = {'Eleitores1': 11589763.0}
Media_Votos_Recebidos_2010 = {'Media1': 9395724.0}

Eleitores_Aptos_2012 = {'Eleitores2': 11893309.0}
Media_Votos_Recebidos_2012 = {'Media2': 8089848.0}

Eleitores_Aptos_2014 = {'Eleitores3': 12141145.0}
Media_Votos_Recebidos_2014 = {'Media3': 7592173.0}

Eleitores_Aptos_2016 = {'Eleitores4': 12414879.0}
Media_Votos_Recebidos_2016 = {'Media4': 7902734.0}

Eleitores_Aptos_2018 = {'Eleitores5': 12408340.0}
Media_Votos_Recebidos_2018 = {'Media5': 8887824.0}

Eleitores_Aptos_2020 = {'Eleitores6': 12455812}
Media_Votos_Recebidos_2020 = {'Media6': 7314819.0}

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