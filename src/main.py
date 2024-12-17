from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.routes import tareas_routes

app = FastAPI()
app.title = "Gestor de Tareas"

app.include_router(tareas_routes.router)

@app.get("/")
def home():
    return {"message": "Hello, world"}

# Conexión con la base de datos
register_tortoise(
    app,
    db_url="postgres://postgres:12345@localhost:5433/AdmiTareas",
    modules={"models": ["src.models.tarea_model"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


