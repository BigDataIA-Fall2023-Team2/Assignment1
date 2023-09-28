import streamlit as st
import subprocess
import time
import os

st.title("Run Command in Streamlit")

# Create an input field for the command
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Define the output directory
    output_directory = st.text_input("Enter the output directory")

   # output_directory = "/root/DAMG7245/Assignment1/Assignment1/part1/nougat"
    
    # Construct the command with the output file path
    output_file_path = os.path.join(output_directory, uploaded_file.name.replace(".pdf", ".mmd"))
    command = f"nougat {uploaded_file.name} -o {output_directory}"


    st.write(command)

    # Create a button to run the command
    if st.button("Run Command"):
        if command:
            try:
                # Run the command and capture the output
                start_time = time.time()
                output = subprocess.check_output(command, shell=True, text=True)
                end_time = time.time()
                elapsed_time = end_time - start_time

                st.success("Command executed successfully in {:.2f} seconds:".format(elapsed_time))
                st.code(output)

                # Read and display the contents of the generated .mmd file
                with open(output_file_path, "r") as mmd_file:
                    mmd_content = mmd_file.read()
                    st.write("Contents of generated .mmd file:")
                    st.write(mmd_content)
            except subprocess.CalledProcessError as e:
                st.error(f"Command failed with error code {e.returncode}:")
                st.code(e.output)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter a command to run.")
else:
    st.warning("Please upload a PDF file to run the command with.")
