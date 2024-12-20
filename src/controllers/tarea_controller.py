from src.models.tarea_model import Tarea
from tortoise.exceptions import DoesNotExist
from datetime import datetime

class TareaController:
    @staticmethod
    async def create_tarea(titulo: str, descripcion: str):
        tarea_obj = await Tarea.create(
            titulo=titulo,
            descripcion=descripcion
        )
        return tarea_obj

    @staticmethod
    async def read_all_tareas():
     return await Tarea.all()

    @staticmethod
    async def update_tarea(tarea_id: int, tarea_data):
        tarea_obj = await Tarea.get_or_none(id=tarea_id)
        if tarea_obj:
            tarea_obj.titulo = tarea_data.titulo
            tarea_obj.descripcion = tarea_data.descripcion
            tarea_obj.completado = tarea_data.completado  
            await tarea_obj.save()
            return tarea_obj
        return None

    @staticmethod
    async def delete_tarea(tarea_id: int):
        tarea = await Tarea.get_or_none(id=tarea_id)
        if tarea:
            await tarea.delete()
            return True
        return False
