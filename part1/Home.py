import streamlit as st
import requests
import uuid
from pypdf import PdfReader
import subprocess
import time
import os

st.title("Securities and Exchange commision form summarizer")

# Create an input field for the command
input_type_option = st.selectbox("How would you like to provide the form to summarize", ('Link', 'Upload a PDF'))
if input_type_option == 'Link':
    file_link = st.text_input("Enter the link to any Securities and Exchange commision form.")
else:
    uploaded_file = st.file_uploader("Upload any Securities and Exchange commision form in pdf format", type=["pdf"])

library_option = st.radio("Select the library to sumamrize your pdf", ('PyPdf', 'Nougat'))

if library_option == 'Nougat':
    collab_link = st.text_input("Enter the localtunnel link to google collab running nougat_api.")

if st.button("Run Command"):
    if input_type_option == 'Link':
        file_path=''
        if file_link is not "":
            random_uuid = uuid.uuid4()
            file_directory = subprocess.check_output("pwd", shell=True, text=True)[:-1]+"/file"
            os.makedirs(file_directory, exist_ok=True)
            file_path = file_directory+"/"+str(random_uuid)+".pdf"
            try:
                response = requests.get(file_link)
                response.raise_for_status()  # Check for any HTTP errors.
                with open(file_path, 'wb') as file:
                    file.write(response.content)

                print(f"File downloaded and saved as {file_path}")
            except requests.exceptions.RequestException as e:
                st.error("Error in fetching file from link. Please provide a valid link to any Securities and Exchange commision form.")
                print(f"Error: {e}")
        else:
            st.error("Please provide a link to any Securities and Exchange commision form.")
    else:
        file_path=''
        if uploaded_file is not None:
            random_uuid = uuid.uuid4()
            file_directory = subprocess.check_output("pwd", shell=True, text=True)[:-1]+"/file"
            os.makedirs(file_directory, exist_ok=True)
            file_path = file_directory+"/"+str(random_uuid)+".pdf"
            with open(file_path, "wb") as pdf_file:
                pdf_file.write(uploaded_file.read())
        else:
            st.error("Please upload any Securities and Exchange commision form in pdf format.")
    if library_option == "Nougat":
        if collab_link is not "":
            if file_path is not "":
                start_time = time.time()
                with open(file_path, 'rb') as pdf_file:
                    reader = PdfReader(pdf_file)
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
                    files = {
                     'file': (str(random_uuid) + "_" +str(page_num)+ ".pdf", open(file_path, 'rb'), 'application/pdf')
                }
                    response = requests.post(collab_link+"/predict", headers=headers, files=files, params=params)
                    if response.status_code == 200:
                        st.write("Page No: " + str(page_num))
                        st.write(response.text)
                    else:
                        st.error("Request failed with status code:" + str(response.status_code))
                        st.error(response.text)
                end_time = time.time()
                st.subheader("Time taken")
                st.text(end_time - start_time )
            else:
                pass
        else:
            st.error("Please provide a localtunnel link to google collab running nougat_api.")
    else:
        if file_path is not "":
            start_time = time.time()
            num_words=0
            with open(file_path, 'rb') as pdf_file:
                reader = PdfReader(pdf_file)
                number_of_pages  = len(reader.pages)
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
            
    
    
    
    
    
