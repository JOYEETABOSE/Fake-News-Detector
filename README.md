# 📰 Fake News Detector using ML & Gemini API

A powerful and explainable fake news detection app built using **Machine Learning**, **Streamlit**, and **Google Gemini API**. It not only classifies articles as real or fake, but also uses Gemini to explain *why* the news might be manipulative or misleading.

---

## 🚀 Features

- ✅ Detects fake vs real news using a trained ML model
- 🤖 Generates detailed explanations using **Gemini 1.5 Flash**
- 🧠 Uses NLP techniques like TF-IDF + Logistic Regression
- 🎨 Simple and clean UI with **Streamlit**
- 🔐 Environment variables secured using `.env`

---

## 🖼️ Screenshot

![Fake News Detector UI](your-screenshot.png)

---

## 🛠️ Technologies Used

| Technology     | Purpose                               |
|----------------|----------------------------------------|
| Python         | Backend logic                          |
| Streamlit      | Frontend web UI                        |
| scikit-learn   | ML model and vectorizer                |
| Google Gemini  | AI explanation via Generative AI API   |
| dotenv         | Environment variable management        |

---

## 📁 Project Structure

📦 fake-news-detector/
├── app.py # Streamlit UI + logic
├── fake_news_model.pkl # Trained ML model
├── tfidf_vectorizer.pkl # Text vectorizer
├── fake_news.ipynb # Model training notebook
├── requirements.txt # Dependencies
├── .env # Your API key (not uploaded)
├── .gitignore # Files to ignore in Git
└── README.md # This file

y
---

## 🧪 How to Run This Locally

###
1. 📦 Clone the Repository
------------------------------
git clone https://github.com/yourusername/fake-news-detector.git
cd fake-news-detector

2. 🐍 Create Virtual Environment
-----------------------------------
python -m venv venv
venv\Scripts\activate   # for Windows

3. 📄 Add .env File
--------------------------
Create a .env file and add your Gemini API key:
GEMINI_API_KEY= "yourApikeyhere"

4. 📥 Install Dependencies
---------------------------------
pip install -r requirements.txt

5. 🚀 Run the App
--------------------------
streamlit run app.py

🧠 How it Works
The user pastes a news article

A trained ML model (Logistic Regression) predicts if it’s fake or real

Google Gemini API provides natural language explanation with reasoning

All results shown in a clear, simple web app

📌 Notes
.env is not pushed to GitHub (for security)

You can switch to gemini-1.5-pro or text-bison-001 depending on your key access and quota

The model was trained on the Kaggle Fake News Dataset

💡 Future Improvements
Upload news via URL or headline

Use LLMs like Gemini for final verdict instead of just explanation

Add database logging with Supabase

🙋‍♀️ Author
Built by Joyeeta Bose — powered by curiosity and chai ☕.



 

