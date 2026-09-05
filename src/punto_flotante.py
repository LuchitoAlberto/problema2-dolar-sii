import numpy as np
from matplotlib.pyplot import plt


def resolver_b1():
    valor_real = 1000.76
    valor_aprox3 = 1000.0 #valor con 3 cifras significativas 1000.76 * 10^0 = 1.00076 * 10^3 = 1.00 * 10^3 = 1000.0

    error_absoluto = abs(valor_real - valor_aprox3)
    error_relativo = (error_absoluto / valor_real) * 100
    print(f"Error relativo: {error_relativo:.2f}%")
    pass

def resolver_b4():
    precio_1 = 874.67
    precio_2 = 875.66
    valor_exacto = precio_1 - precio_2
    p1_float32 = np.float32(precio_1) #valor con 32 bits
    p2_float32 = np.float32(precio_2) #valor con 32 bits
    resta = p1_float32 - p2_float32
    error = abs(resta - valor_exacto)
    print(f"Error absoluto en 32 bits: {error}")

    p1_float64 = np.float64(precio_1) #valor con 64 bits
    p2_float64 = np.float64(precio_2) #valor con 64 bits
    resta = p1_float64 - p2_float64
    error = abs(resta - valor_exacto)
    print(f"Error absoluto en 64 bits: {error}")
    pass

def resolver_b2():
    monto_inicial = 1_000_000.00
    precios = datos['precio'] #esto lo puse asi pero no se como sacar los datos de anualidad o de cargar datos xDDD
    monto_float32 = np.float32(monto_inicial) #monto inicial en float32
    precio_float32 = precios.astype(np.float32) #precio en float32
    dolares_comp_float32 = (monto_float32 / precio_float32) #comprar dolares
    precios_recu_float32 = (dolares_comp_float32 * precio_float32) #volver a pesos
    dolares_comp_float64 = (monto_inicial / precios) #comprar dolares en float64
    precios_recu_float64 = (dolares_comp_float64 * precios) #volver a pesos en float64
    pass

