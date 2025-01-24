# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('../data/raw/data.csv')

# Overview of the Data
print("Dataset Overview:")
print(f"Number of rows: {data.shape[0]}")
print(f"Number of columns: {data.shape[1]}")
print("\nData Types:")
print(data.dtypes)

# Summary Statistics
print("\nSummary Statistics:")
print(data.describe())

# Distribution of Numerical Features
numerical_features = data.select_dtypes(include=[np.number]).columns
for feature in numerical_features:
    plt.figure(figsize=(10, 6))
    sns.histplot(data[feature], kde=True)
    plt.title(f'Distribution of {feature}')
    plt.show()

# Distribution of Categorical Features
categorical_features = data.select_dtypes(include=[object]).columns
for feature in categorical_features:
    plt.figure(figsize=(10, 6))
    sns.countplot(y=data[feature], order=data[feature].value_counts().index)
    plt.title(f'Distribution of {feature}')
    plt.show()

# Correlation Analysis
plt.figure(figsize=(12, 8))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# Identifying Missing Values
missing_values = data.isnull().sum()
print("\nMissing Values:")
print(missing_values[missing_values > 0])

# Outlier Detection
for feature in numerical_features:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=data[feature])
    plt.title(f'Box Plot of {feature}')
    plt.show()