import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('world_happiness.csv', delimiter=',')

# QUESTÃO 1
maisFelizess = df.nlargest(5, 'Ladder score')
plt.bar(maisFelizess['Country name'], maisFelizess['Healthy life expectancy'])
plt.xlabel('País')
plt.ylabel('expectativa de vida saudável')
plt.title('Expectativa de vida saudável dos cinco países mais felizes do mundo')
plt.show()

# QUESTÃO 2
menosFelizes = df.nsmallest(20, 'Ladder score')
paises = menosFelizes['Regional indicator'].value_counts()
plt.pie(paises, labels=paises.index)
plt.title('20 países mais infelizes')
plt.show()

# QUESTÃO 3
lac = df[df['Regional indicator'] == 'Latin America and Caribbean']
top5lac = lac.nlargest(5, 'Ladder score')
plt.scatter(top5lac['Country name'], top5lac['Ladder score'],
            s=top5lac['Log GDP per capita']*300)
plt.xlabel('Países')
plt.ylabel('Felicidade')
plt.title('5 países mais felizes da América Latina e Caribe')
plt.show()

# QUESTÃO 4
avgllac = lac['Freedom to make life choices'].mean()
bl = df[df['Country name'] == 'Brazil']['Freedom to make life choices'].values[0]
plt.bar(['Brazil', 'Latin America & Caribbean Avg'], [bl, avgllac])
plt.ylabel('Liberdade de se fazer escolhas de vida')
plt.title(
    'Liberdade de se fazer escolhas de vida dos países da América Latina e Caribe')
plt.show()
