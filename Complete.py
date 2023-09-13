# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace 'dataset.csv' with your dataset file)
df = pd.read_csv('G:\Projects\Explanatory Data Analysis\dataset.csv')

# Display basic information about the dataset
print("Dataset Info:")
print(df.info())

# Display the first few rows of the dataset
print("\nFirst 5 Rows of the Dataset:")
print(df.head())

# Summary statistics of numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Visualize data patterns

# Distribution of house prices
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], bins=30, kde=True)
plt.title('Distribution of House Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Relationship between the number of bedrooms and house prices
plt.figure(figsize=(10, 6))
sns.boxplot(x='Bedrooms', y='Price', data=df)
plt.title('House Prices by Number of Bedrooms')
plt.xlabel('Bedrooms')
plt.ylabel('Price')
plt.show()

# Correlation heatmap
plt.figure(figsize=(12, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# Pairplot to explore relationships between numerical variables
sns.pairplot(df[['Price', 'SqFt', 'Bedrooms', 'Bathrooms']])
plt.show()
