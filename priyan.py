import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1", device_map="auto")

generator = load_model()

def generate_email(task):
    prompt = f"[INST] Write a professional and polite email for the task: {task} [/INST]"
    output = generator(prompt, max_new_tokens=256, do_sample=True, temperature=0.7)
    return output[0]["generated_text"].split("[/INST]")[-1].strip()

st.set_page_config(page_title="Smart Email Generator", page_icon="📧")
st.title("📨 Smart Email Generator (Mistral Instruct)")
st.markdown("Enter a task or situation and get a clean, professional email.")

task_input = st.text_area("📝 Task or situation (e.g., 'I'm sick', 'Need leave'):")

if st.button("Generate Email"):
    if not task_input.strip():
        st.warning("Please enter something.")
    else:
        with st.spinner("Generating..."):
            result = generate_email(task_input)
        st.markdown("### 📬 Generated Email:")
        st.success(result)
