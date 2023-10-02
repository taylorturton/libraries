import pandas as pd
import numpy as np

# Create a sample dataset with missing values
data = pd.DataFrame({
    'Age': [25, 32, None, 40, None, 50, 28],
    'Income': [45000, None, 55000, None, 60000, None, 70000]
})

# Display the original dataset
print("Original Dataset:")
print(data)

# Create separate copies for each imputation method
mean_imputed_data = data.copy()
median_imputed_data = data.copy()
mode_imputed_data = data.copy()

# Mean Imputation
mean_age = mean_imputed_data['Age'].mean()
mean_income = mean_imputed_data['Income'].mean()
mean_imputed_data['Age'].fillna(mean_age, inplace=True)
mean_imputed_data['Income'].fillna(mean_income, inplace=True)

# Median Imputation
median_age = median_imputed_data['Age'].median()
median_income = median_imputed_data['Income'].median()
median_imputed_data['Age'].fillna(median_age, inplace=True)
median_imputed_data['Income'].fillna(median_income, inplace=True)

# Mode Imputation
mode_age = mode_imputed_data['Age'].mode().values[0]
mode_income = mode_imputed_data['Income'].mode().values[0]
mode_imputed_data['Age'].fillna(mode_age, inplace=True)
mode_imputed_data['Income'].fillna(mode_income, inplace=True)

# Display the imputed datasets for all three methods
print("\nImputed Dataset (Mean Imputation):")
print(mean_imputed_data)

print("\nImputed Dataset (Median Imputation):")
print(median_imputed_data)

print("\nImputed Dataset (Mode Imputation):")
print(mode_imputed_data)
