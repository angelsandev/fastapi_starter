from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()


app.mount("/static", StaticFiles(directory="app/static"), name="static")    # Montar el CSS
templates = Jinja2Templates(directory="app/templates")                      # Config Plantilla JINJA

db_temporal = []

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "titulo": "EAN - FastAPI Starter",
        "usuario": "EAN - User",
        "mensaje": "Gestión de Inventario",
        "productos": db_temporal                                            # Enviar la lista
    })


@app.post("/productos")                                                     # Recibir los datos del formulario
async def crear_producto(nombre: str = Form(...), correo: str = Form(...)):
    nuevo_item = f"{nombre} - {correo}"
    db_temporal.append(nuevo_item)
    #print(f"Producto recibido: {nombre}")
    #print(f"Lista actual: {db_temporal}")
    
    return RedirectResponse(url="/", status_code=303)                       # Redirige a la url "/"