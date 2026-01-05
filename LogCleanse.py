import subprocess
import pandas as pd
import os
import warnings ; warnings.warn = lambda *args,**kwargs: None
from art import *

# Your code before running the second script
def first_part():
    print("This is the first part of the script.")
    # Any other code goes here
    
# Change the working directory to the current folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print()
tprint("LogCleanse")
print()

# Prompt the user for input and store it in a variable
csv_file = input("Please enter the filename for the .csv: ")
 
# Display the input back to the user
print()
print(f"You entered: {csv_file}")

# Load the CSV file
df = pd.read_csv(csv_file)

# Search for columns that contain specific text
date_column = [col for col in df.columns if 'date=' in col]
srcip_column = [col for col in df.columns if 'srcip=' in col]
dstip_column = [col for col in df.columns if 'dstip=' in col]
dstport_column = [col for col in df.columns if 'dstport=' in col]
service_column = [col for col in df.columns if 'service=' in col]
policyid_column = [col for col in df.columns if 'policyid=' in col]
policyname_column = [col for col in df.columns if 'policyname=' in col]
srcintf_column = [col for col in df.columns if 'srcintf=' in col]
dstintf_column = [col for col in df.columns if 'dstintf=' in col]

# Identify the remaining columns that do not match any of the above
remaining_columns = [col for col in df.columns if col not in (date_column + srcip_column + dstip_column + dstport_column + service_column + policyid_column + policyname_column + srcintf_column + dstintf_column)]

# Define the new column order: first sourceip=, then destport=, then srvport=, then policy=, and then the rest
new_column_order = date_column + srcip_column + dstip_column + dstport_column + service_column + policyid_column + policyname_column + srcintf_column + dstintf_column

# Reorder the DataFrame's columns
df_reordered = df[new_column_order]

# Save the reordered DataFrame to a new CSV file
df_reordered.to_csv('output.csv', index=False)

# Run the second Python script near the bottom
def run_another_script():
    print()
    # Using subprocess to call another Python script
    subprocess.run(["python", "script2.py"])

# Call the function to run the second script
run_another_script()