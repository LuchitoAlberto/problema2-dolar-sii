import numpy as np
from cargar_datos import cargar_datos

#cargamos los datos con numpy desde el CSV
datos = cargar_datos()

#armamos la lista de anios usando los datos cargados
datos_anios = []
for a in [2022, 2023, 2024, 2025]:
    datos_anio = datos[datos['anio'] == a]
    datos_anios.append({
        "anio": a,
        "enero": float(datos_anio['precio'][0]),
        "diciembre": float(datos_anio['precio'][-1])
    })

def redondear(valor):
    if valor >= 1000:
        return round(valor, -2)
    else:
        return round(valor, -1)

resultados = []

for item in datos_anios:
    anio = item["anio"]
    precio_enero = item["enero"]
    precio_diciembre = item["diciembre"]

    precio_enero_aprox = redondear(precio_enero) #redondeado a 2 cifras significativas
    precio_diciembre_aprox = redondear(precio_diciembre) #redondeado a 2 cifras significativas

    error_enero = round(abs(precio_enero - precio_enero_aprox), 2) #error absoluto en enero que la formula es (precio real - precioaproximado)
    error_diciembre = round(abs(precio_diciembre - precio_diciembre_aprox), 2) #error absoluto en diciembre que la formula es (precio real - precioaproximado)

    var_real = round(precio_diciembre - precio_enero, 2) #variación real que la formula es (precio diciembre - precio enero)
    var_aprox = round(precio_diciembre_aprox - precio_enero_aprox, 2) #variación aproximada que la formula es (precio diciembre aproximado - precio enero aproximado)

    error_absoluto = round(error_enero + error_diciembre, 2) #el error absoluto es la suma de los errores absolutos de enero y diciembre
    error_porcentual = round((error_absoluto / abs(var_real)) * 100, 2) #error relativo procentual de la variacion
    resultados.append({
        "anio": anio,
        "var_real": var_real,
        "var_aprox": var_aprox,
        "error_absoluto": error_absoluto,
        "error_porcentual": error_porcentual
    })

#con esto se ordena los datos de menor a mayor error porcentual
resultados_ordenados = sorted(resultados, key=lambda x: x["error_porcentual"])

print("Año\tVariación Real\tVariación Aproximada\tError Absoluto\tError Porcentual")
for item in resultados_ordenados:
    print(f"{item['anio']}\t{item['var_real']}\t\t{item['var_aprox']}\t\t\t{item['error_absoluto']}\t\t{item['error_porcentual']}%")