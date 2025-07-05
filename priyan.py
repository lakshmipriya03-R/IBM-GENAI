import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
import torch

# --- Load model & tokenizer only once (cached for speed) ---
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
    model = AutoModelForCausalLM.from_pretrained("distilgpt2")
    model.eval()
    return tokenizer, model

# --- Generate email from input ---
def generate_email(prompt: str, tokenizer, model):
    # Few-shot examples to guide the model
    examples = [
        ("project deadline extended to next friday",
         "The project deadline has been extended to next Friday. Please adjust your schedules accordingly."),

        ("i have a headache",
         "I am feeling unwell and have a headache today, so I will be taking a sick day. Thank you for your understanding."),

        ("client meeting scheduled at 2pm",
         "A client meeting is scheduled today at 2 PM. Please be prepared and join on time."),

        ("ask for budget approval",
         "Please review the attached budget proposal and provide your approval at the earliest convenience."),

        ("i will be working from home tomorrow",
         "I will be working from home tomorrow due to personal commitments. I will remain available online throughout the day."),

        ("congratulate team for successful release",
         "Congratulations to the entire team on the successful release! Your hard work and dedication are truly appreciated.")
    ]

    # Build the input prompt
    few_shot_prompt = ""
    for bullet, email in examples:
        few_shot_prompt += f"Bullet: {bullet}\nEmail: {email}\n\n"
    few_shot_prompt += f"Bullet: {prompt}\nEmail:"

    # Tokenize input
    inputs = tokenizer(few_shot_prompt, return_tensors="pt")
    input_ids = inputs.input_ids

    # Generate response using fast greedy decoding
    gen_config = GenerationConfig(
        max_new_tokens=60,
        do_sample=False,
        num_beams=1,
        pad_token_id=tokenizer.eos_token_id
    )

    with torch.no_grad():
        output = model.generate(input_ids=input_ids, generation_config=gen_config)

    full_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # Extract only the generated email
    generated_part = full_text[len(few_shot_prompt):].strip()

    return generated_part

# --- Streamlit UI ---
st.set_page_config(page_title="AI Email Generator", page_icon="📧")
st.title("📧 Smart Email Generator (Fast + Accurate)")

user_input = st.text_area("📝 Enter your bullet point or task:")

if st.button("Generate Email"):
    if not user_input.strip():
        st.warning("⚠ Please enter something first.")
    else:
        tokenizer, model = load_model()
        email = generate_email(user_input, tokenizer, model)
        st.subheader("📬 Generated Email:")
        st.success(email)
