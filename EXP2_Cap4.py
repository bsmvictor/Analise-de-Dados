import numpy as np

# 1)
np.random.seed(5)
arr1 = np.random.rand(10)
arr1 = arr1*100
arr1 = np.array(arr1, dtype=np.int64)
print("Parte inteira: ", arr1, "\n")

# 2)
np.random.seed(10)
mtz = np.random.randint(1, 50, 16).reshape(4, 4)
print("Matriz: ", mtz, "\n")

# 3)
lin_avg = np.mean(mtz, axis=1)
col_avg = np.mean(mtz, axis=0)
print("Media das linhas: ", lin_avg)
print("Media das colunas: ", col_avg)
print("Maior valor das medias nas linhas: ", np.max(lin_avg))
print("Maior valor das medias nas colunas: ", np.max(col_avg), "\n")

# 4)
arr3 = np.unique(mtz, return_counts=True)
arr3 = np.array(arr3)
print("Matriz: ", arr3, "\n")

unique_values, counts = np.unique(mtz, return_counts=True)
print("Quantidade de aparição de cada número: ", "\n", np.column_stack((unique_values, counts)), "\n")

indices = np.where(counts == 2)
print("Números que aparecem apenas duas vezes: ", unique_values[indices])