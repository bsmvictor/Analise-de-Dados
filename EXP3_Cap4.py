import numpy as np

df = np.loadtxt('C:\\Users\\victo\\Downloads\\space.csv',delimiter=';',dtype=str,encoding='utf-8')

#1. Taxa de Sucesso da Missão:
success_indicator = df[1:, -1] == 'Success'
success_percentage = np.mean(success_indicator) * 100
print(f"Taxa de Sucesso da Missão: {success_percentage}")

#2. Custo Médio das Missões:
cost_data = df[1:, -2].astype(float)
cost_mask = cost_data > 0
average_cost = np.mean(cost_data[cost_mask]) if cost_mask.any() else 0
print(f"Custo médio das missões: {average_cost}")

#3. Número de Missões Espaciais dos EUA:
usa_missions = np.sum(np.char.find(df[1:, 2], 'USA') != -1)
print(f"O número de missões espaciais dos EUA: {usa_missions}")

#4. Missão Mais Cara da SpaceX:
spacex_rows = df[1:][df[1:, 1] == 'SpaceX']
spacex_costs = spacex_rows[:, -2].astype(float)
most_expensive_mission = spacex_rows[spacex_costs.argmax()]
print(f"A missão mais cara da SpaceX: {most_expensive_mission}")
