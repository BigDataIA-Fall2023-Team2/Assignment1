from great_expectations.core.expectation_configuration import ExpectationConfiguration
from great_expectations.data_context import FileDataContext
from great_expectations.core.expectation_configuration import ExpectationConfiguration
import json
import os, shutil

if os.path.exists("./gx") and os.path.isdir("./gx"):
    shutil.rmtree("./gx")

with open("expectations.json", "r") as expectations_file:
    expectations = json.load(expectations_file)
    
context = FileDataContext.create(project_root_dir="./.")
datasource = context.sources.add_pandas("pandas_dataframe_datasource")

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

