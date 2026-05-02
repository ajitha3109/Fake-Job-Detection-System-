import streamlit as st
import joblib
import re

# Page config
st.set_page_config(page_title="Fake Job Detection", page_icon="🕵️")

# Title
st.title("🕵️ Fake Job Detection System")
st.write("Detect whether a job posting is **Real or Fake** using AI.")

# Load model & vectorizer
model = joblib.load("fake_job_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Clean function
def clean(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    return text

# Input
job_desc = st.text_area(
    "📄 Enter Job Description",
    height=200,
    placeholder="Paste job description here..."
)

# Button
if st.button("🔍 Check Job"):

    if job_desc.strip() == "":
        st.warning("⚠️ Please enter a job description")

    else:
        with st.spinner("Analyzing job posting..."):

            cleaned = clean(job_desc)
            vec = vectorizer.transform([cleaned])

            prediction = model.predict(vec)
            prob = model.predict_proba(vec)

        confidence = round(max(prob[0]) * 100, 2)
        fake_prob = round(prob[0][1] * 100, 2)
        real_prob = round(prob[0][0] * 100, 2)

        st.subheader("📊 Result")

        # Prediction result
        if prediction[0] == 1:
            st.error("⚠️ Fake Job Detected!")

            # Risk level
            if confidence > 85:
                st.write("Risk Level: 🔴 High")
            else:
                st.write("Risk Level: 🟠 Medium")

        else:
            st.success("✅ Real Job")

            # Risk level
            if confidence > 75:
                st.write("Risk Level: 🟢 Low")
            else:
                st.write("Risk Level: 🟡 Uncertain")

        # Confidence
        st.info(f"Confidence Score: {confidence}%")

        # Probabilities
        st.write(f"🔴 Fake Probability: {fake_prob}%")
        st.write(f"🟢 Real Probability: {real_prob}%")

        # 🔍 Key Indicators (IMPORTANT FEATURE)
        st.subheader("🔎 Key Indicators")

        feature_names = vectorizer.get_feature_names_out()
        weights = model.coef_[0]

        vec_array = vec.toarray()[0]
        top_indices = vec_array.argsort()[-5:][::-1]

        for idx in top_indices:
            if vec_array[idx] > 0:
                st.write(f"- {feature_names[idx]}")

        # Footer
        st.markdown("---")
        st.caption("Built using Machine Learning & NLP | Project by Kalai Ajitha M")