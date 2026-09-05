datos_anios = [
    {"anio": 2022, "enero": 822.05, "diciembre": 875.66},
    {"anio": 2023, "enero": 826.34, "diciembre": 874.67},
    {"anio": 2024, "enero": 907.99, "diciembre": 982.30},
    {"anio": 2025, "enero": 1000.76, "diciembre": 916.16}
]

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

    error_enero = abs(precio_enero - precio_enero_aprox) #error absoluto en enero que la formula es (precio real - precioaproximado)
    error_diciembre = abs(precio_diciembre - precio_diciembre_aprox) #error absoluto en diciembre que la formula es (precio real - precioaproximado)

    var_real = precio_diciembre - precio_enero #variación real que la formula es (precio diciembre - precio enero)
    var_aprox = precio_diciembre_aprox - precio_enero_aprox #variación aproximada que la formula es (precio diciembre aproximado - precio enero aproximado)

    error_absoltuto = error_enero + error_diciembre #el error absoluto es la suma de los errores absolutos de enero y diciembre
    error_porcentual = (error_absoltuto / abs(var_real)) * 100 #error relativo procentual de la variacion
    resultados.append({
        "anio": anio,
        "var_real": var_real,
        "var_aprox": var_aprox,
        "error_absoluto": error_absoltuto,
        "error_porcentual": error_porcentual
    })

#con esto se ordena los datos de menor a mayor error porcentual
resultados_ordenados = sorted(resultados, key=lambda x: x["error_porcentual"])

print("Año\tVariación Real\tVariación Aproximada\tError Absoluto\tError Porcentual")
for item in resultados_ordenados:
    print(f"{item['anio']}\t{item['var_real']}\t{item['var_aprox']}\t{item['error_absoluto']}\t{item['error_porcentual']}")