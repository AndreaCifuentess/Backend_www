from fastapi import APIRouter, HTTPException
from src.controllers.tarea_controller import TareaController
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class TareaIn(BaseModel):
    id: int
    titulo: str
    descripcion: str | None = None
    fecha_creacion: datetime
    completado: bool

class TareaOut(TareaIn):
    titulo: str
    descripcion: str 

##Crear tarea
@router.post("/tareas", response_model=TareaOut)
async def create_tarea(tarea: TareaIn):
    tarea_obj = await TareaController.create_tarea(tarea.titulo,tarea.descripcion)
    return await TareaOut.from_tortoise_orm(tarea_obj)

@router.get("/tareas/{tarea_id}", response_model=TareaOut)
async def read_tarea(tarea_id: int):
    tarea = await TareaController.read_tarea(tarea_id)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return await TareaOut.from_tortoise_orm(tarea)

@router.put("/tareas/{tarea_id}", response_model=TareaOut)
async def update_tarea(tarea_id: int, tarea: TareaIn):
    tarea_obj = await TareaController.update_tarea(tarea_id, tarea)
    if tarea_obj is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return await TareaOut.from_tortoise_orm(tarea_obj)

@router.delete("/tareas/{tarea_id}")
async def delete_tarea(tarea_id: int):
    success = await TareaController.delete_tarea(tarea_id)
    if not success:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"detail": "Tarea eliminada"}
