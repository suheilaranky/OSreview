import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Advanced OS Exam",
    layout="wide"
)

st.title("Advanced Operating Systems Exam")

html_path = Path("index.html")

if html_path.exists():
    html_content = html_path.read_text(encoding="utf-8")
    components.html(
        html_content,
        height=900,
        scrolling=True
    )
else:
    st.error("HTML file not found. Make sure the HTML file is in the same folder as app.py.")