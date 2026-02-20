from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from schemas.product import ProductCreate

app = FastAPI()


app.mount("/static", StaticFiles(directory="app/static"), name="static")    # Montar el CSS
templates = Jinja2Templates(directory="app/templates")                      # Config Plantilla JINJA

db_temporal = []

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "titulo": "FastAPI Starter",
        "usuario": "Usuario Ejemplo",
        "mensaje": "Gestión de Inventario",
        "productos": db_temporal                                            # Enviar la lista
    })


@app.post("/productos")                                                     # Recibir los datos del formulario
async def crear_producto(
    nombre: str = Form(...), 
    precio: float = Form(...), 
    correo: str = Form(...)
):
    # Usamos Pydantic para validar que los datos son correctos
    nuevo_producto = ProductCreate(nombre=nombre, precio=precio, correo=correo)
    
    db_temporal.append(nuevo_producto.model_dump())                         # Guardar como un diccionario(modeldump)
    
    return RedirectResponse(url="/", status_code=303)                       # Redirige a la url "/"