from faker import Faker
import pandas as pd
import random
import os


fake = Faker()


OUTPUT_PATH = "../data/raw"


os.makedirs(
    OUTPUT_PATH,
    exist_ok=True
)

def generate_customers(number=10000):

    customers = []

    for i in range(1, number + 1):

        customers.append({

            "customer_id": i,

            "first_name": fake.first_name(),

            "last_name": fake.last_name(),

            "email": fake.email(),

            "city": fake.city(),

            "province": random.choice([
                "Ontario",
                "Alberta",
                "British Columbia",
                "Quebec"
            ])

        })


    df = pd.DataFrame(customers)

    df.to_csv(
        f"{OUTPUT_PATH}/customers.csv",
        index=False
    )


    print("Customers generated:", len(df))

def generate_products(number=500):

    categories = [
        "Electronics",
        "Clothing",
        "Food",
        "Furniture",
        "Sports"
    ]


    products = []


    for i in range(1, number + 1):

        products.append({

            "product_id": i,

            "product_name": fake.word(),

            "category": random.choice(categories),

            "price": round(
                random.uniform(5,500),
                2
            )

        })


    df = pd.DataFrame(products)


    df.to_csv(
        f"{OUTPUT_PATH}/products.csv",
        index=False
    )


    print("Products generated:", len(df))

def generate_stores(number=50):

    stores = []


    for i in range(1, number + 1):

        stores.append({

            "store_id": i,

            "store_name": f"Retail Store {i}",

            "city": fake.city(),

            "province": random.choice([
                "Ontario",
                "Alberta",
                "Quebec",
                "British Columbia"
            ])

        })


    df = pd.DataFrame(stores)


    df.to_csv(
        f"{OUTPUT_PATH}/stores.csv",
        index=False
    )


    print("Stores generated:", len(df))

def generate_sales(number=100000):

    sales = []


    for i in range(1, number + 1):

        sales.append({

            "sale_id": i,

            "customer_id": random.randint(
                1,
                10000
            ),

            "product_id": random.randint(
                1,
                500
            ),

            "store_id": random.randint(
                1,
                50
            ),

            "quantity": random.randint(
                1,
                10
            ),

            "sale_date": fake.date_between(
                start_date="-2y",
                end_date="today"
            )

        })


    df = pd.DataFrame(sales)


    df.to_csv(
        f"{OUTPUT_PATH}/sales.csv",
        index=False
    )


    print("Sales generated:", len(df))

if __name__ == "__main__":


    generate_customers()

    generate_products()

    generate_stores()

    generate_sales()


    print("All data generated successfully!")