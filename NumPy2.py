import numpy as np

# numeros aleatorios
# np.random.seed(10)
# arr = np.random.randint(10, 20, 5) #5 numeros aleatorios entre 10 e 20
# print(arr)

# elemenos unicos
# np.random.seed(5)
# arr = np.random.randint(0, 10, 15)
# print(arr)
# print(np.unique(arr))
# print(set(arr))

# operação em matrizes
# np.random.seed(10)
# mtz = np.random.randint(1,11, 9).reshape(3,3)
# print('matriz:\n', mtz)
# print('-----------------------------')
# print('somas das linhas:',mtz.sum(axis = 1))
# print('somas da linha 1:',mtz.sum(axis = 1)[0])
# print('somas da linha 2:',mtz.sum(axis = 1)[1])
# print('somas da linha 3:',mtz.sum(axis = 1)[2])
# print('-----------------------------')
# print('somas das colunas:',mtz.sum(axis = 0))
# print('somas da coluna 1:',mtz.sum(axis = 0)[0])
# print('somas da coluna 2:',mtz.sum(axis = 0)[1])
# print('somas da coluna 3:',mtz.sum(axis = 0)[2])
# print('-----------------------------------')
# print('media da linha 1:',mtz.mean(axis = 1)[0])
# print('media da linha 2:',mtz.mean(axis = 1)[1])
# print('media da linha 3:',mtz.mean(axis = 1)[2])
# print('-----------------------------------')
# print('media da linha 1:',mtz.mean(axis = 0)[0])
# print('media da linha 2:',mtz.mean(axis = 0)[1])
# print('media da linha 3:',mtz.mean(axis = 0)[2])
# print('-----------------------------------')

# broadcasting
# print('matriz multiplicada por dois:\n', mtz*2)

# condicionais do NumPy
# cond = mtz%2 == 0
# print('Mascara de elementos pares por verdadeiros e falsos: \n',cond)
# print('-----------------------------------')
# arr = mtz[mtz%2 == 0]
# print('Elementos pares:',arr)
# print('-----------------------------------')
# cond = mtz>mtz.mean()
# print(cond)
# print('-----------------------------------')
# print('Resultados:',mtz[cond])

# Trabalhando com textos
arr = np.array(['Victor', 'Alves', 'Conrado', 'Dju']) # i e I sao diferentes, para resolver esta diferença, padronize os textos
print(np.char.find(arr, 'a'))
arr2 = arr[np.char.find(arr, 'a') >= 0]
print(arr2)
