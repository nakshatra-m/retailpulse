from pathlib import Path
import sys

from sqlalchemy import text


BASE_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = BASE_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


import pandas as pd

from config.database import engine


DATA_PATH = BASE_DIR / "data" / "raw"


def load_customers():

    print("Loading customers...")

    customers = pd.read_csv(
        DATA_PATH / "customers.csv"
    )


    with engine.begin() as connection:

        connection.execute(
            text("TRUNCATE TABLE customers CASCADE")
        )


    customers.to_sql(
        "customers",
        con=engine,
        if_exists="append",
        index=False,
        method="multi"
    )


    print("Customers loaded successfully.")



if __name__ == "__main__":
    load_customers()