from flask import Flask, render_template, request
import numpy as np
import torch
import joblib

from model_loader import model

app = Flask(__name__)
scaler = joblib.load("scaler.pkl")

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        age = float(request.form["age"])

        gender = int(
            request.form["gender"]
        )

        height = float(
            request.form["height"]
        )

        weight = float(
            request.form["weight"]
        )

        height_m = height / 100

        bmi = weight / (height_m ** 2)

        activity = request.form["activity"]
        diet = request.form["diet"]

        activity_features = [
            1 if activity == "lightly_active" else 0,
            1 if activity == "moderately_active" else 0,
            1 if activity == "sedentary" else 0,
            1 if activity == "very_active" else 0
        ]

        diet_features = [
            1 if diet == "high_protein" else 0,
            1 if diet == "keto" else 0,
            1 if diet == "mediterranean" else 0,
            1 if diet == "vegan" else 0,
            1 if diet == "vegetarian" else 0
        ]

        features = np.array([

            age,
            gender,
            height,
            weight,
            bmi,

            *activity_features,
            *diet_features
        ], dtype=np.float32)

        #Scale features
        features_scaled = scaler.transform(
            [features]
        )

        tensor = torch.tensor(
            features_scaled,
            dtype=torch.float32
        )

        with torch.no_grad():
            prediction = model(tensor).item()

    return render_template(
        "index.html",
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(debug=True)