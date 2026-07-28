import pandas as pd
from pathlib import Path


OUTPUT_PATH = Path("data/raw")


def generate_products():
    """
    Creates RetailPulse product catalogue.
    """

    products = [

        {
            "product_id": "P001",
            "product_name": "Milk",
            "category": "Grocery",
            "brand": "Lactantia",
            "supplier": "Agropur",
            "price": 4.99
        },

        {
            "product_id": "P002",
            "product_name": "Bread",
            "category": "Grocery",
            "brand": "Wonder",
            "supplier": "Weston Foods",
            "price": 3.49
        },

        {
            "product_id": "P003",
            "product_name": "Eggs",
            "category": "Grocery",
            "brand": "Burnbrae Farms",
            "supplier": "Burnbrae Farms",
            "price": 5.99
        },

        {
            "product_id": "P004",
            "product_name": "Laptop",
            "category": "Electronics",
            "brand": "Dell",
            "supplier": "Tech Data",
            "price": 999.99
        },

        {
            "product_id": "P005",
            "product_name": "Monitor",
            "category": "Electronics",
            "brand": "LG",
            "supplier": "Ingram Micro",
            "price": 299.99
        },

        {
            "product_id": "P006",
            "product_name": "Keyboard",
            "category": "Electronics",
            "brand": "Logitech",
            "supplier": "Logitech Canada",
            "price": 79.99
        },

        {
            "product_id": "P007",
            "product_name": "Gaming Mouse",
            "category": "Electronics",
            "brand": "Razer",
            "supplier": "Razer Canada",
            "price": 89.99
        },

        {
            "product_id": "P008",
            "product_name": "Coffee Maker",
            "category": "Home",
            "brand": "Breville",
            "supplier": "Breville Canada",
            "price": 149.99
        },

        {
            "product_id": "P009",
            "product_name": "Winter Jacket",
            "category": "Clothing",
            "brand": "Columbia",
            "supplier": "Northern Outfitters",
            "price": 149.99
        },

        {
            "product_id": "P010",
            "product_name": "Running Shoes",
            "category": "Sports",
            "brand": "Nike",
            "supplier": "Nike Canada",
            "price": 129.99
        }

    ]

    return pd.DataFrame(products)



def save_products():

    OUTPUT_PATH.mkdir(
        parents=True,
        exist_ok=True
    )

    products_df = generate_products()

    products_df.to_csv(
        OUTPUT_PATH / "products.csv",
        index=False
    )

    print("products.csv created successfully")



if __name__ == "__main__":
    save_products()