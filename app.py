from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load("modelspam.joblib")
vectorizer = joblib.load("tfidfvectorizer.joblib")  
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        email_text = request.form['email_text']
        
        # Transform the email text using the loaded TfidfVectorizer
        data = vectorizer.transform([email_text]).toarray()
        
        prediction = model.predict(data)
        
        result = 'Spam' if prediction[0] == 1 else 'Not Spam'
        
        return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
