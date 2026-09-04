import numpy as np
from cargar_datos import cargar_datos

def redondear(arreglo, cifras):
    arreglo = np.asarray(arreglo, dtype=float)

    es_cero = (arreglo == 0)
    arreglo_seguro = np.where(es_cero, 1, arreglo)

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

    print("=" * 70)
    print("A1. ERROR DE REPRESENTACIÓN MES A MES (A 2 CIFRAS SIGNIFICATIVAS)")
    print("=" * 70)
    print(f"{' Etiqueta':<10} | {'Real ($)':<10} | {'Aprox 2C':<10} | {'Ea ($)':<10} | {'Er (%)':<10}")
    print("-" * 70)
    for i in range(len(precios)):
        print(f"{etiquetas[i]:<10} | {precios[i]:<10.2f} | {aprox_2c[i]:<10.1f} | {ea[i]:<10.2f} | {er[i]:<10.2f}%")
        
    print("-" * 70)
    print(f"   Mes con MAYOR error relativo: {etiquetas[indice_max_er]} ({meses[indice_max_er]} {anios[indice_max_er]})")
    print(f"   Precio real: ${precios[indice_max_er]:.2f} | Aprox: ${aprox_2c[indice_max_er]:.0f}")
    print(f"   Error absoluto: ${ea[indice_max_er]:.2f} CLP | Error relativo: {er[indice_max_er]:.2f}%\n")

    return aprox_2c, ea, er

def resolver_A2(precios, etiquetas):
    monto = 1000000

    indice_compra = 2
    indice_venta = 6

    p_compra_real = precios[indice_compra]
    p_venta_real = precios[indice_venta]

    p_compra_aprox = redondear(p_compra_real, 2)
    p_venta_aprox = redondear(p_venta_real, 2)

    er_compra = error_r(p_compra_real, p_compra_aprox)
    er_venta = error_r(p_venta_real, p_venta_aprox)

    dolar_aprox = monto / p_compra_aprox
    pesos_final = dolar_aprox * p_venta_aprox

    er_pesos_final = er_compra + er_venta
    ea_pesos_final = pesos_final * (er_pesos_final / 100)

    ganancia_aprox = pesos_final - monto
    ea_ganancia = ea_pesos_final
    er_ganancia = (ea_ganancia / np.abs(ganancia_aprox)) * 100

    ganancia_real = ((monto / p_compra_real) * p_venta_real) - monto

    print("=" * 70)
    print("A2. EVALUACIÓN ENTRE DOS PUNTOS (COMPRA-VENTA DE $1.000.000 CLP)")
    print("=" * 70)
    print(f"Compra en: {etiquetas[indice_compra]} (Real: ${p_compra_real:.2f}, Aprox: ${p_compra_aprox:.0f}, Er: {er_compra:.2f}%)")
    print(f"Venta en:  {etiquetas[indice_venta]} (Real: ${p_venta_real:.2f}, Aprox: ${p_venta_aprox:.0f}, Er: {er_venta:.2f}%)")
    print(f"Ganancia Real Calculada: ${ganancia_real:,.2f} CLP")
    print(f"Ganancia Aproximada:     ${ganancia_aprox:,.2f} CLP")
    print(f"Error Propagado:         ±${ea_ganancia:,.2f} CLP (Error Porcentual: {er_ganancia:.2f}%)")
    print(f"Resultado final: Ganancia = ${ganancia_aprox:,.2f} ± ${ea_ganancia:,.2f} CLP\n")

if __name__ == "__main__":
    anios, meses, precios, etiquetas, matriz = cargar_datos()
    resolver_A1(meses, anios, precios, etiquetas)
    resolver_A2(precios, etiquetas)
    pass