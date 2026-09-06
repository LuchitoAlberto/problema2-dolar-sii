import numpy as np
from cargar_datos import cargar_datos

#redondeo a n cifras significativas usando potencias de 10
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
    er = error_r(precios, aprox_2c)

    indice_max_er = np.argmax(er)

    print("=" * 70)
    print("A1. ERROR DE REPRESENTACIÓN MES A MES (A 2 CIFRAS)")
    print("=" * 70)
    print(f"{'Etiqueta':<10} | {'Real ($)':<10} | {'Aprox 2C':<10} | {'Ea ($)':<10} | {'Er (%)':<10}")
    print("-" * 70)
    for i in range(len(precios)):
        print(f"{etiquetas[i]:<10} | {precios[i]:<10.2f} | {aprox_2c[i]:<10.1f} | {ea[i]:<10.2f} | {er[i]:<10.2f}%")
        
    print("-" * 70)
    print(f"Mes con mayor error relativo: {etiquetas[indice_max_er]} ({meses[indice_max_er]} {anios[indice_max_er]})")
    print(f"Precio real: ${precios[indice_max_er]:.2f} | Aprox: ${aprox_2c[indice_max_er]:.0f}")
    print(f"Error absoluto: ${ea[indice_max_er]:.2f} CLP | Error relativo: {er[indice_max_er]:.2f}%\n")

    return aprox_2c, ea, er

def resolver_A2(precios, etiquetas):
    monto = 1000000

    #elegimos marzo 2022 (compra) y julio 2022 (venta)
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

    #en multiplicación y división se suman los errores relativos
    er_pesos_final = er_compra + er_venta
    ea_pesos_final = pesos_final * (er_pesos_final / 100)

    #ganancia: resta (el monto no tiene error)
    ganancia_aprox = pesos_final - monto
    ea_ganancia = ea_pesos_final
    er_ganancia = (ea_ganancia / np.abs(ganancia_aprox)) * 100

    ganancia_real = ((monto / p_compra_real) * p_venta_real) - monto

    print("=" * 70)
    print("A2. SIMULACIÓN DE COMPRA-VENTA ($1.000.000 CLP)")
    print("=" * 70)
    print(f"Compra: {etiquetas[indice_compra]} (Real: ${p_compra_real:.2f}, Aprox: ${p_compra_aprox:.0f})")
    print(f"Venta:  {etiquetas[indice_venta]} (Real: ${p_venta_real:.2f}, Aprox: ${p_venta_aprox:.0f})")
    print(f"Ganancia real calculada: ${ganancia_real:,.2f} CLP")
    print(f"Ganancia aproximada:     ${ganancia_aprox:,.2f} CLP")
    print(f"Error propagado:         ±${ea_ganancia:,.2f} CLP ({er_ganancia:.2f}%)")
    print(f"Resultado: Ganancia = ${ganancia_aprox:,.2f} ± ${ea_ganancia:,.2f} CLP\n")

def resolver_A3():
    precio_dic2022 = 875.66
    precio_dic2023 = 874.67

    precio_dic2022_aprox = redondear(precio_dic2022, 3)
    precio_dic2023_aprox = redondear(precio_dic2023, 3)

    ea_dic22 = error_a(precio_dic2022, precio_dic2022_aprox)
    ea_dic23 = error_a(precio_dic2023, precio_dic2023_aprox)

    diferencia_real = precio_dic2023 - precio_dic2022
    diferencia_aprox = precio_dic2023_aprox - precio_dic2022_aprox

    #en la resta se suman los errores absolutos
    ea_diferencia = ea_dic23 + ea_dic22
    er_diferencia = (ea_diferencia / np.abs(diferencia_real)) * 100

    print("=" * 70)
    print("A3. CANCELACIÓN (DICIEMBRE 2022 vs DICIEMBRE 2023 A 3 CIFRAS)")
    print("=" * 70)
    print(f"Dic 2022 real: {precio_dic2022:.2f} | Aprox: {precio_dic2022_aprox:.1f} (Ea: {ea_dic22:.2f})")
    print(f"Dic 2023 real: {precio_dic2023:.2f} | Aprox: {precio_dic2023_aprox:.1f} (Ea: {ea_dic23:.2f})")
    print(f"Variación real:     ΔP = {diferencia_real:.2f} CLP")
    print(f"Variación aprox:    ΔP = {diferencia_aprox:.2f} CLP")
    print(f"Error propagado:    ±{ea_diferencia:.2f} CLP")
    print(f"Error relativo:     {er_diferencia:.2f}%")
    print(f"Rango con margen:   [{diferencia_aprox - ea_diferencia:.2f}, {diferencia_aprox + ea_diferencia:.2f}] CLP")
    print("\n¿Se puede afirmar con seguridad si subió o bajó?")
    print("El intervalo queda en [-1.67, -0.33], ambos negativos, por lo que bajó.")
    print("Pero el error relativo es muy grande (~67.68%), casi tan grande como el valor.\n")

