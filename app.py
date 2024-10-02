from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load("modelspam.joblib")
vectorizer = joblib.load("tfidfvectorizer.joblib")

@app.route('/')
def index():
    return render_template('index.html', prediction=None)  # Initialize prediction as None

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form['email_text']
    data = vectorizer.transform([email_text]).toarray()
    
    # Get prediction probability
    prediction_proba = model.predict_proba(data)
    
    # Use adjusted threshold
    adjusted_threshold = 0.4  # Set your new threshold here
    prediction = (prediction_proba[0][1] >= adjusted_threshold).astype(int)
    
    # Determine the result
    result = 'Spam' if prediction == 0 else 'Ham'
    
    # Render the index template with the prediction result
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(port=3000,debug=True)
