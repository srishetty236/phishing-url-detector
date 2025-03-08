from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("malicious_url_model.pkl", "rb"))

@app.route("/")
def home():
    return "🚀 Malicious URL Detection API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()  # Get JSON input
    df = pd.DataFrame([data])  # Convert JSON to DataFrame

    prediction = model.predict(df)[0]  # Make prediction
    result = "Malicious" if prediction == 1 else "Benign"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
