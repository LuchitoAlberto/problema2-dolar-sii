import numpy as np
import os
import matplotlib.pyplot as plt
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

    print("\n--- A1. Error de representacion mes a mes (2 cifras) ---")
    print("Mes       | Real ($)  | Aprox 2C  | Error Abs | Error Rel (%)")
    print("-" * 57)
    for i in range(len(precios)):
        print(f"{etiquetas[i]:<9} | {precios[i]:>9.2f} | {aprox_2c[i]:>9.1f} | {ea[i]:>9.2f} | {er[i]:>9.2f}%")
        
    print("-" * 57)
    print(f"Respuesta A1: El mes con mayor error relativo al redondear fue {etiquetas[indice_max_er]} ({meses[indice_max_er]} {anios[indice_max_er]})")
    print(f"Precio real: ${precios[indice_max_er]:.2f} | Redondeado: ${aprox_2c[indice_max_er]:.0f}")
    print(f"Dejo un error absoluto de ${ea[indice_max_er]:.2f} CLP y un error relativo de {er[indice_max_er]:.2f}%\n")

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

    #en multiplicacion y division se suman los relativos
    er_pesos_final = er_compra + er_venta
    ea_pesos_final = pesos_final * (er_pesos_final / 100)

    #en la resta se pasa el error absoluto tal cual (el millon inicial no tiene error)
    ganancia_aprox = pesos_final - monto
    ea_ganancia = ea_pesos_final
    er_ganancia = (ea_ganancia / np.abs(ganancia_aprox)) * 100

    ganancia_real = ((monto / p_compra_real) * p_venta_real) - monto

    print("--- A2. Evaluacion compra-venta ($1.000.000 CLP) ---")
    print(f"Mes de compra: {etiquetas[indice_compra]} (Real: ${p_compra_real:.2f}, Aprox: ${p_compra_aprox:.0f})")
    print(f"Mes de venta:  {etiquetas[indice_venta]} (Real: ${p_venta_real:.2f}, Aprox: ${p_venta_aprox:.0f})")
    print(f"Ganancia real exacta:    ${ganancia_real:,.2f} CLP")
    print(f"Ganancia con redondeo:   ${ganancia_aprox:,.2f} CLP")
    print(f"Error propagado:         ±${ea_ganancia:,.2f} CLP (error porcentual: {er_ganancia:.2f}%)")
    print(f"Respuesta A2: La ganancia final es ${ganancia_aprox:,.2f} ± ${ea_ganancia:,.2f} CLP\n")

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

    print("--- A3. Cancelacion entre diciembres (3 cifras) ---")
    print(f"Dic 2022: real = {precio_dic2022:.2f} | aprox (3 cifras) = {precio_dic2022_aprox:.1f}")
    print(f"Dic 2023: real = {precio_dic2023:.2f} | aprox (3 cifras) = {precio_dic2023_aprox:.1f}")
    print(f"Variacion real:   ΔP = {diferencia_real:.2f} CLP")
    print(f"Variacion aprox:  ΔP = {diferencia_aprox:.2f} CLP")
    print(f"Error propagado:  ±{ea_diferencia:.2f} CLP")
    print(f"Error relativo:   {er_diferencia:.2f}%")
    print(f"Intervalo con margen: [{diferencia_aprox - ea_diferencia:.2f}, {diferencia_aprox + ea_diferencia:.2f}] CLP")
    print("Respuesta A3: ¿Se puede afirmar con seguridad si subio o bajo?")
    print("Si, se puede afirmar que bajo porque ambos extremos del intervalo son negativos [-1.67, -0.33].")
    print("Sin embargo, la incertidumbre es enorme (67.68%), casi tan grande como el valor de la resta misma.\n")

def resolver_A4(datos):
    print("--- A4. Variacion anual (Enero a Diciembre) ---")

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

    #ordenamos de menor a mayor error porcentual
    resultados.sort(key=lambda item: item[4])

    print("Año   | Dif Real  | Dif Aprox | Error Abs  | Error Rel (%)")
    print("-" * 55)
    for r in resultados:
        anio, d_real, d_aprox, e_propagado, e_porcentual = r
        print(f"{anio}  | {d_real:>9.2f} | {d_aprox:>9.2f} | ±{e_propagado:>8.2f}  | {e_porcentual:>12.2f}%")
    print("-" * 55)
    print("Respuesta A4: Los años menos confiables (como 2023) tienen en comun que la diferencia real")
    print("fue muy chica, por lo que el error de redondeo acumulado se vuelve dominante frente a la resta.\n")

