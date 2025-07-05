import streamlit as st
from transformers import pipeline

# Cache and load FLAN-T5 model
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-small")

model = load_model()

# Generate Email Function
def generate_email(task):
    prompt = f"Write a professional, polite email for the task: {task}"
    result = model(prompt, max_new_tokens=256)[0]['generated_text']
    return result.strip()

# Streamlit UI
st.set_page_config(page_title="Smart Email Generator", page_icon="📨")
st.title("📨 Smart Email Generator (FLAN-T5)")
st.markdown("Enter your situation or task and generate a professional email.")

user_input = st.text_area("📝 Enter your task (e.g., 'I'm sick', 'Need leave'):")

if st.button("Generate Email"):
    if not user_input.strip():
        st.warning("Please enter something.")
    else:
        with st.spinner("Generating..."):
            email = generate_email(user_input)
        st.markdown("### 📬 Generated Email:")
        st.success(email)
