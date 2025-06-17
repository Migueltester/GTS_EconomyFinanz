import requests
import os

# URL de descarga del XML
url = "https://api.worldbank.org/v2/es/indicator/PA.NUS.FCRF?downloadformat=xml"

# Carpeta de destino
output_dir = r"c:/Users/richa/Python/Python4ano/Parcial2/GTS_EconomyFinanz/rawdata/"
os.makedirs(output_dir, exist_ok=True)

# Nombre del archivo de salida
output_file = os.path.join(output_dir, "tasa_cambio.xml")

# Descargar archivo
response = requests.get(url)

if response.status_code == 200:
    with open(output_file, "wb") as f:
        f.write(response.content)
    print(f"Archivo XML guardado en: {output_file}")
else:
    print(f"Error al descargar. Código de estado: {response.status_code}")
