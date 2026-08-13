# API REST de Tareas (To-Do List)

API RESTful simple hecha con **Flask** para gestionar una lista de tareas. Cumple con:
- Más de 2 endpoints funcionales (5 en total)
- Respuestas en formato JSON
- Documentación básica en la ruta raíz (`/`)
- Lista para desplegar en Render, Railway, Fly.io o Cyclic

## Endpoints

| Método | Ruta                  | Descripción                          |
|--------|-----------------------|---------------------------------------|
| GET    | `/`                   | Documentación básica de la API        |
| GET    | `/api/tareas`         | Lista todas las tareas                |
| GET    | `/api/tareas/<id>`    | Obtiene una tarea por id              |
| POST   | `/api/tareas`         | Crea una nueva tarea                  |
| PUT    | `/api/tareas/<id>`    | Actualiza una tarea existente         |
| DELETE | `/api/tareas/<id>`    | Elimina una tarea                     |

### Ejemplo de body para POST/PUT
```json
{
  "titulo": "Repasar para el examen",
  "completada": false
}
```

## Cómo correrla en local

```bash
pip install -r requirements.txt
python app.py
```

Luego abre en el navegador: `http://127.0.0.1:5000/api/tareas`

Para probar POST/PUT/DELETE usa **Postman** o **curl**, por ejemplo:

```bash
curl -X POST http://127.0.0.1:5000/api/tareas \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Nueva tarea"}'
```

## Cómo desplegarla en Render (gratis)

1. Sube estos archivos (`app.py`, `requirements.txt`, `Procfile`) a un repositorio de GitHub.
2. Entra a [render.com](https://render.com) y crea una cuenta (puedes usar tu GitHub).
3. Clic en **New +** → **Web Service**.
4. Conecta tu repositorio de GitHub.
5. Configura:
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
6. Clic en **Create Web Service** y espera a que despliegue.
7. Render te dará una URL pública (algo como `https://tu-api.onrender.com`) donde puedes probar los endpoints, por ejemplo: `https://tu-api.onrender.com/api/tareas`.

> Nota: en el plan gratis de Render, la API "duerme" tras un rato de inactividad y tarda unos segundos en despertar en la primera petición — es normal.
