import os
import pandas as pd

project_dir = r"C:\Users\muhammad.farooqui\Downloads\Python\Churn-Rate"
os.chdir(project_dir)


# Load all sheets from Excel file
excel_file = 'Customer_Churn_Data_Large - Lloyds.xlsx'
sheets = pd.read_excel(excel_file, sheet_name=None)

# Access individual dataframes
df1 = sheets['Customer_Demographics']
df2 = sheets['Transaction_History']
df3 = sheets['Customer_Service']
df4 = sheets['Online_Activity']
df5 = sheets['Churn_Status']

# Or load specific sheets by name
df = pd.read_excel(excel_file, sheet_name=['Customer_Demographics', 'Transaction_History', 'Customer_Service', 'Online_Activity', 'Churn_Status'])

# Or load all sheets into a dictionary
all_sheets = pd.read_excel(excel_file, sheet_name=None)
for sheet_name, dataframe in all_sheets.items():
    print(f"Sheet: {sheet_name}")
    print(dataframe.head())