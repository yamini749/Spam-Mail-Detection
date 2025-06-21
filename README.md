# 📧 Spam, Ham & Phishing Email Classifier using Machine Learning (Flask + Gmail API)

This is a web-based email classifier that detects **Spam**, **Ham (Genuine)**, and **Phishing** emails using **Machine Learning**, **LIME explainability**, and optionally integrates **Gmail API** to classify real inbox emails.

## 🚀 Features

- 📤 **Text-based Classification** (Spam / Ham / Phishing)
- 🧠 **Explainability** using LIME (see why the model predicts so)
- 📬 **Real Email Fetch** via Gmail API (OAuth2-based)
- 📄 **HTML Email Support** (parsed using BeautifulSoup)
- 💡 **UI Enhancements** with collapsible prediction details and better layout

## 🛠 Tech Stack

- **Flask** – Backend web framework
- **Scikit-learn** – ML model training (Logistic Regression)
- **LIME** – Model explainability
- **BeautifulSoup** – HTML email parsing
- **Gmail API** – To fetch real user emails
- **AngularJS + HTML/CSS** – Frontend

## 📂 Project Structure

.
├── app.py # Main Flask app
├── gmail_fetcher.py # Gmail API integration
├── model_training.ipynb # Model training script (Spam + Phishing)
├── modelspam.joblib # Trained ML model
├── tfidfvectorizer.joblib # TF-IDF Vectorizer
├── templates/
│ └── index.html # Main web page (UI)
├── static/
│ └── style.css # Custom styling
├── credentials.json # Gmail API credentials
└── token.json # OAuth2 token


## 🔐 Gmail API Setup

1. Create a project in [Google Cloud Console](https://console.cloud.google.com/)
2. Enable **Gmail API**
3. Download `credentials.json` and place it in the project root
4. On first run, you will be prompted to log in and authorize the app

## 💻 How to Run

```bash
# Install requirements
pip install -r requirements.txt

# Run the app
python app.py

Then open http://localhost:3000 in your browser.


