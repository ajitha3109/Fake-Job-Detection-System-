# 🕵️ Fake Job Detection System

An AI-powered web application that detects whether a job posting is **Real or Fake** using Natural Language Processing (NLP) and Machine Learning.

---

## 🚀 Features

- 📄 Analyze job descriptions
- ⚠️ Detect fake job postings
- 📊 Confidence score display
- 🔴 Risk level (High / Medium / Low)
- 🔎 Key indicators (important words influencing prediction)
- 🧠 Built using Machine Learning & NLP
- 🌐 Interactive UI using Streamlit

---

## 🧠 How It Works

1. User enters a job description
2. Text is cleaned and preprocessed
3. Converted into numerical features using TF-IDF
4. Logistic Regression model predicts:
   - Fake Job ❌
   - Real Job ✅
5. Displays:
   - Prediction
   - Confidence score
   - Risk level
   - Key indicators

---

## 🛠️ Tech Stack

- Python 🐍
- Pandas
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Logistic Regression
- Streamlit (for UI)

---

## 📊 Model Details

- Algorithm: Logistic Regression
- Feature Extraction: TF-IDF (5000 features)
- Handling Imbalance: Class Weight Balancing
- Evaluation Metrics:
  - Accuracy: ~95%
  - High Recall for Fake Jobs (important for fraud detection)

---

## 📂 Project Structure
Fake-Job-Detection/
│
├── app.py
├── fake_job_model.pkl
├── vectorizer.pkl
├── README.md


---

## ▶️ How to Run the Project

1. Clone the repository
git clone https://github.com/your-username/Fake-Job-Detection.git
cd Fake-Job-Detection


2. Install dependencies
pip install streamlit scikit-learn pandas joblib


3. Run the app
streamlit run app.py


---

## 💡 Example

### ❌ Fake Job Input:

Earn money fast! Work from home! No experience needed!

👉 Output:
- ⚠️ Fake Job Detected
- 🔴 High Risk
- High confidence

---

### ✅ Real Job Input:

We are hiring a Data Analyst with experience in Python, SQL, and data visualization.

👉 Output:
- ✅ Real Job
- 🟡 Medium/Uncertain Risk
- Moderate confidence

---

## 🎯 Key Highlights

- Focused on **recall** to avoid missing fake jobs
- Provides **explainability** using key indicators
- Real-world applicable AI system
- Beginner-friendly UI with strong backend logic

---

## 👩‍💻 Author
**Kalai Ajitha M**  
AI & Data Science Student  

---
## ⭐ Future Improvements

- Add company, salary, and location features
- Deploy the app online
- Use advanced NLP models (BERT)
- Improve accuracy using deep learning

---
## 📌 Conclusion
This project demonstrates how Machine Learning and NLP can be used to solve real-world problems like detecting fraudulent job postings and protecting users from scams.
