import streamlit as st
import pypdf
import io
from pypdf import PdfReader
import textwrap
import time

st.title("PDF Text Extractor")
st.write("Upload a PDF file and extract its text........")


uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file:

    start_time = time.time()
    pdf_file = io.BytesIO(uploaded_file.read())

    reader = PdfReader(pdf_file)

    number_of_pages = len(reader.pages)

    extracted_text = ""

    for page_num in range(number_of_pages):
        page = reader.pages[page_num]
        extracted_text += page.extract_text()

    end_time = time.time()
    st.subheader("Time taken")
    st.text(end_time - start_time)
    st.subheader("Extracted Text")
    st.text(extracted_text)
    words = extracted_text.split()
    num_words = len(words)
    st.subheader("Number of Words")
    st.text(num_words)

