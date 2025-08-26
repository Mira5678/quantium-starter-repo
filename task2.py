#Convert three CSV files into a single formatted output file.
# Your output file should contain three fields:
#   1. Sales
#   2. Date
#   3. Region

import pandas as pd

daily_sales = pd.concat(map(pd.read_csv, ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']), ignore_index=True)
df = pd.DataFrame(daily_sales)

#remove all rows that is not pink morsel
df.drop(df[df['product'] != 'pink morsel'].index, inplace=True)

#Get sales
df['price'] = df['price'].str.replace("[$,.]", "", regex=True).astype(int)
df['sales'] = df['price'] * df['quantity']

new_df = df[['sales', 'date', 'region']].copy()

#print(new_df)

new_df.to_csv('new_daily_sales.csv', index = False)




