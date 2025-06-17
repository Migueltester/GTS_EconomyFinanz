import pandas as pd
import os

# Ruta base
base_path = r"c:/Users/richa/Python/Python4ano/Parcial2/GTS_EconomyFinanz/cleandata"

# Archivos a unificar
archivos = [
    "deuda_externa_limpio.csv",
    "inflacion_anual_limpio.csv",
    "pib_limpio_columnas_seleccionadas.csv",
    "tasa_cambio_estandarizado.csv",
    "deuda_gobierno_limpio.csv",
]

# Columnas esperadas
columnas_objetivo = [
    "tiempo", "valor", "unidad",
    "codigo_indicador", "nombre_indicador",
    "codigo_region", "nombre_region",
    "fuente"
]

# Diccionario de traducciones
mapa_nombre_indicador = {
    "Tasa de cambio oficial (UMN por US$, promedio para un período)": "Tasa de cambio oficial",
    "GDP (current US$)": "Producto Interno Bruto",
    "External debt stocks, total (DOD, current US$)": "Deuda Externa",
    "Inflación anual, precios al consumidor (%) FP_CPI_TOTL_ZG": "Inflación anual",
    "General government debt as a % of GDP": "Deuda del gobierno general como % del PIB",
}

dataframes = []
mapa_codigo_region = {}

# Paso 1: construir mapa de códigos desde los archivos que sí los tienen
for archivo in archivos:
    df_temp = pd.read_csv(os.path.join(base_path, archivo))
    if "codigo_region" in df_temp.columns and "nombre_region" in df_temp.columns:
        pares = df_temp.dropna(subset=["codigo_region", "nombre_region"])[["nombre_region", "codigo_region"]].drop_duplicates()
        for _, row in pares.iterrows():
            mapa_codigo_region[row["nombre_region"]] = row["codigo_region"]

# Paso 2: procesar y transformar los archivos
for archivo in archivos:
    df = pd.read_csv(os.path.join(base_path, archivo))

    # Convertir tipos
    df["tiempo"] = pd.to_numeric(df["tiempo"], errors="coerce")
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

    # Asegurar columnas faltantes
    for col in columnas_objetivo:
        if col not in df.columns:
            df[col] = None

    # Mapear códigos de región
    df["codigo_region"] = df.apply(
        lambda row: mapa_codigo_region.get(row["nombre_region"], row["codigo_region"]),
        axis=1
    )

    # Normalizar nombre_indicador
    df["nombre_indicador"] = df["nombre_indicador"].replace(mapa_nombre_indicador)

    # Eliminar registros incompletos
    df = df.dropna(subset=["tiempo", "valor", "nombre_region"])

    # Reordenar columnas
    df = df[columnas_objetivo]

    dataframes.append(df)

# Unir todos los DataFrames
df_unificado = pd.concat(dataframes, ignore_index=True)

# Guardar archivo final
output_path = os.path.join(base_path, "hechos_economicos_completo.csv")
df_unificado.to_csv(output_path, index=False)

print("Dataset unificado guardado en:\n", output_path)
