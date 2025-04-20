import streamlit as st

st.set_page_config(page_title="ATS Resume Screening", layout="wide")

st.title("🤖 ATS Resume Screening App")

view = st.sidebar.selectbox("Select Role", ["HR", "Candidate"])

if view == "HR":
    st.header("👩‍💼 HR Dashboard")
    uploaded_jd = st.file_uploader("Upload Job Description", type=["pdf", "docx", "txt"])
    if uploaded_jd:
        st.success("Job Description uploaded!")

    candidates = ["John Doe", "Jane Smith"]
    selected_candidate = st.selectbox("Select Candidate", candidates)
    st.metric("ATS Score", "78%")
    st.progress(0.78)
    st.markdown("✅ Matched: Python, SQL\n❌ Missing: Power BI")

elif view == "Candidate":
    st.header("📋 Candidate Dashboard")
    uploaded_resume = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])
    if uploaded_resume:
        st.success("Resume uploaded!")

    st.metric("ATS Score", "65%")
    st.progress(0.65)
    st.markdown("✅ Matched: Python\n❌ Missing: Power BI\n💡 Add projects using ETL tools")
