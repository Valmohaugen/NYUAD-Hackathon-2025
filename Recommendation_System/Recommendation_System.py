import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI, ChatOpenAI
import os
import random
import pandas as pd
import altair as alt

# Load OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI Chat model
llm = ChatOpenAI(temperature=0.4, openai_api_key=openai_api_key, model="gpt-4o", max_tokens=3000)

# Define the prompt template for the health assistant
template = """
You are a compassionate AI health assistant. Always speak warmly, supportively, and as if you are a caring friend.

Task:
Given this brain wave analysis:
{diagnoses}
Identify the top two conditions with the highest percentages Only include the second if its percentage is 40% or more. Otherwise, focus only on the first.
For each included condition, provide:
A brief, friendly interpretation (1–2 sentences).
Specific, practical advice tailored to the severity.
Format each condition exactly as:
"[Condition Name]: [Brief interpretation]. [Practical advice]."

Rules:
Start with the condition that has the highest percentage.
Keep the entire response under 200 words.
DO NOT repeat the percentage or severity terms.
DO NOT use labels like "mild", "moderate", etc.
DO NOT mention "the results" or similar.
DO NOT use bullet points or numbering in the output.
Use warm, easy-to-understand language without medical jargon.
Sound caring and reassuring throughout.
"""
prompt = PromptTemplate(input_variables=["diagnoses"], template=template)
chain = prompt | llm

def classify_disease(likelihood, disease):
    """Classify the disease likelihood into descriptive severity labels."""
    if disease == 'normal':
        if likelihood < 50:
            return "Some risk likely"
        elif likelihood < 70:
            return "Mostly healthy"
        elif likelihood < 85:
            return "Healthy"
        else:
            return "Very healthy!"
    if disease == 'schizophrenia':
        if likelihood < 10:
            return "Very unlikely"
        elif likelihood < 25:
            return "Mild suspicion"
        elif likelihood < 40:
            return "Moderate risk"
        else:
            return "High risk"
    elif disease == 'depression':
        if likelihood < 15:
            return "Very unlikely"
        elif likelihood < 25:
            return "Mild symptoms likely"
        elif likelihood < 40:
            return "Moderate suspicion"
        elif likelihood < 60:
            return "High suspicion"
        else:
            return "Severe risk"
    elif disease == 'anxiety':
        if likelihood < 20:
            return "Very unlikely"
        elif likelihood < 30:
            return "Mild anxiety traits"
        elif likelihood < 50:
            return "Moderate suspicion"
        elif likelihood < 70:
            return "High likelihood"
        else:
            return "Severe anxiety likely"
    elif disease == 'adhd':
        if likelihood < 20:
            return "Very unlikely"
        elif likelihood < 30:
            return "Mild attention difficulties"
        elif likelihood < 45:
            return "Moderate suspicion"
        elif likelihood < 60:
            return "High likelihood"
        else:
            return "Severe ADHD highly likely"
    else:
        return "Unknown"

# Streamlit page setup
st.set_page_config(page_title="Brain Waves Mental Health Check", page_icon="🧠", layout="centered")

# Set custom background and styling
st.markdown("""
<style>
body {
    background-color: #f5f3ff;
}
.stApp {
    background-color: #f5f3ff;
    color: #333333;
    font-family: 'Helvetica Neue', sans-serif;
}
.title {
    text-align: center;
    font-size: 3em;
    color: #6a0dad;
}
</style>
""", unsafe_allow_html=True)

def create_pie_chart(data):
    """Create a pie chart visualization of the brain wave data."""
    df = pd.DataFrame({
        'Condition': list(data.keys()),
        'Value': list(data.values())
    })
    chart = alt.Chart(df).mark_arc().encode(
        theta=alt.Theta(field="Value", type="quantitative"),
        color=alt.Color(field="Condition", type="nominal", legend=alt.Legend(title="Conditions")),
        tooltip=['Condition', 'Value']
    ).properties(
        title='Brain Wave Analysis Results',
        width=350,
        height=350,
        background='#f5f3ff'
    ).configure_view(
        strokeWidth=0
    )
    return chart

def generate_test_data():
    """Generate simulated EEG brain wave percentages for demo purposes."""
    cuts = sorted([random.randint(85, 100)]+[random.randint(0, 100) for _ in range(3)])
    n = cuts[0]
    a = cuts[1] - cuts[0]
    b = cuts[2] - cuts[1]
    c = cuts[3] - cuts[2]
    d = 100 - cuts[3]
    return [n, a, b, c, d]

def get_model_output():
    """Simulate model output (can be updated with real model predictions)."""
    # Uncomment below to use random generated data
    return {
        "normal": data[0],
        "depression": data[1],
        "anxiety": data[2],
        "schizophrenia": data[3],
        "adhd": data[4]
    }
    # return {
    #     "normal": 60,
    #     "depression": 40,
    #     "anxiety": 0,
    #     "schizophrenia": 0,
    #     "adhd": 0
    # }

