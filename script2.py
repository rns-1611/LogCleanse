import pandas as pd
import os
import warnings ; warnings.warn = lambda *args,**kwargs: None
from art import *

# Change the working directory to the current folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#print()
#tprint("LogCleanse")
#print()

# Prompt the user for input and store it in a variable
#csv_file = input('output.csv')
 
# Display the input back to the user
#print()
#print(f"You entered: {csv_file}")

# Load the CSV file into a DataFrame and read as a string
df = pd.read_csv('output.csv', header=None, dtype=str)

# Define the text to remove
rm1 = 'date='

# Remove the specific text from all cells
df = df.applymap(lambda x: x.replace(rm1, '') if isinstance(x, str) else x)

# Define the text to remove
rm2 = 'time='

# Remove the specific text from all cells
df = df.applymap(lambda x: x.replace(rm2, '') if isinstance(x, str) else x)

# Define the text to remove
rm3 = 'srcip='

# Remove the specific text from all cells
df = df.applymap(lambda x: x.replace(rm3, '') if isinstance(x, str) else x)

# Define the text to remove
rm4 = 'dstip='

# Remove the specific text from all cells
df = df.applymap(lambda x: x.replace(rm4, '') if isinstance(x, str) else x)

# Define the text to remove
rm5 = 'dstport='

# Remove the specific text from all cells
df = df.applymap(lambda x: x.replace(rm5, '') if isinstance(x, str) else x)

# Define the text to remove
rm6 = 'service='

# Remove the specific text from all cells
df = df.applymap(lambda x: x.replace(rm6, '') if isinstance(x, str) else x)

# Define the text to remove
rm7 = 'policyid='

# Remove the specific text from all cells
df = df.applymap(lambda x: x.replace(rm7, '') if isinstance(x, str) else x)

# Define the text to remove
rm8 = 'policyname='

# Remove the specific text from all cells
df = df.applymap(lambda x: x.replace(rm8, '') if isinstance(x, str) else x)

# Define the text to remove
rm9 = 'srcintf='

# Remove the specific text from all cells
df = df.applymap(lambda x: x.replace(rm9, '') if isinstance(x, str) else x)

# Define the text to remove
rm10 = 'dstintf='

# Remove the specific text from all cells
df = df.applymap(lambda x: x.replace(rm10, '') if isinstance(x, str) else x)

# Define the text to remove
rm11 = '"'

# Remove the specific text from all cells
df = df.applymap(lambda x: x.replace(rm11, '') if isinstance(x, str) else x)

# Specify the column titles
column_titles = ['Date', 'Source IP', 'Destination IP', 'Port', 'Service', 'Policy ID', 'Policy Name', 'Source Interface', 'Destination Interface']  # Adjust titles according to your needs

# Assign the titles to the DataFrame columns
df.columns = column_titles

# Remove duplicates rows
df = df.drop_duplicates()

# Remove duplicate columns
df = df.drop_duplicates(subset=None)

# Save the updated DataFrame to a new CSV file
df.to_csv('output.csv', index=False)

print("Log file cleansed successfully. Happy parsing! ;D")
print()
os.system('pause')