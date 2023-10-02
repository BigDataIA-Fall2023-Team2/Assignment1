import great_expectations as gx
from great_expectations.core.expectation_configuration import ExpectationConfiguration
import pandas as pd
import json

context = gx.data_context.FileDataContext.create("CheckOriginationContext")
suite = context.add_or_update_expectation_suite("check_origination_suite")

with open("origination_expectation.json", "r") as expectation_file:
    expectations = json.load(expectation_file)
suite.expectations = expectations['expectations']

with open('origination_columns.txt', 'r') as file:
    column_names = [line.strip() for line in file]
valid_column_order_expecation = ExpectationConfiguration(
    expectation_type="expect_table_columns_to_match_ordered_list",
    kwargs={
        "column_list": column_names}
)

suite.append_expectation(valid_column_order_expecation)

context.save_expectation_suite(suite, overwrite=True)








