import pandas as pd
import os

# Ruta al archivo original descargado
input_path = r"c:/Users/richa/Python/Python4ano/Parcial2/GTS_EconomyFinanz/rawdata/deuda_gobierno_2024.csv"

# Leer CSV original
df = pd.read_csv(input_path)

# Agregar columnas faltantes
df["unidad"] = "%"
df["codigo_indicador"] = "GOVT_DEBT_PCT_GDP"
df["codigo_region"] = None  # Dejar explícitamente vacío
df["fuente"] = "Wikipedia"

# Renombrar columnas para estandarización
df = df.rename(columns={
    "pais": "nombre_region",
    "valor": "valor",
    "indicador": "nombre_indicador",
    "tiempo": "tiempo"
})

# Reordenar columnas al formato objetivo
df = df[[
    "tiempo", "valor", "unidad",
    "codigo_indicador", "nombre_indicador",
    "codigo_region", "nombre_region",
    "fuente"
]]

# Guardar archivo limpio
output_path = r"c:/Users/richa/Python/Python4ano/Parcial2/GTS_EconomyFinanz/cleandata/deuda_gobierno_limpio.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print("Archivo limpio generado en:\n", output_path)
