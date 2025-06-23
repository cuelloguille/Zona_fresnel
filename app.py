from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        try:
            distancia = float(request.form["distancia"])  # en km
            frecuencia = float(request.form["frecuencia"])  # en GHz
            if distancia <= 0 or frecuencia <= 0:
                resultado = "⚠️ Los valores deben ser mayores a cero."
            else:
                fresnel = 8.656 * ((distancia / frecuencia) ** 0.5)
                resultado = f"🔍 El radio de la Zona de Fresnel es de: {fresnel:.2f} metros."
        except ValueError:
            resultado = "⚠️ Por favor, ingrese solo números válidos."
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
