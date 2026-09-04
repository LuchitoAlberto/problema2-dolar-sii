import numpy as np

def redondear(arreglo, cifras):
    arreglo = np.asarray(arreglo, dtype=float)

    es_cero = (arreglo == 0)
    arreglo_seguro = np.where(es_cero, 1.0, arreglo)

    magnitud = np.floor(np.log10(np.abs(arreglo_seguro)))
    factor = 10 ** (cifras - 1 - magnitud)

    redondeado = np.round(arreglo_seguro * factor) / factor
    return np.where(es_cero, 0, redondeado)

def error_a(real, aprox):
    return np.abs(real - aprox)

def error_r(real, aprox):
    return (error_a(real, aprox) / np.abs(real)) * 100

def resolver_A1(meses, anios, precios, etiquetas):
    aprox_2c = redondear(precios, 2)
    ea = error_a(precios, aprox_2c)
    er = error_a(precios, aprox_2c)

    indice_max_er = np.argmax(er)

    