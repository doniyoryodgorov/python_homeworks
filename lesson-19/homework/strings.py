TASK 1
# 1.1
category_stats = df.groupby('Category').agg(
    total_quantity=('Quantity', 'sum'),
    average_price=('Price', 'mean'),
    max_quantity_single_transaction=('Quantity', 'max')
)
# 1.2

top_products = (
    df.groupby(['Category', 'Product'])
      ['Quantity'].sum()
      .reset_index()
)

# 1.3
top_selling_products = top_products.loc[top_products.groupby('Category')['Quantity'].idxmax()]

TASK 2
import pandas as pd
df=pd.read_csv('customer_orders.csv')

# 1 Group the data by CustomerID and filter out customers who have made less than 20 orders.
customer_orders = df.groupby('CustomerID').filter(lambda x: len(x) >= 20)
customer_orders

# 2 Identify customers who have ordered products with an average price per unit greater than $120.
average_price_per_unit = df.groupby('CustomerID')['Price'].mean()
average_price_per_unit = average_price_per_unit[average_price_per_unit > 120]

# 3 Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.
product_stats = df.groupby('Product').agg(
total_quantity=('Quantity', 'sum'),
total_price=('Price', 'sum')
)
product_stats = product_stats[product_stats['total_quantity'] >= 5]
product_stats



