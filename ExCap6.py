import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1
dfSpace = pd.read_csv('space.csv', delimiter=';')

usa = dfSpace[dfSpace['Location'].str.contains('USA')]['Company Name'].nunique()
china = dfSpace[dfSpace['Location'].str.contains('China')]['Company Name'].nunique()

labels = ['USA', 'China']
counts = [usa, china]

plt.bar(labels, counts, color=['cyan', 'red'])
plt.xlabel('País')
plt.ylabel('Num.Empresas')
plt.show()

#2
dfPaises = pd.read_csv('paises.csv', delimiter=';')

death = dfPaises[dfPaises['Region'].str.contains('NORTHERN AMERICA')]['Deathrate']
birth = dfPaises[dfPaises['Region'].str.contains('NORTHERN AMERICA')]['Birthrate']
#Plot 2 graficos separados
plt.subplot(1,2,1) 
plt.plot(death,'m-')
plt.subplot(1,2,2)
plt.plot(birth,'c--')
plt.show()