def resolver_A4(datos):
    print("=" * 70)
    print("A4. VARIACIÓN ANUAL (ENERO A DICIEMBRE)")
    print("=" * 70)

    anios = [2022, 2023, 2024, 2025]
    resultados = []

    for a in anios:
        datos_anio = datos[datos['anio'] == a]

        precio_enero = datos_anio['precio'][0]
        precio_diciembre = datos_anio['precio'][-1]

        precio_enero_aprox = redondear(precio_enero, 2)
        precio_diciembre_aprox = redondear(precio_diciembre, 2)

        diferencia = precio_diciembre - precio_enero
        diferencia_aprox = precio_diciembre_aprox - precio_enero_aprox

        ea_enero = error_a(precio_enero, precio_enero_aprox)
        ea_diciembre = error_a(precio_diciembre, precio_diciembre_aprox)
        error_propagado = ea_enero + ea_diciembre

        error_porcentual = (error_propagado / np.abs(diferencia)) * 100

        resultados.append((a, diferencia, diferencia_aprox, error_propagado, error_porcentual))

    #ordenamos de menor a mayor error relativo
    resultados.sort(key=lambda item: item[4])

    print("Año   | Dif Real | Dif Aprox | Error Abs  | Error Rel (%)")
    print("---------------------------------------------------------")
    for r in resultados:
        anio, d_real, d_aprox, e_propagado, e_porcentual = r
        print(f"{anio}  | {d_real:8.2f} | {d_aprox:9.2f} | ±{e_propagado:9.2f} | {e_porcentual:12.2f}%")
    print("---------------------------------------------------------")
    print("Los años poco confiables tienen en común que la variación neta fue chica,")
    print("haciendo que el error de redondeo domine sobre la diferencia real.\n")

def resolver_A5(precios, etiquetas):
    print("=" * 70)
    print("A5. MEJOR COMPRA Y MEJOR VENTA")
    print("=" * 70)

    indice_min = np.argmin(precios)
    indice_max = np.argmax(precios)

    precio_min = precios[indice_min]
    precio_max = precios[indice_max]

    precio_min_aprox = redondear(precio_min, 2)
    precio_max_aprox = redondear(precio_max, 2)

    rentabilidad = ((precio_max - precio_min) / precio_min) * 100
    rentabilidad_aprox = ((precio_max_aprox - precio_min_aprox) / precio_min_aprox) * 100

    #propagamos los errores relativos
    er_compra = (np.abs(precio_min - precio_min_aprox) / precio_min) * 100
    er_venta = (np.abs(precio_max - precio_max_aprox) / precio_max) * 100
    er_total = er_compra + er_venta

    ea_rentabilidad = rentabilidad_aprox * (er_total / 100)

    print(f"Comprar en mínimo: {etiquetas[indice_min]} -> Real: ${precio_min:.2f} | Aprox: ${precio_min_aprox:.0f}")
    print(f"Vender en máximo:  {etiquetas[indice_max]} -> Real: ${precio_max:.2f} | Aprox: ${precio_max_aprox:.0f}")
    print(f"Rentabilidad real: {rentabilidad:.2f}%")
    print(f"Rentabilidad aprox: {rentabilidad_aprox:.2f}% ± {ea_rentabilidad:.2f}%")
    print(f"Margen estimado:   [{rentabilidad_aprox - ea_rentabilidad:.2f}%, {rentabilidad_aprox + ea_rentabilidad:.2f}%]")

    print("\n¿La conclusión sobrevive al error?")
    print("Sí, porque la rentabilidad esperada ronda el 25% frente a un error menor al 1%,")
    print("por lo que la ganancia es clara y la conclusión no queda en duda.\n")

if __name__ == "__main__":
    datos = cargar_datos()
    
    anios = datos['anio']
    meses = datos['mes']
    precios = datos['precio']
    
    etiquetas = [f"{str(m)[:3]}-{str(a)[2:]}" for m, a in zip(meses, anios)]
    
    resolver_A1(meses, anios, precios, etiquetas)
    resolver_A2(precios, etiquetas)
    resolver_A3()
    resolver_A4(datos)
    resolver_A5(precios, etiquetas)