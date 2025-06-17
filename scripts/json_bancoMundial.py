import requests
import pandas as pd
import os

# URL para obtener el PIB de todos los países desde la API del Banco Mundial
url = (
    "https://api.worldbank.org/v2/"
    "country/all/indicator/NY.GDP.MKTP.CD?format=json&per_page=20000"
)

# Realizar la petición
resp = requests.get(url)
data = resp.json()

# Extraer metadatos y registros
meta, records = data[0], data[1]

# Convertir a DataFrame plano
df = pd.json_normalize(records)

# Ruta de salida (JSON estándar)
output_path = 'C:/Users/richa/Python/Python4ano/Parcial2/GTS_EconomyFinanz/rawdata/pib_todos_paises.json'

# Asegurarse de que el directorio existe
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Guardar como JSON estándar (array de objetos)
df.to_json(output_path, orient='records', indent=2, date_format='iso')

print("Archivo guardado exitosamente en formato JSON estándar:")
print(df.head())
