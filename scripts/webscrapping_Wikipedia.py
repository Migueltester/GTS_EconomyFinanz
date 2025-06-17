import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

# URL de Wikipedia
url = "https://en.wikipedia.org/wiki/List_of_countries_by_external_debt"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# Extraer la tabla
tabla = soup.find("table", {"class": "wikitable"})
df = pd.read_html(str(tabla))[0]

# Buscar la columna que contiene la fecha (ej. 'Date' o similar)
fecha_col = next((col for col in df.columns if "Date" in col), None)

# Si la columna existe, extraemos el año
if fecha_col:
    df["Year"] = df[fecha_col].astype(str).str.extract(r'(\d{4})')
else:
    print("⚠️ No se encontró una columna con fechas. No se creó la columna 'Year'.")

# Guardar CSV
output_path = r"c:/Users/richa/Python/Python4ano/Parcial2/GTS_EconomyFinanz/rawdata/deuda_externa_wikipedia.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print(f"✅ CSV guardado correctamente en:\n{output_path}")
