import numpy as np

# Create NumPy arrays for weights (in kg) and heights (in meters)
weights_kg = np.array([58, 83, 78, 68, 75])
heights_m = np.array([1.75, 1.82, 1.84, 1.75, 1.88])

# Calculate BMI for each individual
bmi = weights_kg / (heights_m ** 2)

# Print the BMI values
print("Weights (kg):", weights_kg)
print("Heights (m):", heights_m)
print("BMI Values:", bmi)
