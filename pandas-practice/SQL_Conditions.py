import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    result = products[['product_id', 'product_name', 'low_fats', 'recyclable']]
    return result


data = [['0', 'Pasta', 'Y', 'N'], ['1', 'Noodles', 'Y', 'Y'], ['2', 'Burger', 'N', 'Y'], ['3', 'Pizza', 'Y', 'Y'],
        ['4', 'Chocolate', 'N', 'N']]
products = pd.DataFrame(data, columns=['product_id', 'product_name', 'low_fats', 'recyclable']).astype(
    {'product_id': 'int64', 'product_name': 'category', 'low_fats': 'category', 'recyclable': 'category'})
    
# Filter the DataFrame
result = find_products(products)
print(result)
