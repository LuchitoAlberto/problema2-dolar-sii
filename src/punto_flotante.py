import os
import sys
import numpy as np
import matplotlib.pyplot as plt

from cargar_datos import cargar_datos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def resolver_b1():
    valor_real = 1000.76
    valor_aprox3 = 1000.0 #valor con 3 cifras significativas 1000.76 * 10^0 = 1.00076 * 10^3 = 1.00 * 10^3 = 1000.0
    error_absoluto = abs(valor_real - valor_aprox3)
    error_relativo = (error_absoluto / valor_real) * 100
    print(f"Precio original: {valor_real}")
    print(f"Precio aproximado: {valor_aprox3}")
    print(f"Error absoluto: {error_absoluto}")
    print(f"Error relativo porcentual: {error_relativo}%")

def resolver_b4():
    precio_1 = 874.67
    precio_2 = 875.66
    valor_exacto = precio_1 - precio_2
    p1_float32 = np.float32(precio_1) #valor con 32 bits
    p2_float32 = np.float32(precio_2) #valor con 32 bits
    resta1 = p1_float32 - p2_float32
    error1 = abs(resta1 - valor_exacto)
    p1_float64 = np.float64(precio_1) #valor con 64 bits
    p2_float64 = np.float64(precio_2) #valor con 64 bits
    resta2 = p1_float64 - p2_float64
    error2 = abs(resta2 - valor_exacto)
    print(f"Precio 1: {precio_1}")
    print(f"Precio 2: {precio_2}")
    print(f"Valor exacto: {valor_exacto}")
    print(f"Resultado resta float32: {resta1}")
    print(f"Error float32: {error1}")
    print(f"Resultado resta float64: {resta2}")
    print(f"Error float64: {error2}")
    
def resolver_b2(datos):
    monto_inicial = 1_000_000.00
    precios = datos['precio'] #esto lo puse asi pero no se como sacar los datos de cargar_datos xDDD
    monto_float32 = np.float32(monto_inicial) #monto inicial en float32
    precio_float32 = precios.astype(np.float32) #precio en float32
    dolares_comprados_float32 = (monto_float32 / precio_float32) #comprar dolares
    precios_recu_float32 = (dolares_comprados_float32 * precio_float32) #volver a pesos
    derivado_float32 = precios_recu_float32 - monto_float32 #derivado de la operacion
    dolares_comprados_float64 = (monto_inicial / precios) #comprar dolares en float64
    precios_recu_float64 = (dolares_comprados_float64 * precios) #volver a pesos en float64
    derivado_float64 = precios_recu_float64 - monto_inicial #derivado de la operacion en float64
    print(f"Monto inicial: {monto_inicial}")
    return derivado_float32, derivado_float64

def graficos(datos, derivado_float32, derivado_float64): #aqui pedi ayuda a mi mejor amiga porq no me acuerdo como hacer los graficos :p
    carpeta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    carpeta_graficos = os.path.join(carpeta_raiz, 'graficos')
    os.makedirs(carpeta_graficos, exist_ok=True)
    
    # Obtener etiquetas de meses según cómo vengan los datos
    if isinstance(datos, tuple):
        anios = datos[0]
        meses = datos[1]
        etiquetas = [f"{str(m)[:3]}-{str(a)[2:]}" for a, m in zip(anios, meses)]
        total = len(datos[3])
    else:
        etiquetas = [f"{d['mes'][:3]}-{str(d['anio'])[2:]}" for d in datos]
        total = len(datos)
        
    posiciones = np.arange(total)
    
    plt.figure(figsize=(13, 5))
    
    # Curvas con nombres claros y comprensibles
    plt.plot(posiciones, derivado_float32, marker='o', markersize=4, color='crimson', 
             label='Precisión baja (32 bits): Se gana o pierde dinero por redondeo')
    plt.plot(posiciones, derivado_float64, linestyle='--', color='royalblue', 
             label='Precisión estándar (64 bits): Recupera el millón exacto')
    
    # Línea del cero: el resultado ideal donde no se pierde ni un peso
    plt.axhline(0, color='black', linewidth=1, linestyle=':', label='Meta ideal: Exactamente $1.000.000')
    
    # Etiquetas en el eje X cada 3 meses para que se lean bien
    plt.xticks(posiciones[::3], etiquetas[::3], rotation=45)
    
    # Textos claros y explicativos
    plt.title("¿Volvemos a tener el millón exacto? Error al comprar dólares y volver a pesos en el mismo mes", fontsize=12)
    plt.xlabel("Mes y Año analizado", fontsize=10)
    plt.ylabel("Diferencia en Pesos Chilenos (CLP)", fontsize=10)
    
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(loc='upper right')
    plt.tight_layout()
    
    # Guardar en la carpeta graficos/
    ruta_imagen = os.path.join(carpeta_graficos, "grafica_ida_vuelta.png")
    plt.savefig(ruta_imagen, dpi=300)
    plt.close()
   

if __name__ == "__main__":
    datos = cargar_datos()
    resolver_b1()
    resolver_b4()
    derivado_float32, derivado_float64 = resolver_b2(datos)
    graficos(datos, derivado_float32, derivado_float64)
