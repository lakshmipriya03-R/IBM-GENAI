import streamlit as st
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

def generate_email_gpt2(user_input, max_length=100):
    prompt = f"Write a professional email for the following note:\n'{user_input}'\nEmail:"
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)

    output = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        early_stopping=True
    )

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    email_body = generated_text.split("Email:")[-1].strip()
    return email_body

# Streamlit UI
st.set_page_config(page_title="Smart Email Generator", page_icon="📧", layout="centered")
st.title("📧 Smart Email Generator (GPT-2 Accurate)")

user_input = st.text_input("📝 Enter your bullet point or task:")
if st.button("Generate Email"):
    if user_input:
        with st.spinner("Generating email..."):
            result = generate_email_gpt2(user_input)
        st.success("📬 Generated Email:")
        st.write(result)
    else:
        st.warning("Please enter a bullet point or task to generate an email.")
