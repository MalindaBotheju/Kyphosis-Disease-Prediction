from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the model and scaler
model = joblib.load('kyphosis_svm_model.pkl')
scaler = joblib.load('kyphosis_scaler.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    form_data = {} # Dictionary to store inputs to send back to the UI
    
    if request.method == 'POST':
        # 1. Get the data
        age = request.form.get('age')
        number = request.form.get('number')
        start = request.form.get('start')
        
        # Store them to send back to the form
        form_data = {'age': age, 'number': number, 'start': start}
        
        # 2. Format and scale
        features = np.array([[float(age), float(number), float(start)]])
        scaled_features = scaler.transform(features)
        
        # 3. Make the prediction
        pred = model.predict(scaled_features)[0]
        prediction = "present" if pred == 1 else "absent"
        
    return render_template('index.html', prediction=prediction, form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)