def resolver_A5(precios, etiquetas):
    print("--- A5. Mejor compra y mejor venta ---")

    indice_min = np.argmin(precios)
    indice_max = np.argmax(precios)

    precio_min = precios[indice_min]
    precio_max = precios[indice_max]

    precio_min_aprox = redondear(precio_min, 2)
    precio_max_aprox = redondear(precio_max, 2)

    rentabilidad = ((precio_max - precio_min) / precio_min) * 100
    rentabilidad_aprox = ((precio_max_aprox - precio_min_aprox) / precio_min_aprox) * 100

    #propagamos los relativos
    er_compra = (np.abs(precio_min - precio_min_aprox) / precio_min) * 100
    er_venta = (np.abs(precio_max - precio_max_aprox) / precio_max) * 100
    er_total = er_compra + er_venta

    ea_rentabilidad = rentabilidad_aprox * (er_total / 100)

    print(f"Mejor compra (minimo): {etiquetas[indice_min]} -> Real: ${precio_min:.2f} | Aprox: ${precio_min_aprox:.0f}")
    print(f"Mejor venta (maximo):  {etiquetas[indice_max]} -> Real: ${precio_max:.2f} | Aprox: ${precio_max_aprox:.0f}")
    print(f"Rentabilidad real:     {rentabilidad:.2f}%")
    print(f"Rentabilidad aprox:    {rentabilidad_aprox:.2f}% ± {ea_rentabilidad:.2f}%")
    print(f"Rango de rentabilidad: [{rentabilidad_aprox - ea_rentabilidad:.2f}%, {rentabilidad_aprox + ea_rentabilidad:.2f}%]")
    print("Respuesta A5: ¿La conclusion sobrevive al error?")
    print("Si, totalmente. La rentabilidad es de alrededor del 25% mientras que la incertidumbre")
    print("es menor al 1%, asi que la recomendacion de compra y venta conlleva a un profit claro.\n")

def generar_graficos(precios, etiquetas, aprox_2c, ea, er):
    carpeta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    carpeta_graficos = os.path.join(carpeta_raiz, 'graficos')
    os.makedirs(carpeta_graficos, exist_ok=True) #crear carpeta si no existe

    posiciones = np.arange(len(precios)) #0 a 47

    # 1. Serie mensual del dolar observado 2022-2025 (linea)
    plt.figure(figsize=(11, 4))
    plt.plot(posiciones, precios, color='blue', label='Dólar observado')
    plt.xticks(posiciones[::3], etiquetas[::3], rotation=45)
    plt.title("Serie mensual del dólar observado (2022 - 2025)")
    plt.xlabel("Mes")
    plt.ylabel("Precio ($ CLP)")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(carpeta_graficos, "1_serie_tiempo.png"), dpi=300)
    plt.close()

    # 2. Variacion mes a mes ΔP (barras con error propagado)
    delta_real = np.diff(precios) #precio mes siguiente - precio actual
    error_delta = ea[:-1] + ea[1:] #se suman los errores absolutos en la resta
    pos_delta = np.arange(len(delta_real))
    etiquetas_delta = etiquetas[1:]

    plt.figure(figsize=(11, 4))
    plt.bar(pos_delta, delta_real, yerr=error_delta, capsize=2, color='skyblue', edgecolor='black', label='ΔP ± error')
    plt.axhline(0, color='black', linewidth=1)
    plt.xticks(pos_delta[::3], etiquetas_delta[::3], rotation=45)
    plt.title("Variación mes a mes (ΔP)")
    plt.xlabel("Mes")
    plt.ylabel("Variación ($ CLP)")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(carpeta_graficos, "2_variacion_mes_a_mes.png"), dpi=300)
    plt.close()

    # 3. Error de representacion por mes a 2 cifras (barras de un solo color)
    plt.figure(figsize=(11, 4))
    plt.bar(posiciones, er, color='cornflowerblue', edgecolor='black')
    plt.xticks(posiciones[::3], etiquetas[::3], rotation=45)
    plt.title("Error relativo de representación mes a mes (2 cifras)")
    plt.xlabel("Mes")
    plt.ylabel("Error relativo (%)")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(carpeta_graficos, "3_error_representacion.png"), dpi=300)
    plt.close()

    # 4. Rentabilidad comprando en el minimo y vendiendo despues
    indice_min = np.argmin(precios) #febrero 2023
    p_compra_aprox = aprox_2c[indice_min]
    er_compra = er[indice_min]

    meses_posteriores = posiciones[indice_min + 1:]
    etiquetas_posteriores = etiquetas[indice_min + 1:]

    rentabilidad = []
    error_rentabilidad = []

    for i in meses_posteriores:
        p_venta_aprox = aprox_2c[i]
        er_venta = er[i]

        rent_aprox = ((p_venta_aprox - p_compra_aprox) / p_compra_aprox) * 100
        er_total = er_compra + er_venta
        ea_rent = rent_aprox * (er_total / 100)

        rentabilidad.append(rent_aprox)
        error_rentabilidad.append(ea_rent)

    plt.figure(figsize=(11, 4))
    plt.errorbar(range(len(meses_posteriores)), rentabilidad, yerr=error_rentabilidad, fmt='-o', markersize=3, color='purple', ecolor='gray', capsize=2)
    plt.axhline(0, color='black', linewidth=1, linestyle='--')
    plt.xticks(range(len(meses_posteriores))[::2], etiquetas_posteriores[::2], rotation=45)
    plt.title("Rentabilidad comprando en el mínimo y vendiendo en meses posteriores")
    plt.xlabel("Mes de venta")
    plt.ylabel("Rentabilidad (%)")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(carpeta_graficos, "4_rentabilidad_minimo.png"), dpi=300)
    plt.close()

if __name__ == "__main__":
    datos = cargar_datos()
    
    anios = datos['anio']
    meses = datos['mes']
    precios = datos['precio']
    
    etiquetas = [f"{str(m)[:3]}-{str(a)[2:]}" for m, a in zip(meses, anios)]
    
    aprox_2c, ea, er = resolver_A1(meses, anios, precios, etiquetas)
    resolver_A2(precios, etiquetas)
    resolver_A3()
    resolver_A4(datos)
    resolver_A5(precios, etiquetas)
    
    generar_graficos(precios, etiquetas, aprox_2c, ea, er)