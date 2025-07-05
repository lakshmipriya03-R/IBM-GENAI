import streamlit as st

# 🔹 Define template responses
TEMPLATES = {
    "sick": "I'm feeling unwell and will be taking a sick day today. Please let the team know.",
    "leave": "I would like to request a leave of absence for the mentioned dates. Kindly approve.",
    "meeting": "A team meeting is scheduled. Please make sure to attend on time.",
    "report": "Please prepare and submit the report by the end of the day.",
    "deadline": "The project deadline has been updated. Please adjust your schedule accordingly.",
    "timesheet": "Please remember to submit your timesheet before Monday.",
    "client": "The client has provided new feedback. Please review and make the necessary changes.",
    "work from home": "I'll be working remotely today. Feel free to reach me via email or chat.",
    "follow up": "This is a gentle reminder to follow up on the previous conversation or email."
}

def generate_email(text):
    text = text.lower()
    for keyword, template in TEMPLATES.items():
        if keyword in text:
            return template
    return "Sorry, I couldn't generate a suitable email for this task. Please try rephrasing."

# 🔹 Streamlit App UI
st.set_page_config(page_title="Smart Email Generator", page_icon="📧", layout="centered")
st.title("📧 Smart Email Generator (Rule-Based)")
st.caption("Enter a short task or bullet point and get a professional email draft.")

user_input = st.text_area("✏ Enter a task or bullet point:")

if st.button("Generate Email"):
    if not user_input.strip():
        st.warning("⚠ Please enter something to generate.")
    else:
        result = generate_email(user_input)
        st.success("✅ Generated Email:")
        st.write(result)
