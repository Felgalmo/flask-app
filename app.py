from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML para la página web
HTML_FORM = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de Chiller</title>
</head>
<body>
    <h1>Calculadora de Capacidad de Chiller</h1>
    <form method="POST">
        <label for="ce">Calor específico del agua (Ce) [kJ/(kg·°C)]:</label><br>
        <input type="number" step="0.01" id="ce" name="ce" required><br><br>
        
        <label for="q">Caudal de agua del chiller (Q) [m³/h]:</label><br>
        <input type="number" step="0.01" id="q" name="q" required><br><br>
        
        <label for="te">Temperatura de entrada del agua (Te) [°C]:</label><br>
        <input type="number" step="0.01" id="te" name="te" required><br><br>
        
        <label for="ts">Temperatura de salida del agua (Ts) [°C]:</label><br>
        <input type="number" step="0.01" id="ts" name="ts" required><br><br>
        
        <button type="submit">Calcular</button>
    </form>
    
    {% if resultado is not none %}
    <h2>Resultado:</h2>
    <p>La capacidad del chiller es: {{ resultado }} kW</p>
    {% endif %}
</body>
</html>
"""

# Función para calcular la capacidad del chiller
def calcular_capacidad_chiller(ce, q, te, ts):
    return 1000 * ce * q * (te - ts)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        # Obtener los valores del formulario
        ce = float(request.form["ce"])
        q = float(request.form["q"])
        te = float(request.form["te"])
        ts = float(request.form["ts"])
        
        # Calcular el resultado
        resultado = calcular_capacidad_chiller(ce, q, te, ts)
    
    # Renderizar la página HTML con el resultado
    return render_template_string(HTML_FORM, resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
