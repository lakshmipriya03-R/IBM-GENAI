import streamlit as st
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
    pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
    return pipe

pipe = load_model()

def generate_email(task):
    prompt = f"Write a polite, professional email for the following task: {task}"
    response = pipe(prompt, max_new_tokens=200)[0]['generated_text']
    return response.strip()

# Streamlit UI
st.set_page_config(page_title="Smart Email Generator", layout="centered")
st.title("📨 Smart Email Generator (FLAN-T5 Small)")
st.markdown("Enter your task, situation, or bullet point and get a professional email.")

task = st.text_area("📝 Enter your task:")

if st.button("Generate Email"):
    if not task.strip():
        st.warning("Please enter a task.")
    else:
        with st.spinner("Generating email..."):
            email = generate_email(task)
        st.markdown("### 📬 Generated Email:")
        st.success(email)
