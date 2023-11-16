from flask import Flask, render_template, request, jsonify
from flasgger import Swagger
import pandas as pd
import pickle

app = Flask(__name__)
app.debug = True

# Initialize Swagger
Swagger(app)

# Load the trained machine learning model
with open("credit_card_fraud_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint to predict whether a credit card transaction is fraudulent or non-fraudulent.
    ---
    parameters:
      - name: input_values
        in: body
        required: true
        schema:
          type: object
          properties:
            V1:
              type: number
            V2:
              type: number
            V3:
              type: number
            V4:
              type: number
            V5:
              type: number
            V6:
              type: number
            V7:
              type: number
            V8:
              type: number
            V9:
              type: number
            V10:
              type: number
            V11:
              type: number
            V12:
              type: number
            V13:
              type: number
            V14:
              type: number
            V15:
              type: number
            V16:
              type: number
            V17:
              type: number
            V18:
              type: number
            V19:
              type: number
            V20:
              type: number
            V21:
              type: number
            V22:
              type: number
            V23:
              type: number
            V24:
              type: number
            V25:
              type: number
            V26:
              type: number
            V27:
              type: number
            V28:
              type: number
            Amount:
              type: number
    responses:
      200:
        description: A string indicating whether the transaction is Fraudulent or Non-Fraudulent.
        schema:
          type: string
    """
    try:
        input_values = request.get_json()

        # Create a DataFrame with the input data
        input_data = pd.DataFrame(input_values, index=[0])

        # Make predictions using the loaded model
        predictions = loaded_model.predict(input_data)

        result = 'Fraudulent' if predictions[0] == 1 else 'Non-Fraudulent'

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=5000)
