# ✉️ Spam Mail Detection

A simple machine learning web app that classifies emails as **Spam** or **Not Spam (Ham)** using **Logistic Regression**.

🔗 **Live Website**: [https://spam-mail-detection-y59j.onrender.com/](https://spam-mail-detection-y59j.onrender.com/)

---

## 🚀 Features

- Paste any email content and classify instantly
- Outputs clear prediction: `Spam` or `Not Spam`
- Simple, fast, and beginner-friendly Flask interface
- Fully deployed and accessible via the Render web link

---

## 🛠️ Tech Stack

- Python 3
- Flask (for web app)
- Scikit-learn (Logistic Regression model)
- Pandas & NumPy
- Joblib (for saving/loading model)

---

## 📂 Project Structure

```
📦 Spam-Mail-Detection/
├── app.py                  # Flask application
├── modelspam.joblib        # Trained spam detection model
├── templates/
│   └── index.html          # Frontend HTML template
├── static/                 # Optional: CSS or JS files
├── requirements.txt        # Project dependencies
└── README.md               # You're reading it now
```

---

## 📊 Model Details

- **Model**: Logistic Regression from Scikit-learn
- **Preprocessing**: Cleaned text + TF-IDF vectorization
- **Training Data**: Dataset of labeled emails (spam / ham)
- Model is saved using `joblib` and loaded in `app.py` during runtime

---

## ▶️ Getting Started Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yamini749/Spam-Mail-Detection.git
   cd Spam-Mail-Detection
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app**
   ```bash
   python app.py
   ```

4. **Visit in browser**
   ```
   http://127.0.0.1:5000/
   ```

---

## 🌐 Live Deployment

This project is hosted on **Render**:

🔗 [https://spam-mail-detection-y59j.onrender.com/](https://spam-mail-detection-y59j.onrender.com/)

---


## 🙋‍♀️ Author

**Yamini Settipalli**  
💼 GitHub: [@yamini749](https://github.com/yamini749)
