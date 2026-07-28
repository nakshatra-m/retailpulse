import pandas as pd
import random
from faker import Faker
from pathlib import Path


fake = Faker()

OUTPUT_PATH = Path("data/raw")


cities = [
    ("Toronto","Ontario"),
    ("Mississauga","Ontario"),
    ("Brampton","Ontario"),
    ("Hamilton","Ontario"),
    ("Ottawa","Ontario"),
    ("Calgary","Alberta"),
    ("Edmonton","Alberta"),
    ("Vancouver","British Columbia")
]


def generate_customers(count=10000):

    customers=[]


    for i in range(count):

        city, province = random.choice(cities)


        loyalty = random.choices(
            ["Gold","Silver","Bronze"],
            weights=[10,30,60]
        )[0]


        customers.append({

            "customer_id": f"C{i+1:05}",

            "first_name": fake.first_name(),

            "last_name": fake.last_name(),

            "email": fake.email(),

            "city": city,

            "province": province,

            "signup_date": fake.date_between(
                start_date="-5y",
                end_date="today"
            ),

            "loyalty_level": loyalty

        })


    return pd.DataFrame(customers)



def save_customers():

    OUTPUT_PATH.mkdir(
        exist_ok=True
    )


    df = generate_customers()

    df.to_csv(
        OUTPUT_PATH/"customers.csv",
        index=False
    )


    print("Customers generated")



if __name__=="__main__":
    save_customers()