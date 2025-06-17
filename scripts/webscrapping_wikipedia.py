import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL
url = "https://en.wikipedia.org/wiki/List_of_countries_by_government_debt"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# Extraer tabla
tablas = soup.find_all("table", {"class": "wikitable"})
tabla = tablas[0]
df = pd.read_html(str(tabla))[0]

# Buscar columna con 'gross debt' y '2024'
col_2024 = next(c for c in df.columns if "gross debt" in c and "2024" in c)

# Filtrar columnas
df = df[["Country and region", col_2024]]
df = df.rename(columns={
    "Country and region": "pais",
    col_2024: "valor"
})

# Agregar campos estándar
df["indicador"] = "General government debt as a % of GDP"
df["tiempo"] = 2024

# Limpiar datos: eliminar valores no numéricos
df = df[pd.to_numeric(df["valor"], errors="coerce").notna()]
df["valor"] = df["valor"].astype(float)

# Guardar CSV
output_path = r"c:/Users/richa/Python/Python4ano/Parcial2/GTS_EconomyFinanz/rawdata/deuda_gobierno_2024.csv"
df.to_csv(output_path, index=False, encoding="utf-8-sig")

print("Archivo guardado en:", output_path)
