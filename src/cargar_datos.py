import os
import numpy as np

def cargar_datos(ruta_csv=None):
    """
    Carga el archivo CSV oficial del dólar observado usando numpy.genfromtxt.
    Retorna:
        anios (np.ndarray): Vector con los años de cada registro (48 elementos).
        meses (np.ndarray): Vector con los nombres de los meses (48 elementos).
        precios (np.ndarray): Vector cronológico con los 48 precios (float64).
        etiquetas (list): Lista con etiquetas cortas tipo ['Ene-22', ..., 'Dic-25'].
        matriz_precios (np.ndarray): Matriz de 12 meses x 4 años (2022 a 2025).
    """
    if ruta_csv is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_csv = os.path.join(base_dir, "data", "dolar_observado_sii_2022_2025.csv")

    # Leer años (columna 0), meses (columna 1) y precios (columna 3)
    anios = np.genfromtxt(ruta_csv, delimiter=',', skip_header=1, usecols=0, dtype=int, encoding='utf-8')
    meses = np.genfromtxt(ruta_csv, delimiter=',', skip_header=1, usecols=1, dtype=str, encoding='utf-8')
    precios = np.genfromtxt(ruta_csv, delimiter=',', skip_header=1, usecols=3, dtype=float, encoding='utf-8')

    # Crear etiquetas cortas para los gráficos (ej: "Ene-22")
    etiquetas = [f"{m[:3]}-{str(a)[2:]}" for m, a in zip(meses, anios)]

    # Organizar en matriz de 12 meses x 4 años
    matriz_precios = precios.reshape((4, 12)).T

    return anios, meses, precios, etiquetas, matriz_precios

if __name__ == "__main__":
    anios, meses, precios, etiquetas, matriz = cargar_datos()
    print("✓ Datos cargados exitosamente con NumPy.")
    print(f"Total de registros: {len(precios)} meses (de {etiquetas[0]} a {etiquetas[-1]})")
    print(f"Precio inicial ({meses[0]} {anios[0]}): ${precios[0]:.2f}")
    print(f"Precio final ({meses[-1]} {anios[-1]}): ${precios[-1]:.2f}")
    print(f"Forma de la matriz mensual: {matriz.shape} (12 meses x 4 años)")