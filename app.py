from flask import Flask, jsonify, request

app = Flask(__name__)

# "Base de datos" en memoria (simple, sin necesidad de instalar nada más)
tareas = [
    {"id": 1, "titulo": "Aprender Flask", "completada": False},
    {"id": 2, "titulo": "Desplegar API en la nube", "completada": False},
]
siguiente_id = 3


@app.route("/", methods=["GET"])
def inicio():
    """Documentación básica de la API"""
    return jsonify({
        "mensaje": "API REST de gestión de tareas",
        "endpoints": {
            "GET /api/tareas": "Lista todas las tareas",
            "GET /api/tareas/<id>": "Obtiene una tarea por su id",
            "POST /api/tareas": "Crea una nueva tarea (JSON: {\"titulo\": \"...\"})",
            "PUT /api/tareas/<id>": "Actualiza una tarea existente",
            "DELETE /api/tareas/<id>": "Elimina una tarea"
        }
    })


@app.route("/api/tareas", methods=["GET"])
def obtener_tareas():
    return jsonify(tareas), 200


@app.route("/api/tareas/<int:tarea_id>", methods=["GET"])
def obtener_tarea(tarea_id):
    tarea = next((t for t in tareas if t["id"] == tarea_id), None)
    if tarea is None:
        return jsonify({"error": "Tarea no encontrada"}), 404
    return jsonify(tarea), 200


@app.route("/api/tareas", methods=["POST"])
def crear_tarea():
    global siguiente_id
    datos = request.get_json(silent=True)

    if not datos or "titulo" not in datos:
        return jsonify({"error": "El campo 'titulo' es obligatorio"}), 400

    nueva_tarea = {
        "id": siguiente_id,
        "titulo": datos["titulo"],
        "completada": datos.get("completada", False)
    }
    tareas.append(nueva_tarea)
    siguiente_id += 1
    return jsonify(nueva_tarea), 201


@app.route("/api/tareas/<int:tarea_id>", methods=["PUT"])
def actualizar_tarea(tarea_id):
    tarea = next((t for t in tareas if t["id"] == tarea_id), None)
    if tarea is None:
        return jsonify({"error": "Tarea no encontrada"}), 404

    datos = request.get_json(silent=True) or {}
    tarea["titulo"] = datos.get("titulo", tarea["titulo"])
    tarea["completada"] = datos.get("completada", tarea["completada"])
    return jsonify(tarea), 200


@app.route("/api/tareas/<int:tarea_id>", methods=["DELETE"])
def eliminar_tarea(tarea_id):
    global tareas
    tarea = next((t for t in tareas if t["id"] == tarea_id), None)
    if tarea is None:
        return jsonify({"error": "Tarea no encontrada"}), 404

    tareas = [t for t in tareas if t["id"] != tarea_id]
    return jsonify({"mensaje": "Tarea eliminada correctamente"}), 200


if __name__ == "__main__":
    app.run(debug=True)
