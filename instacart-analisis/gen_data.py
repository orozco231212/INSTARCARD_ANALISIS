import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)

orders = pd.DataFrame({
    'order_id': [1,2,3,4],
    'user_id': [101,102,101,103],
    'eval_set': ['prior','train','prior','prior'],
    'order_number': [1,1,2,1],
    'order_dow': [0,1,0,2],
    'order_hour_of_day': [10,14,10,9],
    'days_since_prior_order': [None, None, 7.0, None]
})
orders.to_csv(DATA_DIR / 'instacart_orders.csv', sep=';', index=False)

products = pd.DataFrame({
    'product_id': [1,2,3],
    'product_name': ['Apple','Banana','Milk'],
    'aisle_id': [1,2,3],
    'department_id': [1,1,2]
})
products.to_csv(DATA_DIR / 'products.csv', sep=';', index=False)

aisles = pd.DataFrame({
    'aisle_id': [1,2,3],
    'aisle': ['fruit','fruit','dairy']
})
aisles.to_csv(DATA_DIR / 'aisles.csv', sep=';', index=False)

departments = pd.DataFrame({
    'department_id': [1,2],
    'department': ['produce','dairy']
})
departments.to_csv(DATA_DIR / 'departments.csv', sep=';', index=False)

order_products = pd.DataFrame({
    'order_id': [1,1,2,3],
    'product_id': [1,2,3,1],
    'add_to_cart_order': [1,2,1,1],
    'reordered': [0,1,0,1]
})
order_products.to_csv(DATA_DIR / 'order_products.csv', sep=';', index=False)

print(f'Datos generados en: {DATA_DIR}')