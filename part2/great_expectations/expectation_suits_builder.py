import great_expectations as gx
from great_expectations.core.expectation_configuration import ExpectationConfiguration
import pandas as pd
import json

context = gx.data_context.FileDataContext.create("fredie_mac_expectations")

with open("expectations.json", "r") as expectations_file:
    expectations = json.load(expectations_file)
    
origination_expectations_suit = context.add_or_update_expectation_suite("origination_expectations_suit")

origination_expectations_suit.expectations = expectations['origination_expectations']

with open('origination_columns.txt', 'r') as file:
    column_names = [line.strip() for line in file]
valid_column_order_expecation = ExpectationConfiguration(
    expectation_type="expect_table_columns_to_match_ordered_list",
    kwargs={
        "column_list": column_names}
)

origination_expectations_suit.append(valid_column_order_expecation)
context.save_expectation_suite(origination_expectations_suit, overwrite=True)

monthly_expectations_suit = context.add_or_update_expectation_suite("monthly_expectations_suit")

monthly_expectations_suit.expectations = expectations['monthly_expectations']

with open('monthly_columns.txt', 'r') as file:
    column_names = [line.strip() for line in file]
valid_column_order_expecation = ExpectationConfiguration(
    expectation_type="expect_table_columns_to_match_ordered_list",
    kwargs={
        "column_list": column_names}
)

monthly_expectations_suit.append(valid_column_order_expecation)
context.save_expectation_suite(monthly_expectations_suit, overwrite=True)