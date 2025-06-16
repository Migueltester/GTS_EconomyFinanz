import requests
import json
import os

# Crear carpeta 'raw' si no existe
os.makedirs('../raw', exist_ok=True)

# URL de la API del Banco Mundial - PIB total (USD)
url = 'https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?format=json&per_page=10000'

# Hacer la solicitud a la API
print("Solicitando datos del Banco Mundial...")
response = requests.get(url)

# Verificar que la respuesta sea exitosa
if response.status_code == 200:
    data = response.json()

    # Guardar el JSON en un archivo local
    output_path = 'C:/Users/migue/Documents/Parcial_2_Gestion/raw/worldbank_gdp.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"✅ Datos guardados en: {output_path}")
else:
    print(f"❌ Error al obtener los datos. Código: {response.status_code}")
