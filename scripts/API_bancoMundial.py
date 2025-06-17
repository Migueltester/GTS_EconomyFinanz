import requests
import pandas as pd
import os

# URL de la API para deuda externa total
url = "https://api.worldbank.org/v2/country/all/indicator/DT.DOD.DECT.CD?format=json&per_page=20000"

response = requests.get(url)
data = response.json()

# La segunda entrada contiene la lista de registros
records = data[1]

# Convertir directamente en DataFrame sin limpieza adicional
df = pd.json_normalize(records)

# Crear ruta de salida si no existe
output_path = r"c:/Users/richa/Python/Python4ano/Parcial2/GTS_EconomyFinanz/rawdata/deuda_externa_worldbank.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Guardar DataFrame en un archivo CSV
df.to_csv(output_path, index=False)

print("Archivo CSV completo guardado en:\n", output_path)
