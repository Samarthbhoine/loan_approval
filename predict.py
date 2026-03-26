# src/predict.py

import pickle
from src.preprocess import preprocess_input

# Load files
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

def predict(data):
    df = preprocess_input(data)

    # Ensure same column order
    df = df.reindex(columns=columns, fill_value=0)

    # Scale
    df_scaled = scaler.transform(df)

    # Predict
    prediction = model.predict(df_scaled)[0]

    return "Approved ✅" if prediction == 1 else "Rejected ❌"