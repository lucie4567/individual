import pandas as pd

# File uploader to upload Excel file
df= pd.read_excel(r"C:\Users\Lucka\Downloads\survey-data-skills (2).xlsx")
df.head()
import pandas as pd

# Assuming df is your existing DataFrame
# Define the index ranges for the columns to combine
start1, end1 = 7, 66
start2, end2 = 67, 126

# Create a new DataFrame for combined questions
combined_df = df.iloc[:, :6].copy()  # Keep the first 6 columns (assuming they are identifiers)

# Combine the questions from columns 7-66 and 67-126 starting from the 7th row
for i in range(start1, end1 + 1):
    question_text = df.columns[i]
    corresponding_index = i + (start2 - start1)
    if corresponding_index < df.shape[1]:
        combined_column = df.iloc[:, i].combine_first(df.iloc[:, corresponding_index])
    else:
        combined_column = df.iloc[:, i]
    combined_df[question_text] = combined_column

# Save the new DataFrame to a new Excel file
output_path = r"C:\Users\Lucka\Downloads\skills_data.xlsx"  # Update with the desired output file path
combined_df.to_excel(output_path, index=False)

print("Combined survey data saved to:", output_path)
combined_df.head()
import streamlit as st
# Title of the app
st.title("individual portfolio")
