from src.models.tarea_model import Tarea
from tortoise.exceptions import DoesNotExist
from datetime import datetime

class TareaController:
    @staticmethod
    async def create_tarea(titulo, descripcion):
        tarea_obj = await Tarea.create(titulo= titulo, descripcion=descripcion)
        return tarea_obj

    @staticmethod
    async def read_tarea(tarea_id: int):
        try:
            tarea = await Tarea.get(id=tarea_id)
            return tarea
        except DoesNotExist:
            return None

    @staticmethod
    async def update_tarea(tarea_id: int, tarea_data):
        try:
            tarea_obj = await Tarea.get(id=tarea_id)
            tarea_obj.titulo = tarea_data.titulo
            tarea_obj.descripcion = tarea_data.descripcion
            tarea_obj.completado = tarea_data.completado
            await tarea_obj.save()
            return tarea_obj
        except DoesNotExist:
            return None

    @staticmethod
    async def delete_tarea(tarea_id: int):
        try:
            tarea = await Tarea.get(id=tarea_id)
            await tarea.delete()
            return True
        except DoesNotExist:
            return False
