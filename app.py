
from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load the trained ML model
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "saved_model",
    "sentiment_model.pkl"
)

model = joblib.load(MODEL_PATH)


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    review = ""
    confidence = None

    if request.method == "POST":
        review = request.form.get("review", "").strip()

        if review:
            # Predict sentiment
            result = model.predict([review])[0]
            prediction = "Positive" if int(result) == 1 else "Negative"

            # Get prediction confidence if supported
            if hasattr(model, "predict_proba"):
                probabilities = model.predict_proba([review])[0]
                confidence = round(float(max(probabilities)) * 100, 2)

    return render_template(
        "index.html",
        prediction=prediction,
        review=review,
        confidence=confidence
    )


if __name__ == "__main__":
    app.run(debug=True)
