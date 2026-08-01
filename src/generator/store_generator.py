import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

OUTPUT_PATH = BASE_DIR / "data" / "raw"

OUTPUT_PATH.mkdir(
    parents=True,
    exist_ok=True
)

def save_stores():

    stores = [

        {
            "store_id":"S001",
            "store_name":"RetailPulse Toronto",
            "city":"Toronto",
            "province":"Ontario",
            "address":"100 King Street",
            "store_type":"Superstore",
            "opening_date":"2020-05-10"
        },

        {
            "store_id":"S002",
            "store_name":"RetailPulse Mississauga",
            "city":"Mississauga",
            "province":"Ontario",
            "address":"200 Lakeshore Road",
            "store_type":"Superstore",
            "opening_date":"2021-03-15"
        },

        {
            "store_id":"S003",
            "store_name":"RetailPulse Brampton",
            "city":"Brampton",
            "province":"Ontario",
            "address":"300 Main Street",
            "store_type":"Warehouse",
            "opening_date":"2021-08-20"
        },

        {
            "store_id":"S004",
            "store_name":"RetailPulse Hamilton",
            "city":"Hamilton",
            "province":"Ontario",
            "address":"400 James Street",
            "store_type":"Superstore",
            "opening_date":"2022-01-12"
        },

        {
            "store_id":"S005",
            "store_name":"RetailPulse Ottawa",
            "city":"Ottawa",
            "province":"Ontario",
            "address":"500 Bank Street",
            "store_type":"Warehouse",
            "opening_date":"2022-06-01"
        },

        {
            "store_id":"S006",
            "store_name":"RetailPulse Calgary",
            "city":"Calgary",
            "province":"Alberta",
            "address":"600 Centre Street",
            "store_type":"Superstore",
            "opening_date":"2023-02-18"
        },

        {
            "store_id":"S007",
            "store_name":"RetailPulse Edmonton",
            "city":"Edmonton",
            "province":"Alberta",
            "address":"700 Jasper Avenue",
            "store_type":"Warehouse",
            "opening_date":"2023-07-25"
        },

        {
            "store_id":"S008",
            "store_name":"RetailPulse Vancouver",
            "city":"Vancouver",
            "province":"British Columbia",
            "address":"800 Granville Street",
            "store_type":"Superstore",
            "opening_date":"2024-04-05"
        }

    ]


    pd.DataFrame(stores).to_csv(
        OUTPUT_PATH/"stores.csv",
        index=False
    )


    print("Stores generated")


if __name__=="__main__":
    save_stores()