import numpy as np

# Create a sample dataset
data = np.array([10, 15, 20, 25, 30])

# Calculate mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data)

print("Original Data:")
print(data)
print(f"Mean: {mean}")
print(f"Standard Deviation: {std_dev}")

# Min-Max Scaling
min_val = np.min(data)
max_val = np.max(data)

scaled_data = (data - min_val) / (max_val - min_val)

print("\nMin-Max Scaled Data:")
print(scaled_data)
