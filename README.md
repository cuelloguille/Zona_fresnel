📡 Calculadora de la Zona de Fresnel
Esta aplicación web permite calcular y visualizar la Zona de Fresnel entre dos antenas. Se puede usar para fines educativos, técnicos o de verificación de enlaces inalámbricos.

✅ Requisitos previos
Tener instalado Python 3

Tener instalado Git (opcional pero recomendado)

Tener instalado pip para instalar dependencias

⚙️ Pasos para ejecutar la aplicación
Clonar el repositorio desde la terminal:

git clone https://github.com/usuario/nombre-repo.git
cd nombre-repo

Instalar las dependencias:

pip install -r requirements.txt


Ejecutar la aplicación Flask:

python app.py


Una vez iniciada, Flask mostrará un enlace como este:

Running on http://127.0.0.1:5000

Copialo y abrilo en tu navegador para usar la calculadora.

🧠 ¿Cómo funciona?
Esta calculadora fue desarrollada usando Flask (Python) para el backend y Chart.js (JavaScript) para los gráficos.

🛠️ En el backend (app.py)
Recibe los datos mediante el método POST (formulario).

Valida que los datos ingresados (distancia, frecuencia y alturas) sean numéricos y positivos.

Calcula el radio de la Primera Zona de Fresnel usando la fórmula Pasada


 
​
 
Donde:

r = radio en metros

d = distancia en km

f = frecuencia en GHz

📈 En el frontend (index.html)
🛰️ ¿Qué permite esta app?
👁️ Visualizar gráficamente cómo se comporta la Zona de Fresnel en función de los datos ingresados.

📝 Personalizar la entrada con:

Distancia entre antenas (km)

Frecuencia de la señal (GHz)

Altura de ambas antenas (m) (opcional)

⚡ Obtener resultados inmediatos, tanto en formato numérico como gráfico.

🚫 Verificar interferencias: muestra el 40% mínimo libre recomendado de la zona de Fresnel para asegurar que no existan obstáculos que degraden la señal.

👨‍💻 Autor :
Desarrollado por Guillermo Cuello

