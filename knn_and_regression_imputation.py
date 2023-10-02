import pandas as pd
import numpy as np
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.impute import KNNImputer

# Create a sample dataset with missing values
data = pd.DataFrame({
    'Age': [25, 32, None, 40, None, 50, 28],
    'Income': [45000, None, 55000, None, 60000, None, 70000]
})

# Display the original dataset
print("Original Dataset:")
print(data)

# Imputation using both KNN and regression
methods = {'KNN': KNNImputer(n_neighbors=2), 'Regression': HistGradientBoostingRegressor()}
imputed_data = data.copy()

for col in data.columns:
    missing = data[col].isnull()
    for method_name, imputer in methods.items():
        temp_data = data.copy()
        if method_name == 'KNN':
            temp_data[col] = imputer.fit_transform(data[[col]])
        else:  # For Regression imputation
            known = ~missing
            X = data[known][['Age']]
            y = data[known][col]
            imputer.fit(X, y)
            temp_data[col] = imputer.predict(data[['Age']])
        imputed_data[method_name + '_' + col] = temp_data[col]

# Display the imputed datasets for both methods
print("\nImputed Datasets:")
print(imputed_data)
