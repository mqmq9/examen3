from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Configura Jinja2 para manejar las plantillas HTML
templates = Jinja2Templates(directory="app/templates")

# Endpoint para servir la página principal
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Endpoint para obtener información de la marca
@app.get("/api/brand-info")
async def get_brand_info():
    return {
        "name": "Silence",
        "description": "Ropa básica con estilo streetwear",
        "motto": "Donde el estilo habla por sí solo"
    }
