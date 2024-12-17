TORTOISE ={
   "connections": {
       "default" : "postgres://postgres:12345@localhost:5433/AdmiTareas"
   },
   "apps": {
       "models": {
           "models": ["src.models.tarea_model"],
           "default_connection": "default",
       }
   }

}

async def init():
    await Tortoise.init(config=TORTOISE)
    await Tortoise.generate_schemas()