import pandas as pd
import os

# Ruta al archivo JSON
input_path = r"c:/Users/richa/Python/Python4ano/Parcial2/GTS_EconomyFinanz/rawdata/pib_todos_paises.json"

# Leer el archivo JSON
df = pd.read_json(input_path)

# Filtrar solo las columnas deseadas 
df = df[[ 
    "date",
    "value",
    "unit",
    "indicator.id",
    "indicator.value",
    "country.id",
    "country.value"
]]

# Renombrar columnas
df = df.rename(columns={
    "date": "tiempo",
    "value": "valor",
    "unit": "unidad",
    "indicator.id": "codigo_indicador",
    "indicator.value": "nombre_indicador",
    "country.id": "codigo_region",
    "country.value": "nombre_region"
})

# Asignar "$" como unidad fija
df["unidad"] = "$"
df["fuente"] = "World Bank"

# Guardar como CSV
output_csv = r"c:/Users/richa/Python/Python4ano/Parcial2/GTS_EconomyFinanz/cleandata/pib_limpio_columnas_seleccionadas.csv"
os.makedirs(os.path.dirname(output_csv), exist_ok=True)
df.to_csv(output_csv, index=False)

print(f"CSV generado con exito en:\n{output_csv}")
