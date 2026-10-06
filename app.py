from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to ML Prediction API - Service Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    return jsonify({"prediction": sum(data["features"])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
