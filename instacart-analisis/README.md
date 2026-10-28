# 📊 Fundamentos en Pandas – Explorando Instacart

**Evidencia:** GA1-220501094-01-AA1-EV04 – Fundamentos en Pandas Explorando Instacart: descubre patrones de compra

**Programa:** Tecnólogo en Análisis y Desarrollo de Software – SENA

---

## 📋 Descripción del proyecto

Este proyecto explora los datos de **Instacart** (pedidos de supermercado) utilizando Python y la librería **Pandas**. A través de un notebook Jupyter se realizan actividades de carga, exploración inicial, diagnóstico de calidad, indexación/filtrado, cálculo de indicadores y **visualización de datos**.

La pregunta orientadora es: **¿Cómo utilizar Python y Pandas para explorar los datos de Instacart, identificar las características de los pedidos y productos, y obtener información relevante sobre los hábitos de compra de sus clientes?**

---

## 📁 Estructura del proyecto

```
instacart-analisis/
├── data/
│   ├── .gitkeep
│   ├── aisles.csv
│   ├── departments.csv
│   ├── instacart_orders.csv
│   ├── order_products.csv
│   └── products.csv
├── notebooks/
│   └── 00_entorno.ipynb
├── .gitignore
├── gen_data.py
├── README.md
├── requirements.txt
└── run_notebook.py
```

---

## 📂 Descripción de los datasets

| Archivo | Descripción | Columnas clave |
|---|---|---|
| `instacart_orders.csv` | Atributos de cada pedido | `order_id`, `user_id`, `order_number`, `order_dow`, `order_hour_of_day`, `days_since_prior_order` |
| `products.csv` | Catálogo de productos | `product_id`, `product_name`, `aisle_id`, `department_id` |
| `aisles.csv` | Nombres de pasillos | `aisle_id`, `aisle` |
| `departments.csv` | Nombres de departamentos | `department_id`, `department` |
| `order_products.csv` | Artículos dentro de cada pedido | `order_id`, `product_id`, `add_to_cart_order`, `reordered` |

> **Nota:** Los archivos CSV usan `;` como separador.

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd instacart-analisis
```

### 2. Crear entorno virtual (recomendado)

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el notebook

**Opción A – Jupyter Notebook:**
```bash
jupyter notebook notebooks/00_entorno.ipynb
```

**Opción B – Ejecutar automáticamente:**
```bash
python run_notebook.py
```

**Opción C – Google Colab:**
1. Sube los 5 archivos CSV a la sesión de Colab.
2. Abre el notebook `00_entorno.ipynb`.
3. Ejecuta todas las celdas (Run All).

---

## 📓 Contenido del notebook

El notebook está organizado en **7 momentos**:

| Momento | Tema | Descripción |
|---|---|---|
| 1 | Comprensión del problema | Reconocimiento de los datos y preguntas iniciales |
| 2 | Importación y exploración inicial | Carga de CSV con `sep=";"`, `head()`, `tail()`, `shape` |
| 3 | Estructura y calidad | `info()`, `dtypes`, detección de valores ausentes, tabla de diagnóstico |
| 4 | Indexación y filtrado | `loc[]`, máscaras booleanas, operadores `&` y `\|` |
| 5 | Indicadores básicos | Promedios, conteos, proporciones, `describe()`, moda |
| 6 | Visualización de datos | Histogramas, gráficos de barras, distribuciones (matplotlib/seaborn) |
| 7 | Análisis avanzado | `groupby`, `merge`, tablas dinámicas, visualizaciones combinadas |

---

## 📊 Visualizaciones incluidas

- Histograma de pedidos por hora del día
- Distribución de días entre pedidos
- Proporción de artículos recomprados (reordered)
- Top 10 productos más frecuentes
- Top 10 departamentos con más productos
- Relación entre hora del pedido y número de pedido (boxplot)
- Heatmap de correlación entre variables numéricas

---

## 🛠️ Tecnologías utilizadas

- **Python 3.10+**
- **Pandas** – manipulación y análisis de datos
- **Matplotlib** – visualización de datos
- **Seaborn** – visualización estadística
- **NumPy** – operaciones numéricas
- **Jupyter Notebook** – entorno interactivo
- **nbformat / nbclient** – ejecución programática de notebooks

---

## ✅ Verificación para la entrega

1. Ejecuta **Run All** y confirma que no haya errores.
2. Verifica que `DATA_DIR` apunte a la carpeta donde están los CSV.
3. Completa tu nombre, programa y ficha en la portada del notebook.
4. Revisa que las salidas de indicadores y las conclusiones correspondan a los resultados.
5. Guarda el archivo `.ipynb` con las salidas si así lo solicita tu instructor.

---

## 📝 Licencia

Proyecto académico – SENA. Uso educativo.