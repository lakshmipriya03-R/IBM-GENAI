import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Load the FLAN-T5 model and tokenizer
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
    gen = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
    return gen

generator = load_model()

# Generate email based on task
def generate_email(task):
    prompt = f"Write a polite and professional email for the task: {task}"
    response = generator(prompt, max_length=128, clean_up_tokenization_spaces=True)[0]["generated_text"]
    return response.strip()

# Streamlit UI
st.set_page_config(page_title="Smart Email Generator", layout="centered")
st.title("📨 Smart Email Generator (FLAN-T5)")
st.markdown("Enter a task or situation and get a clean, professional email.")

user_input = st.text_area("📝 Task / Situation (e.g., 'I'm sick', 'Project deadline'):")

if st.button("Generate Email"):
    if not user_input.strip():
        st.warning("Please enter a task or bullet point.")
    else:
        with st.spinner("Generating your email..."):
            email = generate_email(user_input)
        st.markdown("### 📬 Generated Email:")
        st.success(email)
