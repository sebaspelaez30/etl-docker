# ETL Pipeline con Docker, Python y PostgreSQL

Este proyecto implementa un pipeline **ETL (Extract – Transform – Load)** completamente dockerizado.
El objetivo es extraer datos desde una API pública, validarlos y transformarlos con **Pydantic**, y cargarlos en una base de datos **PostgreSQL**.

El diseño está orientado a buenas prácticas de ingeniería de datos: modularidad, validación explícita y reproducibilidad del entorno.

---

## Descripción general

El flujo del proyecto es el siguiente:

### Extract
- Consumo de datos desde la API pública `https://dummyjson.com/products`
- Peticiones HTTP usando `requests`

### Transform
- Limpieza de campos textuales
- Conversión explícita de tipos
- Validación estricta mediante modelos **Pydantic**
- Manejo de estructuras anidadas (`dimensions`, `reviews`)

### Load
- Inserción de los datos en **PostgreSQL**
- Creación automática de la tabla si no existe
- Manejo de conflictos por clave primaria

Todo el pipeline se ejecuta desde un único punto de entrada (`main.py`).

---

## Tecnologías utilizadas

- Python  
- Docker  
- Docker Compose  
- PostgreSQL  
- Pydantic  
- Requests  
- psycopg2  

---

## Estructura del proyecto

etl-docker/
├── Dockerfile
├── docker-compose.yml
├── main.py
├── fetch.py
├── transform.py
├── load.py
├── models.py
├── checker.py
├── products.csv
├── requirements.txt
└── README.md


---

## Descripción de archivos

- **main.py**  
  Punto de entrada del pipeline. Ejecuta el flujo extract → transform → load.

- **fetch.py**  
  Encargado de la extracción de datos desde la API externa.

- **transform.py**  
  Limpieza, tipado y validación de los datos usando modelos Pydantic.

- **models.py**  
  Definición de los modelos de datos `Product`, `Dimensions` y `Reviews`.

- **load.py**  
  Inserta los datos transformados en PostgreSQL y gestiona la creación de la tabla.

- **checker.py**  
  Script auxiliar para analizar campos faltantes en la fuente de datos.

---

## Ejecución con Docker

### Requisitos previos
- Docker Desktop  
- Docker Compose  

### Levantar el pipeline

```bash
docker compose up --build
```

### Detener los servicios

```bash
docker compose down
```

### Base de datos

La base de datos PostgreSQL se inicializa automáticamente con la siguiente tabla:

products (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    category TEXT,
    price REAL,
    rating REAL,
    stock INTEGER,
    brand TEXT,
    weight REAL
)

La conexión se gestiona mediante la variable de entorno DATABASE_URL