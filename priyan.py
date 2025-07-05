import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Cache model loading
@st.cache_resource
def load_gpt2():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    model.eval()
    return tokenizer, model

def generate_email(prompt: str, tokenizer, model, max_length=100):
    # Build a prefix so GPT‑2 knows what to do
    inp = f"Write a professional email for: {prompt}"
    input_ids = tokenizer.encode(inp, return_tensors="pt")
    output_ids = model.generate(
        input_ids,
        max_length=max_length,
        num_beams=5,
        no_repeat_ngram_size=2,
        early_stopping=True
    )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

# Streamlit UI
st.set_page_config(page_title="Smart Email Generator", page_icon="📧")
st.title("📧 Smart Email Generator (GPT‑2 Only)")

user_input = st.text_area("Enter any task or note:")

if st.button("Generate Email"):
    if not user_input.strip():
        st.warning("Please enter a prompt.")
    else:
        tokenizer, model = load_gpt2()
        email = generate_email(user_input, tokenizer, model)
        st.subheader("🔹 Generated Email:")
        st.write(email)
