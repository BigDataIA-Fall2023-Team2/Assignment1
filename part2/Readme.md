# Assignment 1 - Part 2 (Data Profiling and Validation)

### Project Descrition ###
Using Pandas data profiling to generate a data profiling report and using great expectations to validate the same. The data here used as an input file from https://freddiemac.embs.com/. 

### Application Link ###
https://t2p2a1.streamlit.app/

### Project Resources ###

https://codelabs-preview.appspot.com/?file_id=1I9T3brvdH5yQdfWt2GJ58brCZilZj-V2mS75mKyq3-w#3


### Tech Stack ###
Python | Streamlit | Great Expectations | Pandas profiling

### Architecture diagram ###

![image](https://github.com/BigDataIA-Fall2023-Team2/Assignment1/assets/131703516/19a6bf44-b491-4506-8673-5670ae1d30c3)

### Project Flow

The user uploads a csv/excel file from Freddieemac website and specifies what type of file it is - orgigination/monthly. The data will be then profiled using pandas profiling and validated using great expectations (python suite). A datadoc will be generated that will show case the data validation results.

### Code Explaination

There are two important files - expectation_suits_builder.py and home.py. The expectation_suits_builder.py is used for generating the great expectation suit and home.py is used for showcasing the validation results of great expectation and generating data profling report of the uploaded excel/csv. Apart from that there is an expectation.json file that we are using that contains all the required expectations in json format. 

***expectation_suits_builder.py***

```
from great_expectations.core.expectation_configuration import ExpectationConfiguration
from great_expectations.data_context import FileDataContext
from great_expectations.core.expectation_configuration import ExpectationConfiguration
import json

with open("expectations.json", "r") as expectations_file:
    expectations = json.load(expectations_file)
    
context = FileDataContext.create(project_root_dir="./.")
datasource = context.sources.add_pandas("pandas_dataframe_datasource")

```
In the above code, we are loading our expectations written in json format from expectation.json and creating a data source 

```
origination_expectations_suite = context.create_expectation_suite("origination_expectations_suite")
with open('origination_columns.txt', 'r') as file:
    column_names = [line.strip() for line in file]
ordered_list_origination_expectation_configuration = ExpectationConfiguration(
    expectation_type="expect_table_columns_to_match_ordered_list",
    kwargs={
        "column_list": column_names
    },
)
origination_expectations_suite.add_expectation(expectation_configuration=ordered_list_origination_expectation_configuration)
for column in column_names:
    not_null_origination_expectation_configuration = ExpectationConfiguration(
        expectation_type="expect_column_values_to_not_be_null",
        kwargs={
            "column": column
        },
    )
    origination_expectations_suite.add_expectation(not_null_origination_expectation_configuration)

for expectation in expectations['origination_expectations']:
    if 'meta' not in expectation:
        expectation_config = ExpectationConfiguration(
                expectation_type=expectation['expectation_type'],
                kwargs=expectation['kwargs']
        )
    else:
        expectation_config = ExpectationConfiguration(
                expectation_type=expectation['expectation_type'],
                kwargs=expectation['kwargs'],
                meta=expectation["meta"]
        )
    origination_expectations_suite.add_expectation(expectation_config)
context.save_expectation_suite(origination_expectations_suite)

```
In the above part, we are creating an expectation suite for origination data. We are also checking 2 things hereitself :

a) If the schema is correct by verifying if the column names mentioned in the data set are in the same order of the file that contains the column names mentioned in the column.txt file. This is done using expectation_type="expect_table_columns_to_match_ordered_list"

b) Checking if any of the columns contain null values by using expectation_type="expect_column_values_to_not_be_null"

In later part of the code we are then creating the expectations inside the expectation suite. We are loading the expectations that were present in the json file. We are checking if they contain any extra paramter of 'meta', if so we store keys {meta, expectation type and kwargs} else we just store the keys {expectation type and kwargs}. We are then saving the expectation suite inside the data context.


The same approach is being done for monthly data also as you can see in below code:
```
monthly_expectations_suite = context.create_expectation_suite("monthly_expectations_suite")
with open('monthly_columns.txt', 'r') as file:
    column_names = [line.strip() for line in file]
ordered_list_monthly_expectation_configuration = ExpectationConfiguration(
    expectation_type="expect_table_columns_to_match_ordered_list",
    kwargs={
        "column_list": column_names
    },
)
monthly_expectations_suite.add_expectation(expectation_configuration=ordered_list_monthly_expectation_configuration)
for column in column_names:
    not_null_origination_expectation_configuration = ExpectationConfiguration(
        expectation_type="expect_column_values_to_not_be_null",
        kwargs={
            "column": column
        },
    )
    monthly_expectations_suite.add_expectation(not_null_origination_expectation_configuration)
for expectation in expectations['monthly_expectations']:
    if 'meta' not in expectation:
        expectation_config = ExpectationConfiguration(
                expectation_type=expectation['expectation_type'],
                kwargs=expectation['kwargs']
        )
    else:
        expectation_config = ExpectationConfiguration(
                expectation_type=expectation['expectation_type'],
                kwargs=expectation['kwargs'],
                meta=expectation["meta"]
        )
    monthly_expectations_suite.add_expectation(expectation_config)
context.save_expectation_suite(monthly_expectations_suite)

```



