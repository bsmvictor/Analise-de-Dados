# Importando biblioteca
import numpy as np

# criando numpy array (GUARDA DADOS DE APENAS DO MESMO TIPO)
arr = np.array([1, 2, 3, 4])

# Print np.array
print(arr)
print('-------------------------------------------\n')

# # Permite visualizar o tipo dos dados
print(type(arr))
print('-------------------------------------------\n')

# array de duas dimensões
mtz = np.array([[1, 2], [3, 4]])
print(mtz)
print('-------------------------------------------\n')

# Estruturando numpy arrays automaticamente
mtz = np.ones(9)
print(mtz)
print('-------------------------------------------\n')

# Remodelando dimensão do array
mtz = np.ones(9).reshape(3,3)
print(mtz)
print('-------------------------------------------\n')

# Criando elemento detro de uma faixa de valores desejada
mtz = np.arange(10, 20, 2) # inicia em 10, ate 20 (exclusivo), de 2 em 2
print(mtz)
print('-------------------------------------------\n')

# Operações Elemento a Elemento
arr1 = np.arange(10, 20, 1)
arr2 = np.arange(30, 40, 1)

print(arr1)
print(arr2)
print()

# Somando os dois arrays
print(arr1 + arr2)
print()

# Concatenando os arrays
print(np.concatenate([arr1, arr2]))
print()

# Propriedades de um numpy array
print('Tamanho: ', arr1.size)
print('Dimensões: ', arr1.ndim)
print('Formato: ', arr1.shape)


