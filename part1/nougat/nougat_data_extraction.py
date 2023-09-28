import streamlit as st

import subprocess

import time

# import streamlit_scrollable_textbox as stx

 

# stx.scrollableTextbox('My very long text.')

 

st.title("Run Command in Streamlit")

 

 

# Create an input field for the command

# command = "nougat " + st.text_input("Enter File path") + " -o " + st.text_input("Output Directory")

command = "nougat"+" /root/DAMG7245/Assignment1/Assignment1/part1/nougat/paper2.pdf"+" -o "+"/root/DAMG7245/Assignment1/Assignment1/part1/nougat"

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

            st.success("Command executed successfully:"+ "elapsed_time")

            st.code(output)

        except subprocess.CalledProcessError as e:

            st.error(f"Command failed with error code {e.returncode}:")

            st.code(e.output)

    else:

        st.warning("Please enter a command to run.")