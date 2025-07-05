import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model safely once
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
    model = AutoModelForCausalLM.from_pretrained("distilgpt2")
    model.eval()
    return tokenizer, model

tokenizer, model = load_model()

# Generate polite email
def generate_email(task, max_length=100):
    prompt = (
        f"Write a polite professional email for the following task:\n"
        f"{task.strip()}\n\nEmail:\n"
    )
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

    result = tokenizer.decode(output[0], skip_special_tokens=True)
    final = result.replace(prompt, "").strip()
    return final if final else "Sorry, couldn't generate a useful email."

# Streamlit UI
st.set_page_config(page_title="Smart Email Generator", layout="centered")
st.title("📨 Smart Email Generator (Polite & Professional)")
st.markdown("Enter your task to generate a professional email instantly.")

user_input = st.text_area("📝 Enter your task or message:")

if st.button("Generate Email"):
    if not user_input.strip():
        st.warning("Please enter something.")
    else:
        with st.spinner("Generating email..."):
            response = generate_email(user_input)
        st.success("📬 Generated Email:")
        st.write(response)
