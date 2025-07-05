import streamlit as st
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Set page config
st.set_page_config(page_title="Smart Email Generator", layout="centered")

# Load model and tokenizer once using caching
@st.cache_resource
def load_model():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    model.eval()
    return tokenizer, model

tokenizer, model = load_model()

# Function to generate email
def generate_email(prompt, max_length=100):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    output = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        num_beams=5,
        early_stopping=True
    )

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    
    # Extract only the newly generated content (remove input prompt if repeated)
    cleaned_text = generated_text.replace(prompt, "").strip()

    return cleaned_text if cleaned_text else "Sorry, the model could not generate a useful email. Please try again with clearer input."

# Streamlit UI
st.markdown("📨 *Smart Email Generator (GPT-2 Accurate)*")
st.markdown("Enter your bullet point or task to generate a professional email.")

user_input = st.text_area("📝 Enter your bullet point or task:", placeholder="e.g., I'm sick and cannot attend the meeting.")

if st.button("Generate Email"):
    if user_input.strip():
        with st.spinner("Generating..."):
            prompt = f"Write a professional email for: {user_input}"
            email = generate_email(prompt)
        st.success("📬 Generated Email:")
        st.markdown(f"✉ {email}")
    else:
        st.warning("Please enter a valid input.")
