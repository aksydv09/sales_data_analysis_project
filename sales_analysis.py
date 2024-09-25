import pandas as pd

# Create sample sales data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Product': ['Product_A', 'Product_B', 'Product_C', 'Product_D'] * 25,
    'Sales': [100, 150, 200, 250] * 25,
    'Quantity': [1, 2, 3, 4] * 25,
    'Category': ['Electronics', 'Furniture', 'Clothing', 'Accessories'] * 25
}

# Create DataFrame and save to CSV
sales_df = pd.DataFrame(data)
sales_df.to_csv('sales_data.csv', index=False)
print("Sample sales data created and saved to 'sales_data.csv'")
import pandas as pd

# Load sales data
df = pd.read_csv('sales_data.csv')

# Display first few rows
print(df.head())
print(df.describe())
import matplotlib.pyplot as plt
import seaborn as sns

# Plot total sales by product
plt.figure(figsize=(8, 6))
sns.barplot(x='Product', y='Sales', data=df)
plt.title('Total Sales by Product')
plt.show()
# Plot sales over time
df['Date'] = pd.to_datetime(df['Date'])
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Sales'])
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()
# Group by category and calculate total sales
sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()

# Plot sales by category
plt.figure(figsize=(8, 6))
sns.barplot(x='Category', y='Sales', data=sales_by_category)
plt.title('Total Sales by Category')
plt.show()
# Analyze product performance
product_performance = df.groupby('Product')[['Sales', 'Quantity']].sum().reset_index()

plt.figure(figsize=(8, 6))
sns.barplot(x='Product', y='Sales', data=product_performance)
plt.title('Sales by Product')
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='Product', y='Quantity', data=product_performance)
plt.title('Quantity Sold by Product')
plt.show()
