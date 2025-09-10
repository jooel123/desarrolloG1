from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Cargar tu CSV al iniciar la app
df = pd.read_csv("Customer_DF.csv")

@app.route("/")
def home():
    return "🚀 API BI – Customer_DF funcionando en Heroku"

@app.route("/preview")
def preview():
    # Devuelve las primeras 5 filas del dataset en formato JSON
    return jsonify(df.head(5).to_dict(orient="records"))

@app.route("/info")
def info():
    # Devuelve información básica del dataset
    info = {
        "filas": df.shape[0],
        "columnas": df.shape[1],
        "columnas_nombres": list(df.columns)
    }
    return jsonify(info)

if __name__ == "__main__":
    app.run(debug=True)
