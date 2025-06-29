from flask import Flask, render_template, request  # Importa Flask y funciones útiles para manejar plantillas y formularios

app = Flask(__name__)  # Crea una instancia de la app Flask

@app.route("/", methods=["GET", "POST"])  # Define la ruta principal ("/") y acepta métodos GET y POST
def index():
    # Inicializa variables vacías o por defecto para usarlas luego
    resultado = None
    distancia = ''
    frecuencia = ''
    fresnel_truncado = None
    altura1 = None
    altura2 = None

    if request.method == "POST":  # Si el formulario fue enviado (POST)
        # Recupera los valores enviados desde el formulario HTML
        distancia = request.form.get("distancia", '')
        frecuencia = request.form.get("frecuencia", '')
        altura1_raw = request.form.get("altura1", '')
        altura2_raw = request.form.get("altura2", '')

        errores = []  # Lista para guardar mensajes de error de validación

        # Validación de distancia
        try:
            distancia_f = float(distancia)
            if distancia_f <= 0:
                errores.append("⚠️ La distancia debe ser un número positivo.")
        except ValueError:
            errores.append("⚠️ La distancia debe ser un número válido (usar punto como separador decimal).")

        # Validación de frecuencia
        try:
            frecuencia_f = float(frecuencia)
            if frecuencia_f <= 0:
                errores.append("⚠️ La frecuencia debe ser un número positivo.")
        except ValueError:
            errores.append("⚠️ La  frecuencia debe ser un número válido (usar punto como separador decimal).")

        # Validación de altura1 (opcional)
        try:
            if altura1_raw.strip() != '':
                altura1 = float(altura1_raw)
                if altura1 <= 0:
                    errores.append("⚠️ La altura de la antena 1 debe ser un número positivo.")
            else:
                altura1 = None  # Campo vacío es permitido
        except ValueError:
            errores.append("⚠️ La altura de la antena 1 debe ser un número válido (usar punto como separador decimal).")
            altura1 = None

        # Validación de altura2 (opcional)
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

        # Si hubo errores, los mostramos; si no, calculamos Fresnel
        if errores:
            resultado = "<br>".join(errores)  # Une los errores en un solo string con saltos de línea
        else:
            # Fórmula para el primer radio de la zona de Fresnel
            fresnel = 8.656 * ((distancia_f / frecuencia_f) ** 0.5)
            fresnel_truncado = int(fresnel * 100) / 100  # Trunca a 2 decimales
            fresnel_40 = int(fresnel * 0.4 * 100) / 100  # Calcula el 40% libre recomendado

            # Prepara el mensaje de resultado final
            resultado = (
                f"🔍 El radio de la Zona de Fresnel es de: {fresnel_truncado:.2f} metros.<br>"
                f"✅ El 40% libre (recomendado) equivale a: {fresnel_40:.2f} metros."
            )

    # Renderiza la plantilla HTML 'index.html' y le pasa las variables necesarias
    return render_template(
        "index.html",
        resultado=resultado,
        distancia=distancia,
        frecuencia=frecuencia,
        fresnel=fresnel_truncado,
        altura1=altura1 if altura1 is not None else '',
        altura2=altura2 if altura2 is not None else ''
    )

# Ejecuta la app solo si este archivo es el principal
if __name__ == "__main__":
    app.run(debug=True)  # Activa el modo debug (útil durante desarrollo)
