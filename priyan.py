import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load GPT-2 Model and Tokenizer (cache to avoid reloading every time)
@st.cache_resource
def load_gpt2():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    model.eval()  # Set the model to evaluation mode
    return tokenizer, model

def generate_email_gpt2(prompt, tokenizer, model, max_length=80):
    # Encoding the input prompt
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Generate the output with beam search
    output = model.generate(
        input_ids,
        max_length=max_length,
        num_beams=4,
        no_repeat_ngram_size=2,
        early_stopping=True
    )

    # Decode the generated output
    return tokenizer.decode(output[0], skip_special_tokens=True)

# ----- Streamlit App -----
st.title("📧 Smart Email Generator with GPT-2")

user_input = st.text_area("Enter a task or bullet point:", placeholder="e.g. remind team about meeting at 10am")

if st.button("Generate Email"):
    if user_input.strip() == "":
        st.warning("Please enter a bullet point.")
    else:
        tokenizer, model = load_gpt2()  # Load GPT-2 model only once
        result = generate_email_gpt2(f"Convert this into a professional email: {user_input}", tokenizer, model)
        st.subheader("📬 Generated Email:")
        st.write(result)