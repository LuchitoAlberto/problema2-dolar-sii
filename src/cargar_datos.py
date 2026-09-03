import numpy as np

# Ruta al archivo (ajusta si la estructura de carpetas es distinta)
ruta_archivo = 'data/dolar_observado_sii_2022_2025.csv'

# 1. Cargar solo la matriz de precios numéricos.
# skip_header=1 salta la fila de los años (2022, 2023, 2024, 2025)
# usecols=(1, 2, 3, 4) toma solo las columnas numéricas, saltando la columna 0 (los nombres de los meses)
# Nota: Si tu CSV usa punto y coma, cambia delimiter=',' por delimiter=';'
precios_dolar = np.genfromtxt(ruta_archivo, delimiter=',', skip_header=1, usecols=(1, 2, 3, 4))

# 2. (Opcional) Cargar los nombres de los meses y los años para los gráficos
meses = np.genfromtxt(ruta_archivo, delimiter=',', skip_header=1, usecols=(0), dtype=str)
anios = np.genfromtxt(ruta_archivo, delimiter=',', max_rows=1, dtype=str)[1:]

print("Matriz de precios (Filas = Meses, Columnas = Años):")
print(precios_dolar)

# Ejemplo de cómo recorrer los años para comprobar que se cargaron bien
print("\nPromedio anual (sin propagación de error):")
for i in range(precios_dolar.shape[1]):
    promedio_anual = np.mean(precios_dolar[:, i])
    print(f"Año {anios[i]}: {promedio_anual:.2f}")