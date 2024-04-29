import numpy as np
import pandas as pd

# Series (1D)
dic = {'a': 10,
       'b': 20,
       'c': 30}

# criando a sereies
s1 = pd.Series(dic)

s2 = pd.Series(data=[20, 30, 40], index=['a', 'b', 'd'])

# print (s1 + s2) #faz a operação elemento a elemento, desde que exista o mesmo elemento nas dias series

# print(s1.add(s2, fill_value=0)) #tratando elementos nao exstentes como zero

# print(s1['b']) #acessando um indicie especifico de uma serie

# print(s1[['b','c']]) # acessando multiplos indicies de uma serie

# condicionais
# print(s1[s1 > s1.mean()]) #quais elementos de s1 sao maiores que a media dos elementos de s1

# DataFrame (2D+)
df = pd.DataFrame(
    index=['A', 'B', 'C', 'D'],
    columns=['X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [4, 3])
)

# print(df)

# slicing de dados utilizando loc
# print(df.loc[['B','C'], ['X','Y','Z']]) # separando por linhas e colunas, se utilizar : ele seleciona tudo da mesma forma do iloc

# slicing de dados utilizando iloc
# print(df.iloc[1:3,:])

# ledo um csv com pandas
dfPaises = pd.read_csv('paises.csv', delimiter=';')
# print(dfPaises)

# exemplos de leitura do dataset
print(dfPaises.columns)  # buscando todas as colunas
print('****************')

print(dfPaises['Country'])  # buscando apenas coluna coutry
print('****************')

print(dfPaises.head(5))  # buscando 5 primeiros registros de um df
print('****************')

print(dfPaises.tail(2))  # buscando 2 ultimos registros de um df
