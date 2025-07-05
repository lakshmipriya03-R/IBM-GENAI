import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Sample training data
data = {
    "bullet_points": [
        "project deadline extended to next friday",
        "team meeting scheduled tomorrow at 10am",
        "client requested changes to proposal",
        "please submit timesheets by monday",
        "monthly sales report needs review"
    ],
    "email_output": [
        "The project deadline has been extended to next Friday. Please adjust your schedules accordingly.",
        "A team meeting is scheduled for tomorrow at 10 AM. Kindly be on time.",
        "The client has requested changes to the proposal. Please review and update accordingly.",
        "Please make sure to submit your timesheets by Monday to ensure timely processing.",
        "The monthly sales report is ready and needs your review. Kindly take a look."
    ]
}

# Train classic ML model
@st.cache_resource
def load_model():
    df = pd.DataFrame(data)
    vectorizer = TfidfVectorizer()
    classifier = LogisticRegression()
    X = vectorizer.fit_transform(df['bullet_points'])
    y = df['email_output']
    classifier.fit(X, y)
    return vectorizer, classifier

# App UI
st.title("📧 Smart Email Generator (Classic ML Only)")

user_input = st.text_area("Enter a task or bullet point:")

if st.button("Generate Email"):
    if user_input.strip() == "":
        st.warning("Please enter something.")
    else:
        vectorizer, classifier = load_model()
        X_input = vectorizer.transform([user_input])
        result = classifier.predict(X_input)[0]
        st.subheader("📬 Generated Email:")
        st.write(result)
