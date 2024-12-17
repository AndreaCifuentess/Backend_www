from tortoise import fields, models

class Tarea(models.Model):
    id = fields.IntField(pk=True,auto_increment=True)
    titulo = fields.CharField(max_length=255)
    descripcion = fields.TextField(null=True)
    completado = fields.BooleanField(null=False, default=False)
    fecha_creacion = fields.DatetimeField(null=False, auto_now_add=True)

    class Meta:
        table = "tareas"