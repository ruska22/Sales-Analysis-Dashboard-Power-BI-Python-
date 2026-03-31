import pandas as pd

df = pd.read_csv("retail_sales_5M.csv")

print(df.head())
print(df.shape)

df['Date'] = pd.to_datetime(df['Date'])

# remove duplicates
#df = df.drop_duplicates()

# check missing values
#print(df.isnull().sum())

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['MonthName'] = df['Date'].dt.month_name()

df['OrderValue'] = df['Quantity'] * df['UnitPrice']


monthly_sales = df.groupby(['Year','Month'])['Revenue'].sum().reset_index()
#print(monthly_sales.head())

top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(10)
#print(top_products)

region_sales = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
#print(region_sales)

df.to_csv("sales_cleaned.csv", index=False)

monthly_sales.to_csv("monthly_sales.csv", index=False)
top_products.to_csv("top_products.csv")
region_sales.to_csv("region_sales.csv")