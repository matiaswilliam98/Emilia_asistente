from flask import Flask, render_template, request, session, redirect
import os
from groq_client import obtener_respuesta


app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

print("Valor de __name__:", __name__)

# @app.route("/saludo")
# def saludar():
#     return "ola"

@app.route("/", methods=["GET", "POST"])
def chat():
    if "mensajes" not in session:
        session["mensajes"] = [{"autor": "emilia", "mensaje": "¡Hola! Soy EMILIA, tu asistente de apoyo emocional. ¿Cómo te sientes hoy?"}]
    if request.method == "POST":
        texto_usuario = request.form["mensaje"]
        mensajes = session["mensajes"]
        mensajes.append({"autor": "usuario", "mensaje": texto_usuario})
        respuesta_emilia = obtener_respuesta(texto_usuario)
        mensajes.append({"autor": "emilia", "mensaje": respuesta_emilia})
        session["mensajes"] = mensajes
        return redirect("/")
    return render_template("chat.html", mensajes=session["mensajes"])

if __name__ == "__main__":
    app.run(debug=True)


