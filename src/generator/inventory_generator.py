import random
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

OUTPUT_PATH = BASE_DIR / "data" / "raw"


def generate_inventory():

    stores = pd.read_csv(
        OUTPUT_PATH / "stores.csv"
    )

    products = pd.read_csv(
        OUTPUT_PATH / "products.csv"
    )

    inventory = []

    count = 1

    for _, store in stores.iterrows():

        for _, product in products.iterrows():

            inventory.append({

                "inventory_id":
                    f"I{count:05}",

                "store_id":
                    store.store_id,

                "product_id":
                    product.product_id,

                "stock_quantity":
                    random.randint(
                        20,
                        300
                    ),

                "last_updated":
                    pd.Timestamp.today().date()

            })

            count += 1

    pd.DataFrame(
        inventory
    ).to_csv(
        OUTPUT_PATH / "inventory.csv",
        index=False
    )

    print("Inventory generated")


if __name__ == "__main__":
    generate_inventory()