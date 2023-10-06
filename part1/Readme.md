# Assignment 1 - Part 1 (Text extraction from PDF)
 

### Project Descrition 
Extracting and showing text from a pdf (using nougat & pypdf package) and generate a summary of metrics such as number of words, number of pages etc.

Below were the points observed while doing text extraction using the two packages:

|                   | Nougat                        | PyPDF                        |
| ----------------- | ----------------------------- | ----------------------------- |
| **Execution Time**| It took 7.65 sec (for 6 pages)        | It took 0.19 sec (for 6 pages)        |
| **Text Extraction**| - A new line is treated as a new line while extracting text. <br> - It understands tabular data formats as text formatting is shown using '/n'. <br> - Recognizes heading formatting and titles. <br> - It may lose content due to excessive spaces. <br> - It may also contain spelling errors, e.g. "cigature." | - A new line is not considered as a new line as the text is displayed continuously one after the other. <br> - It doesn't understand tabular data formats. <br> - It does not recognize heading formatting and titles. <br> - It preserves content even with repeated spaces. <br> - No spelling mistakes were observed. |
| **Financial Symbols**| It cannot recognize financial symbols or jargon. | It cannot recognize financial symbols or jargon. |
| **Serial Number**| It can recognize pointers or serial numbers and modify it. | It cannot recognize pointers or serial numbers. It will show case as text only |

### Application Link

https://t2a1p1.streamlit.app/

### Project Resources

https://codelabs-preview.appspot.com/?file_id=1t61T-7IzchvC1qUAso0RRaTfmnOdUZSInwzfCeEK8QM#7

### Project Demo 

https://www.youtube.com/watch?v=SEqMB00-zDw

### Tech Stack
Python | Streamlit | Google Collab | Pydpf | Nougat

### Architecture diagram ###

![image](https://github.com/BigDataIA-Fall2023-Team2/Assignment1/assets/131703516/48d5167d-0a34-48a6-8e01-cb487a8aba85)


![image](https://github.com/BigDataIA-Fall2023-Team2/Assignment1/assets/131703516/9f21a8dc-6bf5-48b0-9a7e-14f3f7bee719)



### Project Flow

The user uploads a pdf file in the application or can directly paste the URL of the pdf from a website. The user then has option to select the package (nougat or pydf) that can be used for text extraction of pdf and summary of metrics. The user will then open a new google collab notebook at https://colab.google/ and run the code present in the google collab notebook. The google collab notebook will generate an output URL and the user has to sumbit this URL in the application. The application then extracts the text from pdf and displays text and other metrics such as number of pages, number of words.
   

### Code Explaination

```
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

```
In the above code we are firstly importing necessary packages, we are giving options to select either file link or pdf. Then we are giving radio buttons to select the package that can be used for execution as you can see in the library_option variable. If the library_option is nougat then it is asking the user to launch the collab notebook using the URL mentioned. It is a publicly shared google collab notebook that contains the required code which user need to run. The generated output by google collab should be added in the input box of collab link. The collab contains the below code 

```

!pip install nougat_ocr
!npm install -g localtunnel

!nougat_api &> /content/log.txt &

!cat log.txt

!npx localtunnel --port 8503

```

In the above code (which is in google collab) we are using localtunnel package of nodejs. LocalTunnel is a tool that allows you to expose a locally hosted web server or application to the internet. It creates a temporary public URL that you can use to access your local development server. We are also installing nougat_ocr package with it. Then we are using the official command of nougat_ocr of calling the API as nougat_api and storing the command output in log file inside content directory. In the next line, using 'cat' command, we are reading the contents of the log file. Then the last command will generate a public URL where the application on local enviornment is running. 

```
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

```
The above code checks if the link and file that has been uploaded correctly. If the link is shared, response.get() tries to fetch the file and if there is an error while fetching it will raise an exception. If no file is uploaded then the exception to upload the form in pdf format will be raised. 

```
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
    
```

The code checks if the value of the variable library_option is equal to "Nougat." Within this "Nougat" section, the code checks multiple conditions before proceeding ahead :

a. It first checks if the collab_link variable is empty. This variable represents the URL related to Google Colab.

b. Next, it checks two conditions within - It checks if input_type_option is equal to 'Link' and if file_link is not empty. Alternatively, it checks if input_type_option is equal to 'Upload a PDF' and if uploaded_file is not provided. This condition suggests that the script can handle two different ways of providing input data: via a link or by uploading a PDF file.

c. It uses a PDF reader (PyPDF) to count the number of pages in the PDF file provided. It sends HTTP requests to a specified collab_link for each page of the PDF file. This involves setting up headers and parameters for the requests. For each page, it sends a POST request with the PDF page content as a file. If the response status code is 200 (indicating success), it prints the page number and the response content. If a request fails (status code other than 200), it retries the request up to three times before giving up. Failed requests are printed with the status code and response content. If, after three retries, a request still fails, it displays an error message indicating that multiple requests have failed. The script also measures and displays the time taken for this process. If any of the conditions in step 2 are not met, the script does not perform any actions (indicated by the "pass" statement). 


```
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
```

The above code is used for pypdf part. Here we are checking if link or pdf is valid. Then we are noting the start time of the process and reading the file contents (io.BytesIO(file_content)) and finding out the number of pages (len(reader.pages)). We are then extracting text for each page one after the other (page.extract_text()) and calculating the number of words (len(extracted_text.split())). Then we are noting the end time of the process and calculating how much time it is taking for end to end pdf extraction.

### Repository Structure

![image](https://github.com/BigDataIA-Fall2023-Team2/Assignment1/assets/131703516/6e2cb954-722c-4979-a008-c272205a16b7)



### Contributions

| Name                            | Contribution                  |  
| ------------------------------- | ------------------------------|
| Chinmay Gandi                   | PyPdf                         |
| Dhawal Negi, Shardul Chavan     | Nougat                        |
| Chinmay Gandi, Shardul Chavan   | Nougat vs PyPdf               | 
