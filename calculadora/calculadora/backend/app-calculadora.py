from flask import Flask, jsonify
from flask_cors import CORS
import math as mt

app = Flask(__name__)
CORS(app)

# Suma
@app.route("/suma/<float:numero1>/<float:numero2>")
@app.route("/suma/<int:numero1>/<int:numero2>")
@app.route("/suma/<int:numero1>/<float:numero2>")
@app.route("/suma/<float:numero1>/<int:numero2>")
def suma(numero1=0, numero2=0):
    Resultado = numero1 + numero2
    data = {
        "Resultado": Resultado,
        "Operación": "Suma",
    }
    return jsonify(data)

# Resta
@app.route("/resta/<float:numero1>/<float:numero2>")
@app.route("/resta/<int:numero1>/<int:numero2>")
@app.route("/resta/<int:numero1>/<float:numero2>")
@app.route("/resta/<float:numero1>/<int:numero2>")
def Resta(numero1=0, numero2=0):
    Resultado = numero1 - numero2
    data = {
        "Resultado": Resultado,
        "Operación": "Resta",
    }
    return jsonify(data)

# Multiplicación
@app.route("/multiplicacion/<float:numero1>/<float:numero2>")
@app.route("/multiplicacion/<int:numero1>/<int:numero2>")
@app.route("/multiplicacion/<int:numero1>/<float:numero2>")
@app.route("/multiplicacion/<float:numero1>/<int:numero2>")
def Multiplicacion(numero1=0, numero2=0):
    Resultado = numero1 * numero2
    data = {
        "Resultado": Resultado,
        "Operación": "Multiplicación",
    }
    return jsonify(data)

# División
@app.route("/division/<float:numero1>/<float:numero2>")
@app.route("/division/<int:numero1>/<int:numero2>")
@app.route("/division/<int:numero1>/<float:numero2>")
@app.route("/division/<float:numero1>/<int:numero2>")
def Division(numero1=0, numero2=0):
    if numero2 == 0:
        return jsonify({"Error": "No se puede dividir entre cero", "Operación": "División"})
    Resultado = numero1 / numero2
    data = {
        "Resultado": Resultado,
        "Operación": "División",
    }
    return jsonify(data)

# Potenciación
@app.route("/potenciacion/<float:numero1>/<float:numero2>")
@app.route("/potenciacion/<int:numero1>/<int:numero2>")
@app.route("/potenciacion/<int:numero1>/<float:numero2>")
@app.route("/potenciacion/<float:numero1>/<int:numero2>")
def Potenciacion(numero1=0, numero2=0):
    Resultado = numero1 ** numero2
    data = {
        "Resultado": Resultado,
        "Operación": "Potenciación",
    }
    return jsonify(data)

# Seno
@app.route("/seno/<float:numero1>")
@app.route("/seno/<int:numero1>")
def Seno(numero1=0):
    Resultado = mt.sin(numero1)
    data = {
        "Resultado": Resultado,
        "Operación": "Seno",
    }
    return jsonify(data)

# Coseno
@app.route("/coseno/<float:numero1>")
@app.route("/coseno/<int:numero1>")
def Coseno(numero1=0):
    Resultado = mt.cos(numero1)
    data = {
        "Resultado": Resultado,
        "Operación": "Coseno",
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
