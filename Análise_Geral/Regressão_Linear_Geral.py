import numpy as np
import matplotlib.pyplot as plt

X = np.array([11259334, 11589763, 11893309, 12141145, 12414879, 12408340, 12455812 ]) #Var independente Eleitores
y = np.array([9896126, 9395724, 8089848, 7592173, 7902734, 8887824, 7314819]) #Var dependente Média Votos

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