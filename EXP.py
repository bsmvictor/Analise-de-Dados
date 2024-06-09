import pandas as pd

df = pd.read_csv('paises.csv', delimiter=';')

#1.a
countries = df[df['Region'].str.strip() == 'OCEANIA']['Country']
print(countries,'\n')

#1.b
print(len(countries),'\n')
    
#2
mean = df['Literacy (%)'].mean()
print(mean.round(2),'\n')
    
#3
bigP = df['Population'].max()
dfBP = df[df['Population'] == bigP]
print(dfBP[['Country', 'Region']].iloc[0],'\n')
    
#4
dfWC = df[df['Coastline (coast/area ratio)'] == 0]
dfWC.to_csv(path_or_buf='noCoastline.csv', index=False, sep=';')
print('Arquivo criado')