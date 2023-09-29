import pandas as pd

# Load an existing dataset from a CSV file
data = pd.read_csv('your_dataset.csv')

# Display the original DataFrame
print("Original DataFrame:")
print(data)

# Remove rows with missing data
data_cleaned = data.dropna()

# Display the cleaned DataFrame
print("\nDataFrame after removing rows with missing data:")
print(data_cleaned)
