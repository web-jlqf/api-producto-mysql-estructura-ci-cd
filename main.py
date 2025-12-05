# main.py
from fastapi import FastAPI
from routers.product_router import router as product_router
from fastapi.middleware.cors import CORSMiddleware
from models.product_model import create_table_if_not_exists

app = FastAPI(title="API REST  - Productos")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],  # Permitir todos los encabezados
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)
@app.on_event("startup")
def startup_event():
    # Crear la tabla cuando la app arranca
    create_table_if_not_exists()


app.include_router(product_router)

# Si quieres algo de prueba:
@app.get("/")
def root():
    return {"message": "API de productos funcionando"}
