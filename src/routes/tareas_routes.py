from fastapi import APIRouter, HTTPException
from src.controllers.tarea_controller import TareaController
from pydantic import BaseModel
from datetime import datetime
from typing import List

router = APIRouter()

class TareaIn(BaseModel):
    titulo: str
    descripcion: str 

class TareaOut(TareaIn):
    id: int
    completado: bool
    fecha_creacion: datetime

    class Config:
        orm_mode = True


##Crear tarea
@router.post("/tareas", response_model=TareaOut)
async def create_tarea(tarea: TareaIn):
    tarea_obj = await TareaController.create_tarea(tarea.titulo,tarea.descripcion)
    return tarea_obj 

##Obtener tareas
@router.get("/obtener_tareas", response_model=List[TareaOut])
async def read_all_tareas():
    tareas = await TareaController.read_all_tareas()  # Llamada al controlador
    if not tareas:
        raise HTTPException(status_code=404, detail="No se encontraron tareas")
    
    # Conversión de cada tarea a TareaOut manualmente
    return [
        TareaOut(
            id=tarea.id,
            titulo=tarea.titulo,
            descripcion=tarea.descripcion,
            completado=tarea.completado,
            fecha_creacion=tarea.fecha_creacion
        )
        for tarea in tareas
    ]

##Editar Tarea no sirve
@router.put("/editar_tarea/{tarea_id}", response_model=TareaOut)
async def update_tarea(tarea_id: int, tarea: TareaIn):
    print("Datos recibidos:", tarea.model_dump())
    tarea_obj = await TareaController.update_tarea(tarea_id, tarea)
    if not tarea_obj:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea_obj



## Eliminar tarea
@router.delete("/borrar_tarea/{tarea_id}")
async def delete_tarea(tarea_id: int):
    success = await TareaController.delete_tarea(tarea_id)
    if not success:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"detail": "Tarea eliminada"}
