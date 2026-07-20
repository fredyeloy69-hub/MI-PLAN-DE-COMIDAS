import pandas as pd
import json

# 1. Cargar el archivo con el separador correcto (;)
df = pd.read_csv('tablas-peruanas-Alimentos excel.csv', encoding='latin-1', sep=';')

# 2. Limpiar nombres de columnas (quitar caracteres raros)
df.columns = [str(c).replace('ï»¿', '').strip() for c in df.columns]

# 3. Convertir a JSON
full_json = df.to_json(orient='records', force_ascii=False, indent=2)

# 4. Guardar archivo
with open('alimentos_completo.json', 'w', encoding='utf-8') as f:
    f.write(full_json)

print("Archivo JSON generado con éxito.")