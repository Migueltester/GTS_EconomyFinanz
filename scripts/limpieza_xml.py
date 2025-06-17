import pandas as pd
import xml.etree.ElementTree as ET
import os

# Ruta del archivo XML
input_path = r"c:/Users/richa/Python/Python4ano/Parcial2/GTS_EconomyFinanz/rawdata/tasa_cambio.xml"

# Parsear el XML con raíz <Root><data><record>...</record></data></Root>
tree = ET.parse(input_path)
root = tree.getroot()

# Buscar registros bajo <data>
records = root.find("data").findall("record")

registros = []
for record in records:
    registro = {
        "tiempo": None,
        "valor": None,
        "unidad": "UMN",
        "codigo_indicador": None,
        "nombre_indicador": None,
        "codigo_region": None,
        "nombre_region": None,
        "fuente": "CEPAL"  # ← Se añade fuente fija
    }
    for field in record.findall("field"):
        name = field.attrib.get("name")
        key = field.attrib.get("key", None)
        value = field.text

        if name == "Country or Area":
            registro["nombre_region"] = value
            registro["codigo_region"] = key
        elif name == "Item":
            registro["nombre_indicador"] = value
            registro["codigo_indicador"] = key
        elif name == "Year":
            registro["tiempo"] = value
        elif name == "Value":
            registro["valor"] = value
    registros.append(registro)

# Crear DataFrame
df = pd.DataFrame(registros)

# Guardar CSV
output_path = r"c:/Users/richa/Python/Python4ano/Parcial2/GTS_EconomyFinanz/cleandata/tasa_cambio_estandarizado.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print(f"Archivo generado con {len(df)} registros y fuente 'CEPAL' en:\n{output_path}")
