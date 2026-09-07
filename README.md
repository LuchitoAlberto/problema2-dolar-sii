# Laboratorio 1 - Computación Numérica (UCM)

**Integrantes:**
* Luis Manzur
* Antonella Mondaca

---

En este trabajo analizamos cómo afecta redondear a pocas cifras significativas y qué pasa cuando restamos precios muy parecidos, usando el promedio mensual del dólar en Chile publicado por el SII.

### Archivos del proyecto
* `data/`: Contiene el CSV con los precios mensuales del dólar.
* `src/cargar_datos.py`: Script para leer el archivo CSV usando NumPy.
* `src/errores.py`: Resuelve las preguntas de error (A1 a A5) y guarda los primeros 4 gráficos.
* `src/anualidad.py`: Revisa la variación de enero a diciembre para cada año.
* `src/punto_flotante.py`: Pruebas de float32 vs float64, ida y vuelta con el millón de pesos y gráfico 5.
* `graficos/`: Carpeta donde se guardan las imágenes generadas.
* `INFORME.md`: Respuestas a las preguntas finales sobre cuándo convenía comprar y vender.

### Cómo ejecutar los códigos

Instalar las librerías necesarias:
```bash
pip install -r requirements.txt
```

Para correr los scripts:
```bash
python src/errores.py
python src/anualidad.py
python src/punto_flotante.py