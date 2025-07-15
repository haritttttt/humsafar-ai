
import streamlit as st

st.set_page_config(page_title="Humsafar AI", page_icon="🎓")

st.title("🎓 Humsafar AI – Your Career Guide After Class 12th")

st.markdown("Welcome! Let’s help you discover the best career path for your future. Answer a few simple questions below.")

# --- Form for Student Input ---
with st.form("career_form"):
    name = st.text_input("👤 Your Name:")

    stream = st.selectbox("📚 Your Stream in Class 12th:", 
                          ["Select...", "Science (PCM/PCB)", "Commerce", "Arts/Humanities"])

    interest = st.selectbox("💡 Your Area of Interest:", 
                            ["Select...", 
                             "Technology / Engineering", 
                             "Medicine / Biology", 
                             "Business / Management", 
                             "Creativity / Arts", 
                             "Government Services / UPSC"])

    submit = st.form_submit_button("Get Career Suggestions")

# --- Logic for Suggestions ---
if submit:
    if stream == "Select..." or interest == "Select...":
        st.warning("⚠️ Please select both stream and interest to proceed.")
    else:
        st.success(f"Great, {name}! Here are your personalized career suggestions:")

        if stream == "Science (PCM/PCB)":
            if interest == "Technology / Engineering":
                st.markdown("- 🚀 B.Tech in Computer Science, Electrical, Mechanical, etc.")
                st.markdown("- 🤖 AI/ML, Robotics, Data Science")
            elif interest == "Medicine / Biology":
                st.markdown("- 🏥 MBBS, BDS, B.Pharm, Nursing")
                st.markdown("- 🔬 Biomedical Engineering, Biotech")
            elif interest == "Government Services / UPSC":
                st.markdown("- 🪖 NDA, Defense Services")
                st.markdown("- 🏛️ UPSC Civil Services")

        elif stream == "Commerce":
            if interest == "Business / Management":
                st.markdown("- 📈 BBA, B.Com, CA, CS")
                st.markdown("- 💼 Finance, Marketing, HR")
            elif interest == "Government Services / UPSC":
                st.markdown("- 🏛️ SSC, UPSC, Banking Exams")

        elif stream == "Arts/Humanities":
            if interest == "Creativity / Arts":
                st.markdown("- 🎨 Design, Journalism, BA in English, Psychology, Sociology")
                st.markdown("- 🎭 Fine Arts, Media, Fashion")
            elif interest == "Government Services / UPSC":
                st.markdown("- 📚 BA + UPSC/State PCS")
                st.markdown("- ⚖️ Law, Social Work, Teaching")

        st.markdown("---")
        st.info("🔁 You can refresh the page to try different combinations!")
