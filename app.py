from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
app.debug = True

# Load the trained machine learning model
loaded_model = joblib.load("credit_card_fraud_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_values = request.get_json()

        # Create a DataFrame with the input data
        input_data = pd.DataFrame(input_values, index=[0])

        # Make predictions using the loaded model
        predictions = loaded_model.predict(input_data)

        result = 'Fraudulent' if predictions[0] == 1 else 'Non-Fraudulent'

        return jsonify(result)

    except Exception as e:
        return jsonify(str(e))

if __name__ == '__main__':
    app.run()
