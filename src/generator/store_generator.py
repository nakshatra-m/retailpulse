import pandas as pd
from pathlib import Path


# Location where generated files will be stored
OUTPUT_PATH = Path("data/raw")


def generate_stores():
    """
    Creates RetailPulse store master data.
    """

    stores = [
        {
            "store_id": "S001",
            "store_name": "RetailPulse Toronto",
            "city": "Toronto",
            "province": "Ontario",
            "opening_date": "2020-05-10"
        },
        {
            "store_id": "S002",
            "store_name": "RetailPulse Mississauga",
            "city": "Mississauga",
            "province": "Ontario",
            "opening_date": "2021-03-15"
        },
        {
            "store_id": "S003",
            "store_name": "RetailPulse Brampton",
            "city": "Brampton",
            "province": "Ontario",
            "opening_date": "2021-08-20"
        },
        {
            "store_id": "S004",
            "store_name": "RetailPulse Hamilton",
            "city": "Hamilton",
            "province": "Ontario",
            "opening_date": "2022-01-12"
        },
        {
            "store_id": "S005",
            "store_name": "RetailPulse Ottawa",
            "city": "Ottawa",
            "province": "Ontario",
            "opening_date": "2022-06-01"
        },
        {
            "store_id": "S006",
            "store_name": "RetailPulse Calgary",
            "city": "Calgary",
            "province": "Alberta",
            "opening_date": "2023-02-18"
        },
        {
            "store_id": "S007",
            "store_name": "RetailPulse Edmonton",
            "city": "Edmonton",
            "province": "Alberta",
            "opening_date": "2023-07-25"
        },
        {
            "store_id": "S008",
            "store_name": "RetailPulse Vancouver",
            "city": "Vancouver",
            "province": "British Columbia",
            "opening_date": "2024-04-05"
        }
    ]

    return pd.DataFrame(stores)



def save_stores():
    """
    Saves store data as CSV.
    """

    OUTPUT_PATH.mkdir(
        parents=True,
        exist_ok=True
    )

    stores_df = generate_stores()

    stores_df.to_csv(
        OUTPUT_PATH / "stores.csv",
        index=False
    )

    print("stores.csv created successfully")



if __name__ == "__main__":
    save_stores()