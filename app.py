from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define endpoint to accept input data and return prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input data from request
        input_data = request.json
        
        # Preprocess input data (if needed)
        input_df = pd.DataFrame(input_data, index=[0])  
        
        # Make prediction
        prediction = model.predict(input_df)
        
        # Return prediction as JSON response
        return jsonify({'prediction': prediction.tolist()})
    else:
        return jsonify({'error': 'Only POST requests are allowed.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
