import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load model and tokenizer
@st.cache_resource
def load_model():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    model.eval()
    return tokenizer, model

tokenizer, model = load_model()

# Function to generate a polite email
def generate_email(task, max_length=100):
    prompt = f"Write a professional and polite email based on the following task:\n{task.strip()}\n\nEmail:\n"
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=max_length,
            num_beams=5,
            no_repeat_ngram_size=2,
            early_stopping=True,
            pad_token_id=tokenizer.eos_token_id
        )

    decoded = tokenizer.decode(output[0], skip_special_tokens=True)
    final_email = decoded.replace(prompt, "").strip()
    return final_email if final_email else "Sorry, no useful email was generated."

# Streamlit App Interface
st.set_page_config(page_title="Smart Email Generator", page_icon="📨", layout="centered")
st.title("📨 Smart Email Generator")
st.markdown("Write your task or bullet point, and get a professional email.")

task_input = st.text_area("📝 Enter your task here:")

if st.button("Generate Email"):
    if not task_input.strip():
        st.warning("Please enter a valid input.")
    else:
        with st.spinner("Generating email..."):
            email = generate_email(task_input)
        st.markdown("### 📬 Generated Email:")
        st.success(email)