***Home.py***


```
import os,re,uuid
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from ydata_profiling import ProfileReport as pr
import great_expectations as gx

st.title("Freddie mac single family dataset quality evaluation and summarization")
st.write("Please upload the dataset in csv or xls file format and indicate if it is Origination/Monthly performance data")

datatype_option = st.selectbox("Select an option!", ('Origination', 'Monthly'))
uploaded_file = st.file_uploader("Please uplaod Freddie mac single family dataset for quality evaluation and summarization.", type=['csv','xls'])

profiling = st.checkbox('Profile Data')
validation = st.checkbox('Validate Data')

if st.button("Submit"):
    if uploaded_file is None:
        st.error("Please upload " + datatype_option +  " dataset in csv or xls format.")
    else:
        filename = uploaded_file.name
        df=process_file(uploaded_file, datatype_option)
        if profiling is True:
            profile_data(df)
        if validation is True:
            validate_data(df, filename, datatype_option)
        

```
We are asking to upload csv/excel file from FreddieMac's website and then process_file function is being called. Below is the code for the same.

```
def process_file(uploaded_file, datatype_option):
    if os.getcwd() != "/mount/src/assignment1/part2":  #added to fix the directory issue on streamlit cloud deployment
        os.chdir("/mount/src/assignment1/part2")
    with open("./"+datatype_option.lower() + '_columns.txt', 'r') as file:
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
```

Here, the file is being mounted to streamcloud directory instead of saving locally on users computer. The data is first loaded into dataframe and then the column names from columns.txt file is being added into the dataframe. Based on the datatype option of monthly or organizational, the data type of the date columns is being set. The date columns are explictly mentioned for each type (monthly or organizational) for converting their datatype to date format.

 
The user selects if he wants to profile or validate or both with the help of st.checkbox(). After clicking on submit button, if profiling checkbox is checked, then  function is called and below is the code for the same.

```
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
```

Here the pandas profiling is being used for the function pr and it is being converted into HTML. It can be downloaded using download button. 

```
def validate_data(df, filename, datatype_option):
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
    checkpoint_result = checkpoint.run(run_name="validation_result")
    context.build_data_docs()
    html_file_name = "pandas_dataframe_datasource-" + asset_name + ".html"
    pattern = re.compile(fr'.*/(\d{{8}}T\d{{6}}\.\d{{6}}Z)/{re.escape(html_file_name)}$')
    root_dir = "./gx/uncommitted/data_docs/local_site/validations/"+ datatype_option.lower() +"_expectations_suite/validation_result"
    for root, dirs, files in os.walk(root_dir):
        for name in files:
            full_path = os.path.join(root, name)
            if name == html_file_name:
                with open(full_path, "r") as file:
                    html_content = file.read()
                components.html(html_content, height=800, width=1000, scrolling=True)
                st.download_button(
                    label="Download validation report",
                    data=html_content.encode("utf-8"),
                    file_name="validation_report.html",
                    mime="text/html"
                )
        

```
The above code is being used for validating the data using great expectations. Here the data context directory path is being given by specifying gx.data_context.DataContext("./gx"). The datasource is from expectation_builder.py file is being fetched here. Then the dataset, assetname, batchrequest is being specified. After this a checkpoint is defined along with validations where in the expectation suit is being defined from expectation_builder.py. After the checkpoint is saved, the checkpoint is executed and the results are stored. Using data docs, the results are being rendered using HTML pages and the option to download the HTML page is shown using download button.


### Repo Structure

![image](https://github.com/BigDataIA-Fall2023-Team2/Assignment1/assets/131703516/9d416138-d5be-4cfb-af97-929f35874263)




### Contributions

| Name                            | Contribution                  |  
| ------------------------------- | ------------------------------|
| Dhawal Negi                     | Data Profiling               |
| Dhawal Negi                     | Expectation Suite validation  |
| Chinmay Gandi, Shardul Chavan   | Expectation Suite expectations| 
