import streamlit as st
import pdfplumber
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import io

# Download NLTK data
nltk.download('punkt')

st.title("📄 Resume Analyzer")

# Job description input
job_desc = st.text_area("Paste Job Description here:", height=150)

# Resume file uploader
resume_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def get_similarity(text1, text2):
    vectorizer = TfidfVectorizer().fit_transform([text1, text2])
    similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]
    return similarity * 100  # convert to percentage

if st.button("Analyze") and resume_file and job_desc:
    with st.spinner("Analyzing resume..."):
        resume_text = extract_text_from_pdf(resume_file)
        similarity_score = get_similarity(resume_text, job_desc)

        st.subheader("🔍 Match Score")
        st.success(f"Your resume matches the job description by **{similarity_score:.2f}%**")
        st.markdown("---")
        st.subheader("📝 Resume Content Preview")
        st.write(resume_text[:1000] + "...")  # show preview only
