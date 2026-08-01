import pandas as pd
from pathlib import Path
import random

BASE_DIR = Path(__file__).resolve().parents[2]

OUTPUT_PATH = BASE_DIR / "data" / "raw"
OUTPUT_PATH.mkdir(
    parents=True,
    exist_ok=True
)

def save_products():

    products=[]


    categories=[
        "Electronics",
        "Clothing",
        "Grocery",
        "Home",
        "Sports"
    ]


    brands=[
        "Samsung",
        "Nike",
        "Apple",
        "Sony",
        "Adidas"
    ]


    suppliers=[
        "Supplier A",
        "Supplier B",
        "Supplier C"
    ]


    for i in range(1,101):

        cost=random.randint(5,500)

        price=round(
            cost*random.uniform(1.2,2),
            2
        )


        products.append({

            "product_id":
            f"P{i:05}",

            "product_name":
            f"Product {i}",

            "category":
            random.choice(categories),

            "brand":
            random.choice(brands),

            "price":
            price,

            "cost":
            cost,

            "supplier":
            random.choice(suppliers)

        })


    pd.DataFrame(products).to_csv(
        OUTPUT_PATH/"products.csv",
        index=False
    )


    print("Products generated")


if __name__=="__main__":
    save_products()