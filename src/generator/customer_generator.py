import pandas as pd
from pathlib import Path
from faker import Faker


BASE_DIR = Path(__file__).resolve().parents[2]

OUTPUT_PATH = BASE_DIR / "data" / "raw"

OUTPUT_PATH.mkdir(
    parents=True,
    exist_ok=True
)


fake = Faker()



def save_customers():

    customers = []

    used_emails = set()


    provinces = [
        "Ontario",
        "Alberta",
        "British Columbia"
    ]


    for i in range(1, 501):

        email = fake.email()

        # Ensure email uniqueness
        while email in used_emails:
            email = fake.email()

        used_emails.add(email)


        customers.append({

            "customer_id":
                f"C{i:05}",

            "first_name":
                fake.first_name(),

            "last_name":
                fake.last_name(),

            "email":
                email,

            "phone":
                fake.phone_number(),

            "city":
                fake.city(),

            "province":
                fake.random_element(
                    provinces
                ),

            "created_date":
                fake.date_between(
                    start_date="-3y",
                    end_date="today"
                )

        })


    pd.DataFrame(customers).to_csv(
        OUTPUT_PATH / "customers.csv",
        index=False
    )


    print("Customers generated")



if __name__ == "__main__":
    save_customers()