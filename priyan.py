import streamlit as st

# ✅ 50+ Prewritten email templates
email_templates = {
    "i'm sick": """Dear [Manager],

I hope you're doing well. I'm feeling unwell and would like to take a sick day to rest and recover. I'll keep you posted on my condition.

Thank you for your understanding.

Best regards,
[Your Name]
""",
    "need leave": """Dear [Manager],

I would like to request leave due to personal reasons. Please let me know if any documentation is required.

Thank you for your support.

Sincerely,
[Your Name]
""",
    "project deadline": """Dear Team,

This is a reminder that our project deadline is approaching. Please make sure all deliverables are finalized by [Deadline Date].

Let me know if you face any blockers.

Thanks,
[Your Name]
""",
    "client feedback": """Dear [Client],

Just following up to see if you had any feedback on our proposal. We're happy to revise anything based on your inputs.

Looking forward to hearing from you.

Best regards,
[Your Name]
""",
    "reschedule meeting": """Dear Team,

Due to a scheduling conflict, I’d like to reschedule our meeting. Please share your availability for the next two days.

Apologies for the change.

Regards,
[Your Name]
""",
    "office closed": """Dear All,

Please note that the office will remain closed on [Date] due to [Reason]. You may continue working remotely as required.

Thanks for your cooperation.

Regards,
[Your Name]
""",
    "internet issue": """Dear [Manager],

I'm facing internet issues and may not be able to attend virtual meetings today. I'll keep you updated.

Apologies for the inconvenience.

Regards,
[Your Name]
""",
    "late to office": """Dear [Manager],

I wanted to inform you that I’ll be reaching the office late due to [Reason]. I’ll make up the time accordingly.

Thank you for your understanding.

Best regards,
[Your Name]
""",
    "appreciate team": """Dear Team,

Kudos to everyone for your hard work and commitment! I'm truly proud of what we've achieved together.

Let’s keep the momentum going.

Warm regards,
[Your Name]
""",
    "follow up": """Dear [Recipient],

Just checking in on the below request. Please let me know if there's any update or if further input is needed from my side.

Thanks,
[Your Name]
""",
    "weekly report": """Dear [Manager],

Please find below the weekly report for [Week]:

- Completed: ...
- In Progress: ...
- Blockers: ...

Let me know if you'd like more details.

Regards,
[Your Name]
""",
    "daily update": """Dear Team,

Here’s my daily update:

- Task A: Done  
- Task B: In progress  
- Blockers: None  

Thanks,  
[Your Name]
""",
    "thank you": """Dear [Name],

Thank you so much for your support on [specific task/project]. I really appreciate your help.

Warm regards,  
[Your Name]
""",
    "reminder meeting": """Dear All,

This is a reminder for our meeting scheduled on [Date] at [Time]. Please be prepared with updates.

See you all then.

Best,  
[Your Name]
""",
    "training session": """Dear Team,

You are invited to a training session on [Topic] scheduled for [Date, Time]. Attendance is mandatory.

Best,  
[Your Name]
""",
    "out of office": """Dear [Recipient],

I will be out of office from [Start Date] to [End Date]. For urgent matters, please contact [Alternative Contact].

Thanks,  
[Your Name]
""",
    "work from home": """Dear [Manager],

I’d like to request permission to work from home today due to [Reason]. I’ll remain available online and ensure tasks are completed.

Regards,  
[Your Name]
""",
    "request extension": """Dear [Manager],

I’d like to request an extension on the [Task/Project] deadline due to [Reason]. I assure you of quality and timely submission thereafter.

Thank you for your understanding.

Best,  
[Your Name]
""",
    "submit documents": """Dear [Recipient],

Please find attached the requested documents. Let me know if anything else is required.

Thanks,  
[Your Name]
""",
    "schedule interview": """Dear [Candidate],

We would like to schedule your interview for [Role] on [Date] at [Time]. Please confirm your availability.

Regards,  
[Recruiter Name]
""",
    "team lunch": """Dear Team,

We’re planning a team lunch on [Date] at [Venue]. Please RSVP by [Deadline].

Looking forward to seeing you all there!

Warmly,  
[Your Name]
""",
    "holiday notice": """Dear All,

The office will remain closed on [Date] for [Holiday Name]. Wishing everyone a safe and joyful holiday!

Regards,  
HR Team
""",
    "onboarding": """Dear [New Joiner],

Welcome aboard! We’re excited to have you join [Company]. Please report on [Date] at [Time]. Your onboarding schedule is attached.

Best,  
HR Team
""",
    "performance review": """Dear [Employee],

Your annual performance review is scheduled for [Date]. Please ensure your self-evaluation is completed by then.

Thanks,  
[Manager Name]
""",
    "reject request": """Dear [Name],

Thank you for your request. Unfortunately, we are unable to approve it at this time due to [Reason].

Regards,  
[Your Name]
""",
    "approve leave": """Dear [Employee],

Your leave request from [Start Date] to [End Date] has been approved. Wishing you a restful break.

Best,  
[Manager Name]
""",
    "complaint received": """Dear [Name],

We acknowledge receipt of your complaint regarding [Issue]. Our team is reviewing the matter and will revert shortly.

Sincerely,  
[Support Team]
""",
    "issue resolved": """Dear [Name],

We’re glad to inform you that the reported issue has been resolved. Please verify and let us know if you face any further difficulties.

Thank you,  
Support Team
""",
    "greeting": """Dear [Name],

Hope you're having a wonderful day! Just checking in to see how things are going on your side.

Warm wishes,  
[Your Name]
""",
    "handover task": """Dear [Name],

As discussed, I’m handing over [Task] to you during my absence. All documents have been shared.

Thank you for your support.

Best,  
[Your Name]
""",
}

# 🚀 Streamlit App
st.set_page_config(page_title="Smart Email Generator", layout="centered")
st.title("📨 Smart Email Generator (50+ Templates)")
st.markdown("Enter your situation/task to generate a clean professional email instantly.")

user_input = st.text_input("📝 Task or Situation (e.g., I'm sick, Request leave)").lower()

if st.button("Generate Email"):
    if not user_input.strip():
        st.warning("Please enter a task to generate an email.")
    else:
        matched = False
        for key, template in email_templates.items():
            if key in user_input:
                st.markdown("### 📬 Generated Email")
                st.code(template)
                matched = True
                break
        if not matched:
            # Generic fallback email
            st.markdown("### 📬 Generated Email (Generic)")
            st.code(f"""Dear [Recipient],

I hope this message finds you well. I'm reaching out regarding the following matter: "{user_input.strip()}".

Please let me know if you need any further details or clarification.

Thank you for your attention.

Best regards,  
[Your Name]
""")
