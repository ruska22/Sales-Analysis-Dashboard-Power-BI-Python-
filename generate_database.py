import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
Faker.seed(42)
np.random.seed(42)

# Number of rows
n_rows = 5_000_000

# Generate Order IDs
order_ids = np.arange(1, n_rows + 1)

# Generate dates within 2 years
dates = pd.to_datetime(np.random.randint(
    pd.Timestamp('2022-01-01').value // 10**9,
    pd.Timestamp('2023-12-31').value // 10**9,
    n_rows), unit='s')

# Product categories
categories = ['Electronics', 'Furniture', 'Clothing', 'Toys', 'Books', 'Groceries']

# Product names per category
products = {
    'Electronics': ['Laptop', 'Phone', 'Headphones', 'Camera', 'Monitor'],
    'Furniture': ['Chair', 'Desk', 'Couch', 'Table', 'Bookshelf'],
    'Clothing': ['Shirt', 'Pants', 'Jacket', 'Dress', 'Shoes'],
    'Toys': ['Lego', 'Doll', 'Puzzle', 'Action Figure', 'Board Game'],
    'Books': ['Novel', 'Textbook', 'Magazine', 'Comics', 'Notebook'],
    'Groceries': ['Apple', 'Milk', 'Bread', 'Eggs', 'Cheese']
}

# Regions and Sales Reps
regions = ['North', 'South', 'East', 'West', 'Central']
sales_reps = ['John Smith', 'Alice Brown', 'David Lee', 'Maria Garcia', 'James Wilson']

# Randomly assign categories
category_col = np.random.choice(categories, n_rows)

# Assign products based on category
product_col = [random.choice(products[cat]) for cat in category_col]

# Assign regions and sales reps
region_col = np.random.choice(regions, n_rows)
sales_rep_col = [random.choice(sales_reps) for _ in range(n_rows)]

# Quantity
quantity_col = np.random.randint(1, 20, n_rows)

# Unit price based on category (rough realistic range)
price_dict = {
    'Electronics': (100, 2000),
    'Furniture': (50, 1500),
    'Clothing': (10, 200),
    'Toys': (5, 100),
    'Books': (5, 50),
    'Groceries': (1, 20)
}
unit_price_col = [round(random.uniform(*price_dict[cat]), 2) for cat in category_col]

# Discount 0% - 30%
discount_col = [round(random.uniform(0, 0.3), 2) for _ in range(n_rows)]

# Revenue calculation
revenue_col = [round(q * p * (1 - d), 2) for q, p, d in zip(quantity_col, unit_price_col, discount_col)]

# Build DataFrame
df = pd.DataFrame({
    'OrderID': order_ids,
    'Date': dates,
    'Product': product_col,
    'Category': category_col,
    'Region': region_col,
    'SalesRep': sales_rep_col,
    'Quantity': quantity_col,
    'UnitPrice': unit_price_col,
    'Discount': discount_col,
    'Revenue': revenue_col
})
# print (df.head())
