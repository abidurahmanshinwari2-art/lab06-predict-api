import random

from flask import Flask, jsonify, request

# The response shows the registration number. The grader seeds with the
# numeric roll number only.
REGISTRATION_NUMBER = "SP22-BCS-108"
ROLL_NUMBER = 108

random.seed(ROLL_NUMBER)
a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)

app = Flask(__name__)


@app.get("/predict")
def predict():
    x1 = float(request.args["x1"])
    x2 = float(request.args["x2"])
    x3 = float(request.args["x3"])
    prediction = a1 * x1 + a2 * x2 + a3 * x3 + b
    return jsonify(
        {
            "registration number": REGISTRATION_NUMBER,
            "prediction": round(prediction, 2),
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
