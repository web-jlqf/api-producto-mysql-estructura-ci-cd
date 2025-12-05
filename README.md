# API REST de Productos (FastAPI + Arquitectura por Capas)


Esta API REST implementa un CRUD básico de productos utilizando FastAPI, con una arquitectura organizada en tres capas principales:

1. Routers (Controladores / Endpoints HTTP)
2. Services (Lógica de negocio)
3. Models (Acceso a datos con SQL directo)

Se conecta a una base de datos MySQL, pero evita ORMs y programación declarativa para mantener el ejemplo simple y académico.

##  Descripción de Componentes

- **main.py**: Punto de entrada de la aplicación. Inicializa FastAPI y monta los routers.
- **db.py**: Configura la conexión a la base de datos.
- **routers/**: Define los endpoints HTTP que exponen la funcionalidad de la API.
    - product_router.py
- **services/**: Implementa la lógica de negocio, separando responsabilidades del controlador.
    - product_service.py
- **models/**: Contiene los modelos que interactúan directamente con la base de datos.
    - product_model.py
      
## Routers (Controladores / Vistas HTTP)

Responsabilidades:

- Definir endpoints (GET, POST, DELETE, etc.)..
- Recibir solicitudes HTTP (req).
- Devolver respuestas HTTP (res) con códigos apropiados.
- Validar el formato de entrada (Pydantic mínimo).
- Llaman a los servicios.
- No contienen lógica de negocio.

```python
@router.post("/", status_code=201)
def create_product(product: ProductIn):
    new_product = add_product(product.dict())
    return { ... }

```

## Services (Lógica de negocio)

Responsabilidades:

- Validan reglas de negocio.
Ejemplo: precio e inventario no pueden ser negativos.
- Orquestan las acciones.
- Llaman a los modelos para acceder a los datos.
- No realizan SQL.
- No devuelven respuestas HTTP, solo datos o excepciones.

```python
if price < 0:
    raise ValueError("El precio no puede ser negativo.")

```

## Models (Acceso a datos / SQL directo)

Responsabilidades:

- Ejecutan instrucciones SQL sin ORM.
- Transforman filas en objetos.
- Solo manejan datos, no reglas de negocio.
- Se apoyan en db.py para conectar a MySQL.

```python
cursor.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)")

```

## Ejecución

### Crear entorno virtual (opcional pero recomendado)

```bash
python3 -m venv .venv
source .venv/bin/activate
```
### Instalar dependencias

```bash
pip install fastapi uvicorn mysql-connector-python
```

### Ejecutar la API

```bash
uvicorn main:app --host 0.0.0.0 --port XXX
```

### Probar la API

Abrir en el navegador:
```bash
http://servidor:PUERTO/docs
```


