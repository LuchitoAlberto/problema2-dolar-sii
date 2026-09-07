import os
import sys
import numpy as np
import matplotlib.pyplot as plt

from cargar_datos import cargar_datos

def resolver_B1():
    print("\n--- B1. Cifras significativas y mantisa corta ---")

    valor_real = 1000.76
    valor_aprox3 = 1000.0 #1000.76 truncado a 3 cifras significativas (1.00 * 10^3)

    error_absoluto = abs(valor_real - valor_aprox3)
    error_relativo = (error_absoluto / valor_real) * 100

    print(f"Precio original:             {valor_real}")
    print(f"Precio aproximado (3 cifras): {valor_aprox3}")
    print(f"Error absoluto:              {error_absoluto:.2f} CLP")
    print(f"Error relativo porcentual:   {error_relativo:.4f}%")
    print("Respuesta B1:")
    print("En computacion un numero en punto flotante guarda sus digitos en la mantisa.")
    print("Redondear a solo 2 o 3 cifras equivale a tener una mantisa de muy pocos bits en binario,")
    print("lo que descarta los decimales y mete error de representacion.\n")

def resolver_B2(datos):
    print("--- B2. Prueba de ida y vuelta ---")

    monto_inicial = 1_000_000.00
    precios = datos['precio']

    monto_float32 = np.float32(monto_inicial) #monto inicial en float32
    precio_float32 = precios.astype(np.float32) #precio en float32
    dolares_comprados_float32 = (monto_float32 / precio_float32) #comprar dolares
    precios_recu_float32 = (dolares_comprados_float32 * precio_float32) #volver a pesos
    derivado_float32 = precios_recu_float32 - monto_float32 #diferencia respecto al millon

    dolares_comprados_float64 = (monto_inicial / precios) #en float64
    precios_recu_float64 = (dolares_comprados_float64 * precios)
    derivado_float64 = precios_recu_float64 - monto_inicial

    print(f"Monto de trabajo: ${monto_inicial:,.2f} CLP")
    print(f"Maxima diferencia en float32: ${np.max(np.abs(derivado_float32)):.4f} CLP")
    print(f"Maxima diferencia en float64: ${np.max(np.abs(derivado_float64)):.4e} CLP")
    print("Respuesta B2: ¿Siguen el mismo patron de movimiento?")
    print("Si, el error se varia segun el valor del dolar de cada mes,")
    print("porque ciertos precios generan decimales periodicos que no caben exactos en el binario.\n")

    return derivado_float32, derivado_float64

def resolver_B4():
    print("--- B4. Cancelacion en la maquina ---")

    precio_1 = 874.67
    precio_2 = 875.66

    valor_exacto = precio_1 - precio_2 # -0.99

    p1_float32 = np.float32(precio_1) #en 32 bits
    p2_float32 = np.float32(precio_2)
    resta1 = p1_float32 - p2_float32
    error1 = abs(float(resta1) - valor_exacto)

    p1_float64 = np.float64(precio_1) #en 64 bits
    p2_float64 = np.float64(precio_2)
    resta2 = p1_float64 - p2_float64
    error2 = abs(float(resta2) - valor_exacto)

    print(f"Resta teorica exacta: {valor_exacto:.6f}")
    print(f"Resta en float32:     {resta1:.10f} | Error frente al exacto: {error1:.2e}")
    print(f"Resta en float64:     {resta2:.10f} | Error frente al exacto: {error2:.2e}")
    print("\nRespuesta B4:")
    print("- Cifras validas en float32: float32 solo tiene 7 cifras decimales. Como ambos numeros")
    print("  compartian las primeras cifras (87...), al restarse se cancelan y quedan solo unas 3 o 4 cifras validas.")
    print("- Cifras validas en float64: Como tiene 16 cifras decimales, la perdida no afecta y quedan casi 13 cifras validas.")
    print("- Conexion con A3: Es la misma cancelacion que calculamos a mano en A3,")
    print("  solo que aqui ocurre directamente en el computador por la falta de bits.\n")

def graficos(datos, derivado_float32, derivado_float64):
    carpeta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    carpeta_graficos = os.path.join(carpeta_raiz, 'graficos')
    os.makedirs(carpeta_graficos, exist_ok=True) #crear carpeta si no existe
    
    #etiquetas de meses tipo Ene-22
    etiquetas = [f"{d['mes'][:3]}-{str(d['anio'])[2:]}" for d in datos]
    posiciones = np.arange(len(datos))
    
    plt.figure(figsize=(12, 5))
    
    plt.plot(posiciones, derivado_float32, marker='o', markersize=3, color='red', label='Precision float32 (32 bits)')
    plt.plot(posiciones, derivado_float64, linestyle='--', color='blue', label='Precision float64 (64 bits)')
    
    plt.axhline(0, color='black', linewidth=1, linestyle=':', label='Valor exacto ($0 error)')
    
    plt.xticks(posiciones[::3], etiquetas[::3], rotation=45)
    plt.title("Deriva en punto flotante al comprar y vender en el mismo mes")
    plt.xlabel("Mes")
    plt.ylabel("Diferencia respecto al millon ($ CLP)")
    
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    
    ruta_imagen = os.path.join(carpeta_graficos, "5_grafica_ida_vuelta.png")
    plt.savefig(ruta_imagen, dpi=300) #alta calidad
    plt.close()
    print("Grafico guardado en: graficos/grafica_ida_vuelta.png\n")

if __name__ == "__main__":
    datos = cargar_datos()
    resolver_B1()
    resolver_B4()
    derivado_float32, derivado_float64 = resolver_B2(datos)
    graficos(datos, derivado_float32, derivado_float64)