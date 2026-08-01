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


def load_order_items():

    print("Loading order items...")

    order_items = pd.read_csv(
        DATA_PATH / "order_items.csv"
    )

    with engine.begin() as connection:
        connection.execute(
            text("TRUNCATE TABLE order_items CASCADE")
        )

    order_items.to_sql(
        "order_items",
        con=engine,
        if_exists="append",
        index=False,
        method="multi"
    )

    print("Order items loaded successfully.")


if __name__ == "__main__":
    load_order_items()