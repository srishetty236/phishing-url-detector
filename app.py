import pickle
import zlib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Load model
with open("malicious_url_model_compressed.pkl", "rb") as file:
    model = pickle.loads(zlib.decompress(file.read()))

class FeaturesInput(BaseModel):
    features: str  # Example: "3,0,0,1,0,0,0,0,0,0,1,2,0,892,0,0,0,0,0,0"

@app.post("/predict")
def predict_url(data: FeaturesInput):
    features = np.array([list(map(float, data.features.split(",")))])
    prediction = model.predict(features)
    return {"result": "Malicious URL" if prediction[0] == 1 else "Benign URL"}
