import pandas as pd
import os

# Crear carpeta de salida si no existe
os.makedirs('C:/Users/migue/Documents/Parcial_2_Gestion/data/clean', exist_ok=True)

# Ruta al archivo original
input_path = 'C:/Users/migue/Documents/Parcial_2_Gestion/raw/cepal_pib.xlsx'

try:
    df = pd.read_excel(input_path, engine='openpyxl')
except Exception as e:
    print(f"❌ Error al leer el Excel: {e}")
    exit()

# Mostrar las primeras filas para validar lectura
print("✅ Primeras filas del archivo original:")
print(df.head())

# Seleccionar solo las columnas necesarias y renombrarlas
df_limpio = df[['País__ESTANDAR', 'Años__ESTANDAR', 'value']].copy()
df_limpio.columns = ['pais', 'anio', 'pib_millones_usd']

# Eliminar filas con datos faltantes
df_limpio.dropna(inplace=True)

# Convertir tipos
df_limpio['anio'] = df_limpio['anio'].astype(int)
df_limpio['pib_millones_usd'] = pd.to_numeric(df_limpio['pib_millones_usd'], errors='coerce')

# Guardar archivo limpio
output_path = 'C:/Users/migue/Documents/Parcial_2_Gestion/data/clean/cepal_pib.csv'
df_limpio.to_csv(output_path, index=False, encoding='utf-8')

print(f"✅ Archivo limpio guardado en: {output_path}")
print(df_limpio.head())
