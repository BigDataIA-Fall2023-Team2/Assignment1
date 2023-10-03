import great_expectations as gx
from great_expectations.core.expectation_configuration import ExpectationConfiguration
import pandas as pd
import json
import os
import subprocess


subprocess.run(["great_expectations", "init"], cwd='./.')   
context = gx.data_context.DataContext("./gx")
datasource_config = {
        "name": "my_datasource",
        "class_name": "PandasDatasource",
        "data_asset_type": {
            "class_name": "PandasDataset"
        },
        "batch_kwargs_generators": {}
    }
context.add_datasource(**datasource_config)

with open("expectations.json", "r") as expectations_file:
    expectations = json.load(expectations_file)
    
origination_expectations_suite = context.create_expectation_suite("origination_expectations_suit")

for expectation in expectations['origination_expectations']:
    column = expectation['column']
    expectation_type = expectation['expectation_type']
    kwargs = expectation['kwargs']
    expectation_config = ExpectationConfiguration(
            expectation_type=expectation_type,
            kwargs={"column": column, **kwargs}
    )
    origination_expectations_suite.add_expectation(expectation_config)

# with open('origination_columns.txt', 'r') as file:
#     column_names = [line.strip() for line in file]
# valid_column_order_expecation = ExpectationConfiguration(
#     expectation_type="expect_table_columns_to_match_ordered_list",
#     kwargs={
#         "column_list": column_names}
# )
# origination_expectations_suit.add_expectation(valid_column_order_expecation)
context.save_expectation_suite(origination_expectations_suite, "origination_expectations_suit.json")

# monthly_expectations_suite = context.create_expectation_suite("monthly_expectations_suit")

# for expectation in expectations['monthly_expectations']:
#     print(expectation)
#     column = expectation['column']
#     expectation_type = expectation['expectation_type']
#     kwargs = expectation['kwargs']
#     expectation_config = ExpectationConfiguration(
#             expectation_type=expectation_type,
#             kwargs={"column": column, **kwargs}
#     )
#     origination_expectations_suite.add_expectation(expectation_config)

# # with open('monthly_columns.txt', 'r') as file:
# #     column_names = [line.strip() for line in file]
# # valid_column_order_expecation = ExpectationConfiguration(
# #     expectation_type="expect_table_columns_to_match_ordered_list",
# #     kwargs={
# #         "column_list": column_names}
# # )
# # monthly_expectations_suit.add_expectation(valid_column_order_expecation)
# context.save_expectation_suite(monthly_expectations_suite, "monthly_expectations_suit.json")
