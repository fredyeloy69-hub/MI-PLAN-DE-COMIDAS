import pandas as pd
import json

# ---------- Función auxiliar: limpia números con coma decimal (formato en español) ----------
def limpiar_numero(valor):
    if pd.isna(valor):
        return None
    s = str(valor).strip()
    if s in ('', '•', '-'):
        return None
    s = s.replace(',', '.')
    try:
        f = float(s)
        return int(f) if f.is_integer() else f
    except ValueError:
        return None


def procesar_csv(ruta_csv, columnas_numericas, salida_json):
    # Cargar el archivo con el separador de punto y coma
    df = pd.read_csv(ruta_csv, encoding='utf-8-sig', sep=';')

    # Limpiar nombres de columnas (por si viene con BOM o espacios)
    df.columns = [str(c).replace('ï»¿', '').strip() for c in df.columns]

    # Limpiar las columnas numéricas (comas -> puntos, "•"/"" -> None)
    for col in columnas_numericas:
        if col in df.columns:
            df[col] = df[col].apply(limpiar_numero)

    # Convertir a lista de diccionarios (evita el .to_json de pandas para controlar None correctamente)
    registros = df.where(pd.notnull(df), None).to_dict(orient='records')

    with open(salida_json, 'w', encoding='utf-8') as f:
        json.dump(registros, f, ensure_ascii=False, indent=2)

    print(f"'{salida_json}' generado con éxito! ({len(registros)} alimentos)")


# ---------- Archivo 1: tabla internacional ----------
cols_internacional = [
    'Calorías (Kcal.)', 'Carbohidratos (g.)', 'Proteínas (g.)',
    'Grasas (g.)', 'Fibra (g.)', 'Peso unidad referencia (g)'
]
procesar_csv(
    'tabla-de-alimentos_ACTUALIZADO.csv',
    cols_internacional,
    'tabla-de-alimentos.json'
)

# ---------- Archivo 2: tablas peruanas ----------
cols_peruana = [
    'Energía (kcal)', 'Energía (kJ)', 'Agua (g)', 'Proteínas (g)',
    'Grasa total (g)', 'Carbohidratos totales (g)',
    'Carbohidratos disponibles (g)', 'Fibra dietaria (g)',
    'Peso unidad referencia (g)'
]
procesar_csv(
    'tablas-peruanas-Alimentos_ACTUALIZADO.csv',
    cols_peruana,
    'tablas-peruanas-alimentos.json'
)

print("¡Listo! Ambos archivos JSON actualizados correctamente.")
