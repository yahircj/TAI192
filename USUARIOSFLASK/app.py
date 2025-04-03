from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = "supersecreto"

FASTAPI_URL = "http://127.0.0.1:5001"

@app.route("/", methods=["GET"])
def home():
    return render_template("registro.html")

@app.route("/consulta", methods=["GET"])
def consulta():
    return render_template("consulta.html")

#añadir
@app.route("/usuariosFastAPI", methods=["POST"])
def post_usuario():
    try:
        usuarioNuevo = {
            "name": request.form["txtNombre"],
            "age": int(request.form["txtEdad"]),
            "email": request.form["txtCorreo"]
        }

        response = requests.post(f"{FASTAPI_URL}/addUsuarios/", json=usuarioNuevo)

        if response.status_code in [200, 201]:
            flash("Usuario guardado correctamente", "success")
        else:
            flash(f"Error al guardar usuario: {response.json().get('detail', 'Error desconocido')}", "danger")

        return redirect(url_for("home"))

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "No se pudo conectar con la API", "detalle": str(e)}), 500

#Mostrar registros
@app.route("/consultaUsuarios", methods=["GET"])
def get_usuarios():
    try:
        response = requests.get(f"{FASTAPI_URL}/todosUsuarios/")
        response.raise_for_status()
        usuarios = response.json()

        return render_template("consulta.html", usuarios=usuarios)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "No se pudo conectar con la API", "detalle": str(e)}), 500

#Eliminar
@app.route("/eliminarUsuario/<int:id>", methods=["POST"])
def eliminar_usuario(id):
    try:
        response = requests.delete(f"{FASTAPI_URL}/eliminarUsuario/{id}")
        if response.status_code == 200:
            flash("Usuario eliminado correctamente", "success")
        else:
            flash("Error al eliminar usuario", "danger")
        return redirect(url_for("get_usuarios"))
    except requests.exceptions.RequestException as e:
        flash("No se pudo conectar con la API", "danger")
        return redirect(url_for("get_usuarios"))

# Actualizar
@app.route("/editarUsuario/<int:id>", methods=["GET", "POST"])
def editar_usuario(id):
    if request.method == "GET":
        try:
            response = requests.get(f"{FASTAPI_URL}/usuario/{id}")
            if response.status_code == 200:
                usuario = response.json()
                return render_template("editar.html", usuario=usuario)
            else:
                flash("Usuario no encontrado", "danger")
                return redirect(url_for("get_usuarios"))
        except requests.exceptions.RequestException as e:
            flash("No se pudo conectar con la API", "danger")
            return redirect(url_for("get_usuarios"))
    else:
        usuarioActualizado = {
            "name": request.form["txtNombre"],
            "age": int(request.form["txtEdad"]),
            "email": request.form["txtCorreo"]
        }
        try:
            response = requests.put(f"{FASTAPI_URL}/actualizarUsuarios/{id}", json=usuarioActualizado)
            if response.status_code == 200:
                flash("Usuario actualizado correctamente", "success")
            else:
                flash("Error al actualizar usuario", "danger")
            return redirect(url_for("get_usuarios"))
        except requests.exceptions.RequestException as e:
            flash("No se pudo conectar con la API", "danger")
            return redirect(url_for("get_usuarios"))

if __name__ == "__main__":
    app.run(debug=True, port=8002)
