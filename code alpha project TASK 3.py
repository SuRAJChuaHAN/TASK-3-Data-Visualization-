#  TASK 3: Data Visualization 
# ● Transform raw data into visual formats like charts, graphs, and dashboards. 
# ● Use tools like Matplotlib, Seaborn, or Tableau for creating visuals. 
# ● Design visuals that enhance understanding and reveal insights clearly. 
# ● Craft compelling data stories that support decision-making. 
# ● Build a strong portfolio with impactful and well-designed visualizations. 

import pandas as pd

# Load the Excel file
df = pd.read_excel("C:\\Users\\DELL\\Desktop\\suraj project ..xlsx")

# Quick cleanup for column names
df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('(USD)', 'USD').str.replace('(', '').str.replace(')', '')

import matplotlib.pyplot as plt

# Convert Order_Date to datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Group by Order Date
daily_sales = df.groupby('Order_Date')['Total_USD'].sum()

# Plotting
plt.figure(figsize=(12,6))
daily_sales.plot(kind='line', marker='o', color='steelblue')
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Revenue (USD)")
plt.grid(True)
plt.tight_layout()
plt.show()

# top customers by total sales

top_customers = df.groupby('Customer_Name')['Total_USD'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_customers.plot(kind='barh', color='teal')
plt.title("Top 10 Customers by Sales")
plt.xlabel("Total Sales (USD)")
plt.ylabel("Customer Name")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

#Price vs Quantity Purchased (Trend Analysis)
import seaborn as sns

plt.figure(figsize=(10,6))
sns.regplot(data=df, x='Retail_Price_USD', y='Order_Quantity', scatter_kws={'s': 40}, line_kws={'color': 'red'})
plt.title("Retail Price vs Order Quantity")
plt.xlabel("Retail Price (USD)")
plt.ylabel("Order Quantity")
plt.tight_layout()
plt.show()


# Pie Chart: Sales Contribution by Custome
import matplotlib.pyplot as plt

# Aggregate total sales per customer
customer_sales = df.groupby('Customer_Name')['Total_USD'].sum().sort_values(ascending=False)

# Optional: Take top 10 contributors
top_10 = customer_sales.head(10)

# Create pie chart
plt.figure(figsize=(8,8))
plt.pie(top_10, labels=top_10.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title("Top 10 Customers by Sales Contribution")
plt.axis('equal')  # Ensures the pie is circular
plt.tight_layout()
plt.show()