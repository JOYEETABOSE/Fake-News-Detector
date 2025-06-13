import streamlit as st
import joblib
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# # 🔍 Check available models
# st.subheader("🧪 Available Gemini Models")
# models = genai.list_models()
# for m in models:
#     st.write(m.name)

# Load model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

def predict_news(text):
    cleaned = text.lower()
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)
    return "🟢 Real News" if prediction[0] == 1 else "🔴 Fake News"

def analyze_with_gemini(text):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(
            f"Is this news article fake or manipulative?\n\n{text[:1000]}"
        )
        return response.text
    except Exception as e:
        return f"⚠️ Gemini API quota exceeded or another error occurred:\n{e}"



# Streamlit UI
st.title("📰 Fake News Detector with Gemini AI")
input_text = st.text_area("Paste a news article here:")

if st.button("Analyze"):
    st.subheader("🤖 ML Model Prediction")
    st.success(predict_news(input_text))

    st.subheader("🧠 Gemini's Explanation")
    with st.spinner("Gemini is analyzing..."):
        explanation = analyze_with_gemini(input_text)
    st.write(explanation)
