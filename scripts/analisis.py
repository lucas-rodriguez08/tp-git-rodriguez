import pandas as pd
import matplotlib.pyplot as plt

# Leer datos
df = pd.read_csv('datos/annual.csv')

# Calcular métricas PROY-2
promedio = df['Mean'].mean()
maxima = df['Mean'].max()
minima = df['Mean'].min()
año_max = df.loc[df['Mean'].idxmax(), 'Year']
año_min = df.loc[df['Mean'].idxmin(), 'Year']

# Gráfico
plt.figure(figsize=(10,5))
df.plot(x='Year', y='Mean', title='Temperatura Global Anual', legend=False, color='red')
plt.ylabel('Anomalía Temperatura °C')
plt.grid(True)
plt.savefig('resultados/grafico_temperatura.png')
plt.close()

# ESTOS 3 PRINT SON LOS QUE TE FALTABAN
print(f"PROY-2: Promedio: {promedio:.2f}°C")
print(f"PROY-2: Máxima: {maxima:.2f}°C en el año {int(año_max)}")
print(f"PROY-2: Mínima: {minima:.2f}°C en el año {int(año_min)}")
