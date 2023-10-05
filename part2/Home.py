import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport as pr
# from streamlit_pandas_profiling import st_profile_report
import great_expectations as gx
import uuid
import streamlit.components.v1 as components


def validate_data(df, datatype_option, filename):
    context = gx.data_context.DataContext("./gx")
    datasource = context.get_datasource("pandas_dataframe_datasource")
    random_uuid = uuid.uuid4()
    asset_name="asset_"+filename.split('.')[0].lower() +"_" +str(random_uuid)
    data_asset = datasource.add_dataframe_asset(name=asset_name)
    batch_request = data_asset.build_batch_request(dataframe=df)
    checkpoint=context.add_or_update_checkpoint(
        run_name_template=asset_name,
        name = "my_checkpoint",
        validations = [
            {
                "assest_name": asset_name,
                "batch_request": batch_request,
                "expectation_suite_name": datatype_option.lower() +"_expectations_suite"
            }
        ],
    )
    checkpoint_result = checkpoint.run(run_name="test")
    context.build_data_docs()
    with open("./gx/uncommitted/data_docs/local_site/index.html", "r") as file:
        html_content = file.read()
    components.html(html_content, height=800, width=1000, scrolling=True)
    st.download_button(
        label="Download validation report",
        data=html_content.encode("utf-8"),
        file_name="vlidation_report.html",
        mime="text/html"
    )

        
def profile_data(df):
    profile = pr(df, explorative=True)
    st.write("Data Summary:")
    st.title("Pandas Profiling Report")
    # st_profile_report(profile)
    profile_html = profile.to_html()
    components.html(profile_html, height=800, width=800, scrolling=True)
    st.download_button(
        label="Download profiling report",
        data=profile_html.encode("utf-8"),
        file_name="profiling_report.html",
        mime="text/html"
    )
        
        
def process_file(uploaded_file, datatype_option):
    with open(datatype_option.lower() + '_columns.txt', 'r') as file:
        column_names = [line.strip() for line in file]
    if uploaded_file.name.split('.')[1].lower() == "csv":
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    df.columns=column_names
    if datatype_option == 'Monthly':
        date_type_columns=['Monthly Reporting Period','Defect Settlement Date','Zero Balance Effective Date','Due Date of Last Paid Installment (DDLPI)']
    else:
        date_type_columns=['First Payment Date','Maturity Date']
    for date_type_column in date_type_columns:
        df[date_type_column] = pd.to_datetime(df[date_type_column]).dt.strftime('%Y%m')
    return df
        
        
st.title("Freddie mac single family dataset quality evaluation and summarization")
st.write("Please upload the dataset in csv or xls file format and indicate if it is Origination/Monthly performance data")

datatype_option = st.selectbox("Select an option!", ('Origination', 'Monthly'))
uploaded_file = st.file_uploader("Please uplaod Freddie mac single family dataset for quality evaluation and summarization.", type=['csv','xls'])

if st.button("Submit"):
    if uploaded_file is None:
        st.error("Please upload " + datatype_option +  " dataset in csv or xls format.")
    else:
        filename = uploaded_file.name
        df=process_file(uploaded_file, datatype_option)
        profile_data(df)
        validate_data(df, datatype_option, filename)