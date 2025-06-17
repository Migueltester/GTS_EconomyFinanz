import pandas as pd
import os

# Ruta del archivo Excel original
input_path = r"c:/Users/richa/Python/Python4ano/Parcial2/GTS_EconomyFinanz/rawdata/inflacion.xlsx"

# Leer archivo Excel
df = pd.read_excel(input_path)

# Renombrar columnas al formato estandarizado
df = df.rename(columns={
    "indicator": "nombre_indicador",
    "País__ESTANDAR": "nombre_region",
    "Años__ESTANDAR": "tiempo",
    "Tipo de informe": "tipo_informe",
    "value": "valor",
    "unit": "unidad"
})

# Asignar código genérico si no hay columna de código
df["codigo_indicador"] = "INF"  # Indicador ejemplo
df["codigo_region"] = None  # Si no se cuenta con código de país
df["fuente"] = "World Bank"

# Guardar como CSV limpio
output_path = r"c:/Users/richa/Python/Python4ano/Parcial2/GTS_EconomyFinanz/cleandata/inflacion_anual_limpio.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print("Archivo limpio exportado a:\n", output_path)
