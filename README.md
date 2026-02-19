# 🚀 FastAPI Starter - Clean Architecture

Este proyecto utiliza una estructura de **Arquitectura Limpia** para separar las responsabilidades y facilitar el escalado.

## 📂 Estructura del Proyecto

### 1. `app/models/`
Contiene las **entidades de datos puros**. Aquí se definen las tablas de la base de datos (SQLAlchemy/Tortoise).
* **Función:** Representar cómo se guardan los datos en el disco.
* **Ejemplo:** Modelo `Producto` (id, sku, precio).

### 2. `app/schemas/`
Define los **esquemas de Pydantic** para la validación de datos (JSON).
* **Función:** Validar qué datos entran y salen de la API.
* **Diferencia:** El *model* es para la DB, el *schema* es para el cliente.

### 3. `app/services/`
Contiene la **Lógica de Negocio**. Es el núcleo de la aplicación.
* **Función:** Aplicar reglas de negocio (descuentos, cálculos, procesos).
* **Regla de oro:** No conocen la existencia de la API; solo procesan datos.

### 4. `app/api/`
Define las **Rutas y Endpoints** de FastAPI.
* **Función:** Recibir peticiones, llamar al servicio correspondiente y devolver la respuesta.
* **Nota:** No contienen lógica compleja, solo dirigen el tráfico.

### 5. `app/core/`
Configuraciones globales y constantes del sistema.
* **Contenido:** Conexión a DB, variables de entorno (`.env`), seguridad (JWT) y logs.


## 🛠️ Cómo arrancar el proyecto

Para iniciar el servidor en modo desarrollo con recarga automática, ejecuta:

```bash
uv run fastapi dev app/main.py
```

### Un detalle importante:
Al usar `fastapi dev`, el comando espera encontrar la variable `app = FastAPI()` dentro de `main.py`.