import numpy as np
import matplotlib.pyplot as plt

# Generate random test scores for 20 students (values between 0 and 100)
np.random.seed(0)  # Setting a random seed for reproducibility
test_scores = np.random.randint(0, 101, 20)

# Calculate statistics
mean_score = np.mean(test_scores)
median_score = np.median(test_scores)
std_deviation = np.std(test_scores)

# Define custom bin intervals
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Visualize the data with a histogram using custom bins
plt.hist(test_scores, bins=bins, edgecolor='k')
plt.title('Test Scores Distribution')
plt.xlabel('Test Scores')
plt.ylabel('Frequency')
plt.show()

# Print summary statistics
print("Test Scores:", test_scores)
print("Mean Score:", mean_score)
print("Median Score:", median_score)
print("Standard Deviation:", std_deviation)
