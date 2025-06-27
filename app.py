from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    distancia = ''
    frecuencia = ''
    fresnel_truncado = None
    altura1 = None
    altura2 = None

    if request.method == "POST":
        distancia = request.form.get("distancia", '')
        frecuencia = request.form.get("frecuencia", '')
        altura1_raw = request.form.get("altura1", '')
        altura2_raw = request.form.get("altura2", '')

        # Intentar convertir inputs a float cuando se pueda
        errores = []

        try:
            distancia_f = float(distancia)
            if distancia_f <= 0:
                errores.append("⚠️ La distancia debe ser un número positivo.")
        except ValueError:
            errores.append("⚠️ La distancia debe ser un número válido (usar punto como separador decimal).")

        try:
            frecuencia_f = float(frecuencia)
            if frecuencia_f <= 0:
                errores.append("⚠️ La frecuencia debe ser un número positivo.")
        except ValueError:
            errores.append("⚠️ La  frecuencia debe ser un número válido (usar punto como separador decimal).")

        # Altura1 valida y positiva si está presente
        try:
            if altura1_raw.strip() != '':
                altura1 = float(altura1_raw)
                if altura1 <= 0:
                    errores.append("⚠️ La altura de la antena 1 debe ser un número positivo.")
            else:
                altura1 = None
        except ValueError:
            errores.append("⚠️ La altura de la antena 1 debe ser un número válido (usar punto como separador decimal).")
            altura1 = None

        # Altura2 valida y positiva si está presente
        try:
            if altura2_raw.strip() != '':
                altura2 = float(altura2_raw)
                if altura2 <= 0:
                    errores.append("⚠️ La altura de la antena 2 debe ser un número positivo.")
            else:
                altura2 = None
        except ValueError:
            errores.append("⚠️ La altura de la antena 2 debe ser un número válido (usar punto como separador decimal).")
            altura2 = None

        if errores:
            resultado = "<br>".join(errores)
        else:
            fresnel = 8.656 * ((distancia_f / frecuencia_f) ** 0.5)
            fresnel_truncado = int(fresnel * 100) / 100  # Truncar a 2 decimales
            fresnel_40 = int(fresnel * 0.4 * 100) / 100

            resultado = (
                f"🔍 El radio de la Zona de Fresnel es de: {fresnel_truncado:.2f} metros.<br>"
                f"✅ El 40% libre (recomendado) equivale a: {fresnel_40:.2f} metros."
            )

    return render_template(
        "index.html",
        resultado=resultado,
        distancia=distancia,
        frecuencia=frecuencia,
        fresnel=fresnel_truncado,
        altura1=altura1 if altura1 is not None else '',
        altura2=altura2 if altura2 is not None else ''
    )


if __name__ == "__main__":
    app.run(debug=True)
