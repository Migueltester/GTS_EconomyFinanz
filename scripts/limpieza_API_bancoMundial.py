import pandas as pd
import os

# Ruta al archivo descargado
input_path = r"c:/Users/richa/Python/Python4ano/Parcial2/GTS_EconomyFinanz/rawdata/deuda_externa_worldbank.csv"

# Leer CSV original
df = pd.read_csv(input_path)

# Seleccionar y renombrar columnas
df = df[[
    "date",
    "value",
    "unit",
    "indicator.id",
    "indicator.value",
    "country.id",
    "country.value"
]].rename(columns={
    "date": "tiempo",
    "value": "valor",
    "unit": "unidad",
    "indicator.id": "codigo_indicador",
    "indicator.value": "nombre_indicador",
    "country.id": "codigo_region",
    "country.value": "nombre_region"
})

# Reemplazar unidad vacía por "USD"
df["unidad"] = "USD"
df["fuente"] = "World Bank"

# Guardar CSV limpio
output_path = r"c:/Users/richa/Python/Python4ano/Parcial2/GTS_EconomyFinanz/cleandata/deuda_externa_limpio.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print("Deuda externa limpiada y exportada a:\n", output_path)
