# 📧 Spam, Ham & Phishing Email Classifier using Machine Learning (Flask + Gmail API)

A web-based email classification tool that identifies **Spam**, **Ham (Genuine)**, and **Phishing** emails using a Machine Learning model. It also offers real-time **Gmail inbox integration** and **explainable AI** through **LIME** to visualize why a particular prediction was made.

---

## 🚀 Features

- ✅ **Classifies emails** into: Spam / Ham / Phishing  
- 📬 **Gmail API Integration**: Fetch and classify your real inbox emails  
- 🧠 **Explainability with LIME**: Understand why a prediction was made  
- 🖼️ **HTML Email Parsing**: Cleanly extracts content from formatted emails using BeautifulSoup  

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)  
- **Frontend**: AngularJS, HTML, CSS  
- **Machine Learning**: scikit-learn (Logistic Regression Model)  
- **Explainability**: LIME  
- **Email Parsing**: BeautifulSoup  
- **Gmail Integration**: Gmail API (OAuth2)

---

## 🔐 Gmail API Setup

To enable Gmail access via the API:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or use an existing one)
3. Enable the **Gmail API**
4. Create **OAuth 2.0 Credentials**
5. Download the `credentials.json` file
6. Place `credentials.json` in the project root directory
7. On the first run, a browser will open asking for Gmail access

> ⚠️ Ensure that `redirect_uri` in your Google Cloud Console matches the local Flask redirect (usually `http://localhost:5000/` or as per your app setup).

---

## 📦 Installation & Running the App

### 🔧 Prerequisites

- Python 3.7+
- pip (Python package manager)

### 🚀 Steps to Run

```bash
# 1. Clone the repository
git clone https://github.com/yamini749/spam-email-phishing-detector.git
cd spam-email-phishing-detector

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Flask app
python app.py
```

> The app will be live at: [http://localhost:3000](http://localhost:3000)

---

## 📁 Project Structure

```
spam-email-phishing-detector/
├── static/               # Frontend assets (HTML, CSS, JS)
├── templates/            # Jinja2 templates
├── credentials.json      # Gmail API credentials (secure this file)
├── app.py                # Main Flask application
├── model.pkl             # Trained ML model
├── vectorizer.pkl        # Fitted TF-IDF vectorizer
├── lime_explainer.pkl    # (Optional) Pickled LIME explainer
└── requirements.txt      # Python dependencies
```

---

## 🧠 Model Training (Optional)

If you want to retrain or improve the model:

- Update or extend your dataset
- Use `scikit-learn` to retrain the logistic regression model
- Save the new model as `model.pkl`
- Update `vectorizer.pkl` if using a new TF-IDF configuration

---

## 🙋‍♀️ Author

**Yamini Settipalli**

- GitHub: [@yamini749](https://github.com/yamini749)
  
---

⭐ If you found this useful, please consider giving a star to the repository!
