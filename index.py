import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Exam Prep Suite",
    layout="wide"
)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Exam:", ["Operating Systems Exam", "Object Oriented Programming Exam"])

# --- PAGE 1: OS EXAM (index.html) ---
if page == "Operating Systems Exam":
    st.title("🖥️ Advanced Operating Systems Exam")
    
    html_path = Path("index.html")
    if html_path.exists():
        html_content = html_path.read_text(encoding="utf-8")
        components.html(
            html_content,
            height=900,
            scrolling=True
        )
    else:
        st.error("❌ index.html not found. Make sure it's in the same folder as app.py.")

# --- PAGE 2: OOP EXAM (oop.html) ---
elif page == "Object Oriented Programming Exam":
    st.title("📘 Object Oriented Programming Exam")
    st.caption("11 Lectures Summary | Cram Mode Active")
    
    oop_html_path = Path("oop.html")  # Your second HTML file
    if oop_html_path.exists():
        oop_content = oop_html_path.read_text(encoding="utf-8")
        components.html(
            oop_content,
            height=900,
            scrolling=True
        )
    else:
        st.error("❌ oop.html not found. Make sure it's in the same folder as app.py.")
        st.info("💡 Tip: Save your AI agent's output as 'oop.html' in the same directory")