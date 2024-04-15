import numpy as np

path = 'C:\\Users\\victo\\Downloads\\paises.csv'

df = np.loadtxt(path, delimiter=';', dtype=str, encoding='utf-8')

# 1
arr = df[:, 0:4]
print(arr)

# 2
arr1 = df[1:, 1]
# print(arr1)
arr2 = np.unique(arr1)
print(np.count_nonzero(arr2))

# 3
arr3 = df[1:, 9].astype(float)
print(np.mean(arr3))

# 4
arr4 = np.char.find(arr1, "NORTHERN AMERICA") != -1
print(np.count_nonzero(arr4))

# 5
cond = np.char.find(df[:, 1], 'LATIN AMER. & CARIB') != -1
latin = df[cond]
renda = np.array(latin[:, 8]).astype(float)
arr7 = latin[np.argmax(renda)]
print(arr7[0])
