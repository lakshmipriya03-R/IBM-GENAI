import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load GPT-2 model and tokenizer once
@st.cache_resource
def load_model():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    model.eval()
    return tokenizer, model

tokenizer, model = load_model()

# 🔥 Email Generation Logic
def generate_email(prompt, max_length=100):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            num_beams=5,
            early_stopping=True,
            pad_token_id=tokenizer.eos_token_id
        )

    decoded = tokenizer.decode(output[0], skip_special_tokens=True)

    # Clean up output
    cleaned = decoded.replace(prompt, "").strip()
    paragraph = cleaned.replace("\n", " ").strip()
    return f"{paragraph}" if paragraph else "Sorry, couldn't generate a meaningful email."

# 🎨 Streamlit UI
st.set_page_config(page_title="Smart Email Generator", page_icon="📨", layout="centered")
st.title("📨 Smart Email Generator (GPT-2 Accurate)")
st.markdown("Enter your bullet point or task to generate a professional email.")

user_input = st.text_area("📝 Enter your bullet point or task:", height=100)

if st.button("Generate Email"):
    if not user_input.strip():
        st.warning("Please enter a valid task or bullet point.")
    else:
        with st.spinner("Generating email..."):
            prompt = f"Write a professional email for the following task: {user_input.strip()}"
            email = generate_email(prompt)
        st.markdown("### 📬 Generated Email:")
        st.success(email)
