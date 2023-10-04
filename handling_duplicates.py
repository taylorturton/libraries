import pandas as pd

# Create a sample dataset with duplicates
data = pd.DataFrame({
    'TransactionID': [1, 2, 3, 4, 4, 3],
    'CustomerID': [1, 2, 1, 1, 1, 1],
    'Amount': [10, 20, 15, 5, 25, 15]
})

# Display the original dataset
print("Original Dataset:")
print(data)

# Detecting Duplicates
duplicate_rows = data[data.duplicated()]
print("\nDuplicate Rows:")
print(duplicate_rows)

# Removing Exact Duplicates
data.drop_duplicates(inplace=True)

# Handling Partial Duplicates (Keeping the first occurrence)
partial_duplicates = data[data.duplicated(subset=['TransactionID', 'CustomerID'], keep='first')]
print("\nPartial Duplicates (Keeping the first occurrence):")
print(partial_duplicates)

# Aggregating Data (Sum of Amount)
aggregated_data = data.groupby('CustomerID')['Amount'].sum().reset_index()
print("\nAggregated Data (Sum of Amount by CustomerID):")
print(aggregated_data)
