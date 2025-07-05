import streamlit as st
from llama_cpp import Llama

# Load Mistral model (local)
@st.cache_resource
def load_model():
    return Llama(model_path="./mistral-7b-instruct-v0.1.Q4_K_M.gguf", n_ctx=2048, n_threads=4)

llm = load_model()

def generate_email(task):
    prompt = f"""<s>[INST] Write a professional and polite email for the task: {task} [/INST]"""
    output = llm(prompt, max_tokens=256, stop=["</s>"])
    return output['choices'][0]['text'].strip()

# Streamlit UI
st.set_page_config(page_title="Smart Email Generator", page_icon="📧")
st.title("📨 Smart Email Generator (Mistral 7B)")
st.markdown("Enter a task or situation and get a professional email.")

task = st.text_area("📝 Task / Situation:")

if st.button("Generate Email"):
    if not task.strip():
        st.warning("Please enter a task.")
    else:
        with st.spinner("Generating..."):
            result = generate_email(task)
        st.markdown("### 📬 Generated Email:")
        st.success(result)
