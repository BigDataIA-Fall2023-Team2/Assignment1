import streamlit as st
import requests
import uuid
from pypdf import PdfReader
import subprocess
import time
import os
import io

st.title("Securities and Exchange commision form summarizer")

# Create an input field for the command
input_type_option = st.selectbox("How would you like to provide the form to summarize", ('Link', 'Upload a PDF'))
if input_type_option == 'Link':
    file_link = st.text_input("Enter the link to any Securities and Exchange commision form.")
else:
    uploaded_file = st.file_uploader("Upload any Securities and Exchange commision form in pdf format", type=["pdf"])

library_option = st.radio("Select the library to sumamrize your pdf", ('PyPdf', 'Nougat'))

if library_option == 'Nougat':
    st.write("Launch this notebook to generate localtunnel link (https://colab.research.google.com/drive/1p1GjuY8mrnZlx1IsC2F1hvqYusFJPmli?usp=sharing)")
    collab_link = st.text_input("Enter the localtunnel link to google collab running nougat_api.")


if st.button("Run Command"):
    if input_type_option == 'Link':
        if file_link != '':
            try:
                file_response = requests.get(file_link)
                file_response.raise_for_status()  # Check for any HTTP errors.
                file_content = file_response.content
            except requests.exceptions.RequestException as e:
                st.error("Error in fetching file from link. Please provide a valid link to any Securities and Exchange commision form.")
                print(f"Error: {e}")
        else:
            st.error("Please provide a link to any Securities and Exchange commision form.")
    else:
        if uploaded_file is not None:
            file_content = uploaded_file.read()
        else:
            st.error("Please upload any Securities and Exchange commision form in pdf format.")
    if library_option == "Nougat":
        if collab_link != "":
            if ((input_type_option == 'Link' and file_link != '') or (input_type_option == 'Upload a PDF' and uploaded_file is not None)):
                start_time = time.time()
                
                reader = PdfReader(io.BytesIO(file_content))
                number_of_pages  = len(reader.pages)
                st.write("Number of pages in the PDF are: " + str(number_of_pages))
                headers = {
                    'accept': 'application/json',
                    'Bypass-Tunnel-Reminder': 'true',
                }
                for page_num in range(1, number_of_pages+1):
                    params = {
                        'start': page_num,  
                        'stop': page_num
                    }
                    request_counter =0
                    while request_counter < 3:
                        random_uuid = uuid.uuid4()
                        files = {
                        'file': (str(random_uuid) + "_" +str(page_num), file_content, 'application/pdf')
                        }
                        nougat_response = requests.post(collab_link+"/predict", headers=headers, files=files, params=params)
                        if nougat_response.status_code == 200:
                            st.write("Page No: " + str(page_num))
                            st.write(nougat_response.text)
                            break
                        else:
                            print("Request failed with status code:" + str(nougat_response.status_code))
                            print(nougat_response.text)
                            request_counter += 1
                    if request_counter == 3:
                        st.error("Multiple requests failed")
                        st.error("Please check your localtunnel to nougat_api on google collab!!!")
                        break
                end_time = time.time()
                st.subheader("Time taken")
                st.text(end_time - start_time )
            else:
                pass
        else:
            st.error("Please provide a localtunnel link to google collab running nougat_api.")
    else:
        if ((input_type_option == 'Link' and file_link != '') or (input_type_option == 'Upload a PDF' and uploaded_file is not None)):
            start_time = time.time()
            num_words=0
            reader = PdfReader(io.BytesIO(file_content))
            number_of_pages  = len(reader.pages)
            st.write("Number of pages in the PDF are: " + str(number_of_pages))
            for page_num in range(number_of_pages):
                page = reader.pages[page_num]
                st.write("Page No: " + str(page_num+1))
                extracted_text = page.extract_text()
                st.write(extracted_text)
                num_words += len(extracted_text.split())
            st.subheader("Number of Words")
            st.text(num_words)
            end_time = time.time()
            st.subheader("Time taken")
            st.text(end_time - start_time)
        else:
            pass