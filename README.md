📝 Proyecto de Notas "Post-it" con FastAPI
¡Una aplicación web simple pero poderosa para gestionar notas al estilo "Post-it", construida con la magia de Python y FastAPI!

Este proyecto es una demostración perfecta de cómo construir una aplicación web Full-Stack (backend y frontend) con FastAPI, sirviendo HTML dinámico con plantillas Jinja2.

🚀 Características Principales
Crear Notas: Añade nuevas notas a través de un formulario simple.
Ver Notas: Visualiza todas tus notas en la página principal.
Eliminar Notas: Borra las notas que ya no necesites con un solo clic.

🔧 Cómo Ponerlo en Marcha
¡Empezar es súper fácil! Solo sigue estos pasos.

1. Dependencias del Proyecto
Primero, necesitarás las herramientas adecuadas. Este proyecto depende de unas pocas librerías clave de Python.

Puedes instalarlas todas con pip:

Bash

pip install fastapi uvicorn jinja2 python-multipart
fastapi: El framework web.

uvicorn: El servidor ASGI para ejecutar nuestra app.

jinja2: El motor de plantillas para renderizar nuestro HTML.

python-multipart: Necesario para recibir datos de formularios HTML.

2. Ejecuta el Servidor
Una vez que tengas las dependencias, ¡enciende el motor! Desde la carpeta raíz de tu proyecto, ejecuta:

Bash

uvicorn main:app --reload
El comando --reload es fantástico para el desarrollo, ya que reinicia el servidor automáticamente cada vez que guardas cambios en tu código.

--------------------------------------------------------------------------------------------------------------------

💡 ¿Cómo Funciona? (La Lógica)

1. El Almacenamiento (Temporal)
En lugar de una base de datos compleja, todas las notas se guardan en una simple lista de Python que vive en la memoria del servidor.

Python
# main.py
nota = []

2. Los Endpoints (Las Rutas)
La aplicación tiene 3 rutas principales que manejan toda la lógica:

GET / (La Página Principal)

Qué hace: Muestra la página de inicio.

Cómo: Usa Jinja2Templates para renderizar el archivo index.html y le pasa la lista completa de nota para que el HTML pueda mostrarlas.

POST /notas/add (Crear Nota)

Qué hace: Recibe los datos del formulario cuando envías una nueva nota.

Cómo: Crea un diccionario de nota (new_nota), le asigna un ID único (uuid4), lo añade a la lista nota, y te redirige de vuelta a la página principal (/).

GET /notas/delete (Borrar Nota)

Qué hace: Elimina una nota específica.

Cómo: Recibe el nota_id desde la URL, lo busca en la lista nota y lo elimina. Después, te redirige de vuelta a la página principal (/).

<img width="3835" height="2174" alt="Captura de pantalla 2025-11-11 140905" src="https://github.com/user-attachments/assets/20eac35a-4d10-4628-a25e-6fba0cf85fb6" />

