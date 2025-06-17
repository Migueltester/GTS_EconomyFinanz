import json
import pandas as pd
import os

# Crear carpeta clean si no existe
os.makedirs('../data/clean', exist_ok=True)

# Cargar archivo JSON crudo
with open('../raw/worldbank_gdp.json', 'r') as f:
    data = json.load(f)

# Extraer solo la parte útil: data[1] es la lista de observaciones
records = data[1]

# Crear DataFrame con pandas
df = pd.DataFrame(records)

# Filtrar solo Latin America & Caribbean
df = df[df['country'].apply(lambda x: x['value'] == 'Latin America & Caribbean')]

# Limpiar columnas necesarias
df_clean = df[['date', 'value']].copy()
df_clean.rename(columns={'date': 'anio', 'value': 'pib_usd'}, inplace=True)

# Convertir tipos
df_clean['anio'] = df_clean['anio'].astype(int)
df_clean['pib_usd'] = pd.to_numeric(df_clean['pib_usd'], errors='coerce')

# Eliminar filas con PIB nulo
df_clean.dropna(inplace=True)

# Ordenar por año
df_clean.sort_values(by='anio', inplace=True)

# Guardar CSV limpio
output_path = 'C:/Users/migue/Documents/Parcial_2_Gestion/data/clean/worldbank_gdp_latam.csv'
df_clean.to_csv(output_path, index=False)

# Mostrar resumen
print("✅ Limpieza completa. Archivo guardado en:", output_path)
print(df_clean.head())
