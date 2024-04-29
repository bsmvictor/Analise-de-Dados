import numpy as np

path = 'C:\\Users\\victo\\Downloads\\paises.csv'

data = np.loadtxt(path, delimiter = ';', dtype = str, encoding = 'utf-8')

# #1
slicedData = data[:,0:4] # todas as linhas e colunas da 0 ate a 3 (4 é exclusive)
#print(slicedData)

#2
slicedData = data[1:, 1] # todas as linhas a partir da 1, se n pega o titulo, da coluna 1
numOfRegions = np.unique(slicedData) #extraindo elementos nao repetidos
#print('Numero de regiões do planeta: ', np.count_nonzero(numOfRegions),
#      '\nDiferentes regiões do planeta: ', numOfRegions)

#3
slicedData = data[1:, 9].astype(float) # todas as linhas a partir da 1 da coluna 9, converto os valores para float
#print('\nTaxa media de alfabetização:',np.mean(slicedData),'%')

#4
slicedData = data[1:, 1]
na = np.char.find(slicedData,'NORTHERN AMERICA') != -1
print(na)
print('\nNumero de paises que fazem parte da America do Norte:',np.count_nonzero(na))

#5
cond = np.char.find(data[:, 1], 'LATIN AMER. & CARIB  ') != -1
latin = data[cond]
renda = np.array(latin[:, 8]).astype(float)
arr7 = latin[np.argmax(renda)]
print(arr7[0])

import matplotlib.pyplot as plt

# Supondo que latinData já esteja definido como explicado antes
countries = latin[:, 0]  # Nomes dos países estão na primeira coluna
gdp_values = latin[:, 8].astype(float)  # Renda (assumindo que esteja na nona coluna e ainda não convertida)

# Criar o gráfico de barras
plt.figure(figsize=(10, 8))  # Tamanho do gráfico
plt.bar(countries, gdp_values, color='blue')  # Cria barras azuis

# Adicionar títulos e rótulos
plt.title('Renda nos Países da América Latina e Caribe')
plt.xlabel('País')
plt.ylabel('Renda (USD)')

# Melhorar a disposição das etiquetas do eixo x para melhor legibilidade
plt.xticks(rotation=45, ha='right')

# Opcional: adicionar grade para melhor visualização
plt.grid(True)

# Mostrar o gráfico
plt.show()