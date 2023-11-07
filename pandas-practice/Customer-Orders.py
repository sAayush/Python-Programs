import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Merge the customers and orders DataFrames using a left join
    merged_df = customers.merge(orders, left_on='id', right_on='customerId', how='left')

    # Filter rows where customerId is NaN (indicating no order)
    result_df = merged_df[merged_df['customerId'].isna()]

    # Select the 'name' column from the resulting DataFrame
    result_df = result_df[['name']]

    #changing the column name
    result_df.columns = ['customers']

    # Reset the index (optional)
    result_df.reset_index(drop=True, inplace=True)

    return result_df


data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id': 'Int64', 'customerId': 'Int64'})

# Filter the DataFrame
result = find_customers(customers, orders)
print(result)
