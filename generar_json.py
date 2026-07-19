import pandas as pd
import json

# Cargar el archivo con el separador de punto y coma
df = pd.read_csv('tablas-peruanas-Alimentos excel.csv', encoding='latin-1', sep=';')

# Limpiar nombres de columnas
df.columns = [str(c).replace('ï»¿', '').strip() for c in df.columns]

# Convertir a formato JSON
json_data = df.to_json(orient='records', force_ascii=False, indent=2)

# Guardar
with open('alimentos_completo.json', 'w', encoding='utf-8') as f:
    f.write(json_data)

print("¡Archivo 'alimentos_completo.json' generado con éxito!")