import numpy as np
import os

def cargar_datos():
    carpeta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_csv = os.path.join(carpeta_base, 'data', 'dolar_observado_sii_2022_2025.csv')
    
    datos = np.genfromtxt(
        ruta_csv,
        delimiter=',',
        skip_header=1,
        dtype=[('anio', 'i4'), ('mes', 'U20'), ('mes_num', 'i4'), ('precio', 'f8')]
    )
    return datos