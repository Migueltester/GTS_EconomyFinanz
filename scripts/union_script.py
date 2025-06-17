import pandas as pd

# Cargar ambos archivos
df_cepal = pd.read_csv('C:/Users/migue/Documents/Parcial_2_Gestion/data/clean/cepal_pib.csv')
df_wb = pd.read_csv('C:/Users/migue/Documents/Parcial_2_Gestion/data/clean/worldbank_gdp_latam.csv')

# Renombrar columnas de CEPAL para que coincidan
df_cepal = df_cepal.rename(columns={
    'Años__ESTANDAR': 'anio',
    'value': 'pib_usd'
})

# Convertir tipos y valores
df_cepal['anio'] = df_cepal['anio'].astype(int)
df_cepal['pib_usd'] = pd.to_numeric(df_cepal['pib_usd'], errors='coerce')
df_cepal['fuente'] = 'CEPAL'

# Agregar columna de fuente a Banco Mundial
df_wb['fuente'] = 'Banco Mundial'

# Unificar ambos
df_unificado = pd.concat([df_cepal[['anio', 'pib_usd', 'fuente']],
                          df_wb[['anio', 'pib_usd', 'fuente']]], ignore_index=True)

# Guardar archivo combinado
df_unificado.to_csv('C:/Users/migue/Documents/Parcial_2_Gestion/data/clean/pib_unificado.csv', index=False)

# Mostrar preview
print("✅ Datos combinados correctamente. Vista previa:")
print(df_unificado.sort_values('anio').head())
