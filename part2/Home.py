import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport as pr
from streamlit_pandas_profiling import st_profile_report
import great_expectations as gx
from great_expectations.checkpoint import SimpleCheckpoint
from great_expectations.core.batch import Batch, BatchRequest, RuntimeBatchRequest
from great_expectations.validator.validator import Validator
from great_expectations.execution_engine import PandasExecutionEngine
import json
import yaml

# from great_expectations.data_context import DataContext


st.title("Freddie mac single family dataset quality evaluation and summarization")
st.write("Please upload the dataset in csv or xls file format and indicate if it is Origination/Monthly performance data")

# Upload a file
datatype_option = st.selectbox("Select an option!", ('Origination', 'Monthly'))
uploaded_file = st.file_uploader("Please uplaod Freddie mac single family dataset for quality evaluation and summarization.", type=['csv','xls'])



if st.button("Submit"):
    if uploaded_file is None:
        st.error("Please upload " + datatype_option +  " dataset in csv or xls format.")
        exit()
    else:
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
        st.write(df.head(5))
        
        # suite = context.get_expectation_suite(origination_expectations_suit)  # Replace with your suite name
        # is_running = suite.is_expectation_suite_configured()
        # if is_running:
        #     st.success("Great Expectations expectations are running.")
        # else:
        #     st.error("Great Expectations expectations are not configured.")


        # profile = pr(df, explorative=True)
        # st.write("Data Summary:")
        # st.title("Pandas Profiling Report")
        # st_profile_report(profile)
        
        
        context = gx.data_context.DataContext("./gx/")
        execution_engine = PandasExecutionEngine()
        expectation_suite = context.get_expectation_suite("origination_expectations_suit.json")
        batch = Batch(
            data=df,
            batch_request={
                "datasource_name": "temporary",
                "data_connector_name": "default_inferred_data_connector_name",
                "data_asset_name": "temp_asset",
                "partition_request": {
                    "batch_identifiers": {
                        "id": "temporary"
                    }
                },
                "expectation_suite_name": "origination_expectations_suit"  # Include this line
            }
        )
        validator = Validator(
            execution_engine=execution_engine,
            batches=(batch,),
            expectation_suite=expectation_suite,
        )
        results = validator.validate()

        results_json_str = json.dumps(results.to_json_dict(), indent=4)
        st.write(results_json_str)
        st.download_button(
            label="Download Results",
            data=results_json_str,
            file_name='validation_results.json',
            mime='application/json'
        )
        
        context.build_data_docs()
        context.open_data_docs()
