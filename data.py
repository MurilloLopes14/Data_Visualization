from pandas import read_csv, to_datetime
import matplotlib.pyplot as plt

#* Gráfico de barras
df = read_csv("queimadas_1998_2016.csv")

df['year'] = df['year'].astype('str')

plt.figure(figsize=(7,4))
plt.bar(df['year'], df["number"], color='skyblue')

plt.title("Numero de queimadas no Brasil de 1998 à 2016")
plt.xlabel("Ano")
plt.ylabel("Numero de casos")

plt.xticks(rotation=45)

plt.tight_layout()

#* Gráfico de pizza 
dt = read_csv('queimadas_por_regiao.csv')

if 'region' not in dt.columns or 'number' not in dt.columns:
    raise ValueError("Este arquivo .CSV precisa conter as chaves 'region' e 'numbers'")

if len(dt['region']) != len(dt['number']):
    raise ValueError("A quantidade de valores de ambas as colunas precisam ser iguais")

plt.figure(figsize=(8,8))
plt.pie(dt['number'],labels=dt['region'], autopct='%1.1f%%',startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
plt.title("Número de queimadas nas regiões do Brasil de 1998 à 2016")

#*  Gráfico temporal

data = read_csv('queimadas_sao_paulo.csv')

data['year'] = to_datetime(data['year'], format='%Y')

fig, ax = plt.subplots(figsize=(12,8))

for state, state_data in data.groupby('state'):
    ax.plot(state_data['year'], state_data['number'], label=state)

ax.set_xlabel('Data')
ax.set_ylabel('Número de Casos')
ax.set_title('Queimadas no estado de São Paulo de 1998 à 2016')
ax.legend()

plt.show()