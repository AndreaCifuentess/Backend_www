#Backend_www

Aplicación del lado del servidor para la gestión de tareas, que permite crear, ver, borrar y editar las tareas.
La aplicación esta desarrollada en fastApi, un framework para crear Apis con pyhton.

Se instalaron dependencias como tprtoise-orm

Guia de ejecución:

Clonar repositorio Se debe crear el ambiente virtual, si se desea: python -m venv env 
Se activa el ambiente: ./env/Scripts/Activate 
Se procede a instalar las dependencias: pip install -r requirements.txt 
Se inicia el proyecto: uvicorn src.main:app --reload
