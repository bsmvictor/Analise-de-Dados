import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# # plot simples
# x = np.array([1, 2, 3, 4])

# # broadcastig
# y = x*2
# y2 = x**2

# plt.xlabel('Eixo X')
# plt.ylabel('Eixo Y')

# #plt.plot(x, y, 'o--g', x, y2, 'b:o',linewidth=3, markersize=20)

# plt.subplot(1, 2, 1)
# plt.xlabel('Eixo X')
# plt.ylabel('Eixo Y')
# plt.title('Linear')
# plt.plot(x, y, 'x--r')

# plt.subplot(1, 2, 2)

# plt.title('Exponencial')
# plt.plot(x, y2, 'o:g')

# plt.show()

df = pd.read_csv('paises.csv', delimiter=';')

df2 = df.nlargest(6, 'Area (sq. mi.)')  # n maiores onde n = 6 baseado na area

plt.scatter(df2['Country'], df2['Area (sq. mi.)'],
            s=df2['GDP ($ per capita)']/50)

plt.show()