def dynamic_recommendations(summary_text):
    """Generate dynamic self-care tips based on user analysis."""
    rec_prompt = f"""
The user has the following situation:
{summary_text}
Suggest 5 short caring tips to feel better. Start each tip with "- ".
"""
    response = llm.invoke(rec_prompt).content
    tips = [tip.strip('- ').strip() for tip in response.split('\n') if tip.strip()]
    return tips

def display_recommendations_as_cards(tips):
    """Display the generated tips in card-like containers."""
    for tip in tips:
        with st.container():
            st.markdown(f"""
                <div style='background-color: #f0f4ff; padding: 15px; border-radius: 12px; margin-bottom: 10px; box-shadow: 0px 2px 8px rgba(0,0,0,0.15);'>
                    <p style='font-size: 16px; margin: 0;'>{tip}</p>
                </div>
            """, unsafe_allow_html=True)

# Display title
st.markdown("<h1 class='title'>📈 Brain Wave Mental Health Analyzer</h1>", unsafe_allow_html=True)

# Button to simulate receiving new data
if st.button("Receive New Data"):
    st.session_state.model_data = get_model_output()
elif 'model_data' not in st.session_state:
    st.session_state.model_data = get_model_output()

# Split into two columns: one for text, one for chart
col1, col2 = st.columns([1, 1])

with col1:
    st.write("### Analysis Results")
    for condition, value in st.session_state.model_data.items():
        severity = classify_disease(value, condition.lower())
        st.write(f"**{condition}:** {value}% - {severity}")

    if st.button("Analyze Data"):
        with st.spinner('Analyzing the brain wave data...'):
            user_input = st.session_state.model_data
            diagnoses = "\n".join([f"{disease}: {value}% likelihood" for disease, value in user_input.items()])
            report = chain.invoke({"diagnoses": diagnoses}).content
            st.session_state.report = report
            st.session_state.precise_report = report.split('\n')
            st.session_state.analysis_complete = True

with col2:
    chart = create_pie_chart(st.session_state.model_data)
    st.altair_chart(chart, use_container_width=True)

if 'analysis_complete' in st.session_state and st.session_state.analysis_complete:
    st.markdown("---")
    st.markdown("### Your Personalized Analysis")
    st.success(st.session_state.report)

    st.markdown("### 🏋️ Tips for Feeling Better")
    tips = dynamic_recommendations(st.session_state.report)
    display_recommendations_as_cards(tips)

    st.markdown("---")
    st.markdown("### 💬 Need More Help? Chat with Our Support Bot")

    # Support chat feature
    if st.button("Start Support Chat"):
        st.session_state.show_chat = True
        st.session_state.chat_history = []

    if st.session_state.get("show_chat"):
        user_msg = st.text_input("Your message:", key="chat_input")
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        if user_msg:
            st.session_state.chat_history.append({"role": "user", "content": user_msg})
            messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history]
            messages.insert(0, {"role": "system", "content": "You are a compassionate support assistant offering emotional support."})
            response = llm.invoke(messages).content
            st.session_state.chat_history.append({"role": "assistant", "content": response})

        if st.session_state.get("chat_history"):
            st.markdown("### Chat History")
            for msg in st.session_state.chat_history:
                if msg["role"] == "user":
                    st.markdown(f"**You:** {msg['content']}")
                else:
                    st.markdown(f"**Support Bot:** {msg['content']}")

    st.markdown("---")
    st.markdown("### Support Options")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("##### Find Help")
        if st.button("Find Mental Health Services Nearby"):
            st.session_state.show_map = True

        if "show_map" in st.session_state and st.session_state.show_map:
            st.write("Locating services in your area...")
            st.info("Please allow location access in your browser to find nearby services.")
            st.markdown("[National Mental Health Hotline](tel:988)")
            st.markdown("[Online Directory of Mental Health Providers](https://www.psychologytoday.com/us/therapists)")

    with col2:
        st.markdown("##### Connect")
        contact_option = st.selectbox("Contact support:", ["Select an option", "Send results to my doctor", "Share with family member", "Save report for later"])

        if contact_option == "Send results to my doctor":
            doctor_email = st.text_input("Doctor's email:")
            if st.button("Send Report") and doctor_email:
                st.success(f"Report would be sent to {doctor_email}")

        elif contact_option == "Share with family member":
            family_contact = st.text_input("Family member contact:")
            if st.button("Share Results") and family_contact:
                st.success(f"Results would be shared with {family_contact}")

        elif contact_option == "Save report for later":
            if st.button("Save Report"):
                st.success("Report saved. You can access it in your account.")
