import pandas as pd
import pandas as pd
import streamlit as st

from ydata_profiling import ProfileReport as pr
from streamlit_pandas_profiling import st_profile_report

# change the sheet name as per data being processed
sheet_name="Origination"
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
    if data_type_format.startswith("Numeric"):
        # Split the format into parts
        parts = data_type_format.split('-')
        
        if len(parts) == 2:
            # Extract precision and scale if available
            precision, scale = map(int, parts[1].split(','))
            dtype_dict[attribute_name] = f"float({precision},{scale})"
        else:
            # If precision and scale are not specified, set as "int"
            dtype_dict[attribute_name] = "int"

    # Check if the data type is "Alpha" and set to "str"
    elif "Alpha" or "Alpha Numeric" or " Alpha-Numeric" in data_type_format:
        dtype_dict[attribute_name] = "str"
    else:
        # If neither "Numeric" nor "Alpha," you can handle other cases here
        dtype_dict[attribute_name] = data_type_format

# Now, dtype_dict contains the attribute names as keys and their data types & formats as values
print(dtype_dict)

# Change the file name before writing the txt file 
with open('origination_dtypes.txt','w') as data: 
      data.write(str(dtype_dict))

