from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()


app.mount("/static", StaticFiles(directory="app/static"), name="static")    # Montar el CSS


templates = Jinja2Templates(directory="app/templates")                      # Config Plantilla JINJA

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    
    datos_ejemplo = {                                                       # Simular BBDD
        "titulo": "Mi Starter Pro",
        "usuario": "angelsandev",
        "tecnologias": ["FastAPI", "Jinja2", "Python", "SQLAlchemy"]
    }
    
    
    return templates.TemplateResponse(                                      # Enviar datos a plantilla index.html
        request=request, 
        name="index.html", 
        context=datos_ejemplo
    )