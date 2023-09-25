import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport as pr
from streamlit_pandas_profiling import st_profile_report


st.title("Freddie mac single family dataset quality evaluation and summarization")
st.write("Please upload the dataset in csv/xls file format and indicate if it is Origination/Monthly performance data")

# Upload a file
option = st.selectbox("Select an option", ('Origination', 'Monthly'))
uploaded_file=""
uploaded_file = st.file_uploader(f"", type=['csv','xls'])


if uploaded_file is not None:
    with open(option.lower() + '_columns.txt', 'r') as file:
        column_names = [line.strip() for line in file]
    
    file_extension = uploaded_file.name.split('.')[1]
    if file_extension.lower() == "csv":
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    df.columns = column_names
    st.write(df.head(5))
        
    profile = pr(df, explorative=True)
    st.write("Data Summary:")
    
    st.title("Pandas Profiling Report")
    st_profile_report(profile)
