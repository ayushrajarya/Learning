import pandas as pd
import numpy as np

# Create a random DataFrame 
np.random.seed(0)
data = np.random.randn(5, 60)
df = pd.DataFrame(data)
print(df)
# Function to calculate mean values for each second
def calculate_second_means(row):
    # Split the row into chunks of 100 values (for 100 Hz sampling rate)
    chunks = [row[i:i+10] for i in range(0, len(row), 10)]
    
    # Calculate the mean for each chunk (second)
    mean_values_per_second = [chunk.mean() for chunk in chunks]
    
    return mean_values_per_second

rows = []

# Iterate through each row 
for index, row in df.iterrows():
    # Calculate the mean values for each second for a row
    mean_values_per_second = calculate_second_means(row)
    
    # Append the mean values for this row to the list
    rows.append(mean_values_per_second)

# Create the seconds_df DataFrame from the list of rows
seconds_df = pd.DataFrame(rows)

# seconds_df contains the mean values for each second for all rows
seconds_df.columns = [f'Second_{i+1}' for i in range(len(seconds_df.columns))]

# Display result
print(seconds_df)