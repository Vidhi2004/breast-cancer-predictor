from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model/breast_cancer_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get feature values from form
        input_values = [float(request.form[f'feature{i}']) for i in range(1, 11)]

        # Predict using the model
        prediction = model.predict([input_values])[0]
        result = 'Malignant' if prediction == 0 else 'Benign'

        # Send prediction to result.html
        return render_template('result.html', prediction=result)

    except Exception as e:
        return render_template('index.html', prediction=f"Error: Invalid input.\n{e}")

if __name__ == '__main__':
    app.run(debug=True)
