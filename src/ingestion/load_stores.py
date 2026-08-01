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


def load_stores():

    print("Loading stores...")

    stores = pd.read_csv(
        DATA_PATH / "stores.csv"
    )

    try:

        # Remove existing records before loading fresh data
        with engine.begin() as connection:

            connection.execute(
                text("TRUNCATE TABLE stores CASCADE")
            )


        # Insert fresh CSV data
        stores.to_sql(
            "stores",
            con=engine,
            if_exists="append",
            index=False,
            method="multi"
        )


        print("Stores loaded successfully.")


    except Exception as e:

        print("Failed loading stores.")
        print(e)



if __name__ == "__main__":
    load_stores()