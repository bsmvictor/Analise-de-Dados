import numpy as np

path = "C:\\Users\\victo\\Downloads\\brands.csv"

data = np.loadtxt(path, delimiter=';', dtype=str, encoding='utf-8')

# 1
val2021 = data[4, 10].astype(float)  # fatiamento microsoft valorização 2021
val2022 = data[4, 9].astype(float)  # fatiamento microsoft valorização 2022
# print('Valorizacao de 2021 para 2022: ',val2022-val2021)

# 2
brands = data[1:, 0]  # fatiamento marcas
# separando marcas que começam com a letra A
aBrands = brands[np.char.find(brands, 'A') == 0]
# print('Empresas que começam com A: ',aBrands)

# 3
slicedData = data[1:, 3]  # fatiamento dos dados
# encontrndo United States nos dados
countryData = np.char.find(slicedData, 'United States') != -1
# contando quantos United States foram encontrados
countryData = np.count_nonzero(countryData)
# print('media:',countryData/100, '%') #dividindo pelo total para tirar a media

# 4
slicedData = data[1:, 0:3]  # fatiando as colunas solicitadas
foundedData = data[1:, 2].astype(int)  # fatiando ano de fundação
cond = foundedData > 2000  # separand apenas os maiores de 2000
foundedData = foundedData[cond]  # aplicando condição no array
# nao terminado

# 5
slicedData = data[1:, 2].astype(int)  # fatinando ano de fundação
# nao teminado
