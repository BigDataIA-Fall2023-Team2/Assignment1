import pandas as pd
import pandas as pd
import streamlit as st

from ydata_profiling import ProfileReport as pr
from streamlit_pandas_profiling import st_profile_report
sheet_name="Monthly"
# Load the Excel file into a DataFrame
df = pd.read_excel('/home/shardulc/DAMG7245/Assignment1/Part-2/streamlit/file_layout.xlsx',sheet_name = sheet_name, skiprows=1)

print(df.head)


# Create a dictionary to store the attribute names and their data types
dtype_dict = {}

# Iterate through the rows of the DataFrame and populate the dictionary
for index, row in df.iterrows():
    attribute_name = row['ATTRIBUTE NAME']

    data_type_format = row['DATA TYPE & FORMAT']
    dtype_dict[attribute_name] = data_type_format
    
    # Check if the data type is "Numeric" and set to "int"
    if "Numeric" in data_type_format:
        dtype_dict[attribute_name] = "int"
    # Check if the data type is "Alpha" and set to "str"
    elif "Alpha" in data_type_format:
        dtype_dict[attribute_name] = "str"
    else:
        # If neither "Numeric" nor "Alpha," you can handle other cases here
        dtype_dict[attribute_name] = data_type_format

# Now, dtype_dict contains the attribute names as keys and their data types & formats as values
print(dtype_dict)

  
with open('monthly_dtypes.txt','w') as data: 
      data.write(str(dtype_dict))

# file_path = '/home/shardulc/DAMG7245/ydataProfile/sample_orig_2021.csv'
# df = pd.read_csv(file_path, dtype=dtype_dict)
# print(df.head(10))

# profile = pr(df,tsmode=True, ,explorative=True)

# profile = ProfileReport(df, title="Profiling Report",explorative=True)