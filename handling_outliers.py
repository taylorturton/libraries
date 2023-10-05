import numpy as np

# Pitstop times data
pitstop_times = [2.83, 2.91, 3.03, 3.20, 3.10, 2.98, 3.56, 3.73, 685.32, 3.42]

# Set a threshold (e.g., 30 seconds) to identify outliers
threshold = 30.0

# Remove outliers (values exceeding the threshold)
filtered_times = [time for time in pitstop_times if time <= threshold]

# Calculate the mean pitstop time for the filtered data
mean_pitstop_time = np.mean(filtered_times)

# Print the filtered pitstop times and mean pitstop time
print("Filtered Pitstop Times (without outliers):")
print(filtered_times)
print("\nMean Pitstop Time (after removing outliers):", mean_pitstop_time)
