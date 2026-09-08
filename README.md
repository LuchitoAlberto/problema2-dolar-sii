# Laboratorio 1 - Computación Numérica (UCM)

**Integrantes:**
* Luis Manzur
* Antonella Mondaca

---

## Descripción del Proyecto
En este laboratorio se analiza el impacto del redondeo en punto flotante y el fenómeno de "cancelación catastrófica" al operar con el valor mensual del dólar observado en Chile con datos del SII entre enero de 2022 y diciembre de 2025. 

Se evalúan estrategias de compra y venta propagando errores en operaciones de multiplicación, división y resta, determinando numéricamente en qué casos las decisiones financieras son confiables y en cuáles el margen de error destruye la certeza del resultado.

---

## Estructura del Repositorio

```text
problema2-dolar-sii/
├── README.md                <- descripción del proyecto y forma de uso
├── INFORME.md               <- documento de entrega con el análisis financiero
├── requirements.txt         <- dependencias necesarias (numpy, matplotlib)
├── data/
│   └── dolar_observado_sii_2022_2025.csv <- dataset oficial del SII (48 meses)
├── src/
│   ├── cargar_datos.py      <- carga del archivo CSV con NumPy (structured array)
│   ├── errores.py           <- resolución preguntas A1 a A5 y gráficos 1 al 4
│   ├── anualidad.py         <- variación y error año a año de enero a diciembre
│   └── punto_flotante.py    <- pruebas en float32/float64, ida y vuelta y gráfico 5
└── graficos/                <- figuras generadas en formato PNG
    ├── 1_serie_tiempo.png
    ├── 2_variacion_mes_a_mes.png
    ├── 3_error_representacion.png
    ├── 4_rentabilidad_minimo.png
    └── 5_grafica_ida_vuelta.png
```

---

## Instalación de dependencias

Para instalar las librerías necesarias se ocupa pip:

```bash
pip install -r requirements.txt
```

---

## Ejecución de los scripts

Para ejecutar los cálculos y generar las imágenes en la carpeta `graficos/`:

```bash
# 1. Cálculos de error (A1 a A5) y gráficos 1 al 4:
python src/errores.py

# 2. Variación anual (Enero a Diciembre):
python src/anualidad.py

# 3. Pruebas de punto flotante, ida y vuelta y gráfico 5:
python src/punto_flotante.py
```