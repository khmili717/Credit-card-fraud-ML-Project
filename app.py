from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Charger le modèle sauvegardé avec joblib
model_path = os.path.join(os.getcwd(), 'models', 'model.pkl')
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupérer les 30 caractéristiques du formulaire
        features = [float(request.form[f'feature{i}']) for i in range(1, 31)]
        input_data = np.array([features])  # Convertir en tableau numpy

        # Prédiction
        prediction = model.predict(input_data)
        result = "Fraude détectée" if prediction[0] == 1 else "Transaction légitime"

        return render_template('result.html', prediction=result)
    except Exception as e:
        return f"Une erreur s'est produite : {e}"

if __name__ == '__main__':
    app.run(debug=True)

