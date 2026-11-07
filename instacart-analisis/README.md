# 📊 Instacart Data Processing with Pandas

Evidencia GA1-220501094-01-AA1-EV06 en la rama `feature/pandas-data-processing`.

Este repositorio documenta la preparación, limpieza, análisis y combinación de datos de Instacart con Python y Pandas, siguiendo la guía del curso en cuatro etapas:

1. Lección 2: limpieza y estandarización de datos
2. Lección 3: filtrado, ordenamiento y agrupación
3. Lección 4: combinación de datasets y tabla maestra
4. Documentación final del proyecto y resultados procesados

---

## 📁 Estructura del proyecto

```text
instacart-analisis/
├── data/
│   ├── aisles.csv
│   ├── departments.csv
│   ├── instacart_orders.csv
│   ├── order_products.csv
│   ├── processed/
│   │   ├── department_summary.csv
│   │   └── instacart_master_table.csv
│   └── products.csv
├── notebooks/
│   └── pandas_labs.ipynb
├── .gitignore
├── gen_data.py
├── README.md
├── requirements.txt
├── run_notebook.py
└── .venv/
```

---

## 🧹 Qué incluye el laboratorio

El notebook principal `notebooks/pandas_labs.ipynb` desarrolla la evidencia completa de forma ejecutable y ordenada:

- Diagnóstico inicial del conjunto de datos
- Pipeline de limpieza con reporte de cambios
- Validación de duplicados, tipos, texto y valores nulos
- Filtros, segmentación por cliente y análisis temporal
- Agrupaciones por hora, día, departamento y frecuencia de recompra
- Mezcla de tablas con integridad de claves y relación cardinal
- Guardado de resultados procesados en `data/processed/`

---

## 📦 Datasets base

Los archivos CSV se leen con `sep=';'` y corresponden a un conjunto mínimo de Instacart:

- `instacart_orders.csv`: pedidos, usuarios y tiempos de compra
- `products.csv`: catálogo de productos
- `aisles.csv`: pasillos de productos
- `departments.csv`: departamentos comerciales
- `order_products.csv`: detalle de cada producto en cada pedido

---

## 📝 Resultados procesados

La cuarta lección genera una tabla maestra y un resumen por departamento que quedan almacenados en:

- `data/processed/instacart_master_table.csv`
- `data/processed/department_summary.csv`

Estos archivos permiten reutilizar la combinación de datos sin recalcular el merge desde cero.

---

## 🚀 Ejecución local

1. Crear o activar el entorno virtual.
2. Instalar dependencias:

```bash
python -m pip install -r requirements.txt
```

3. Ejecutar el notebook principal con Jupyter o nbclient:

```bash
jupyter notebook notebooks/pandas_labs.ipynb
```

También puede ejecutarse con la utilidad incluida:

```bash
python run_notebook.py
```

---

## ✅ Validación

La evidencia se valida ejecutando el notebook completo y comprobando que:

- el pipeline de limpieza no rompe la integridad de los datos,
- los ejercicios de Reto 2 y Reto 3 producen resultados coherentes,
- la combinación de datasets genera la tabla maestra sin errores de cardinalidad,
- los archivos de salida en `data/processed/` se guardan correctamente.

---

## 📌 Estado del proyecto

El proyecto queda documentado en la rama `feature/pandas-data-processing` con el flujo completo de limpieza, análisis y combinación de datasets para la evidencia GA1-220501094-01-AA1-EV06.