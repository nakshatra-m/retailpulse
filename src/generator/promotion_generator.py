import pandas as pd
from pathlib import Path
import random
from datetime import datetime, timedelta


BASE_DIR = Path(__file__).resolve().parents[2]

OUTPUT_PATH = BASE_DIR / "data" / "raw"
OUTPUT_PATH.mkdir(
    parents=True,
    exist_ok=True
)

def save_promotions():

    products = pd.read_csv(
        OUTPUT_PATH / "products.csv"
    )


    promotions = [

        "Black Friday Sale",
        "Christmas Sale",
        "Boxing Day Sale",
        "Summer Sale",
        "Winter Clearance",
        "Back To School",
        "Spring Discount"
    ]


    promotion_data = []


    start_dates = [
        "2026-01-15",
        "2026-03-01",
        "2026-06-01",
        "2026-08-15",
        "2026-11-20",
        "2026-12-01"
    ]


    for i in range(1, 31):

        product = products.sample(
            1
        ).iloc[0]


        start_date = datetime.strptime(
            random.choice(start_dates),
            "%Y-%m-%d"
        )


        duration = random.randint(
            7,
            45
        )


        end_date = start_date + timedelta(
            days=duration
        )


        promotion_data.append(

            {
                "promotion_id":
                    f"PR{i:05}",

                "product_id":
                    product["product_id"],

                "promotion_name":
                    random.choice(promotions),

                "discount_percentage":
                    random.choice(
                        [
                            10,
                            15,
                            20,
                            25,
                            30,
                            40
                        ]
                    ),

                "start_date":
                    start_date.date(),

                "end_date":
                    end_date.date()
            }

        )


    df = pd.DataFrame(
        promotion_data
    )


    df.to_csv(
        OUTPUT_PATH / "promotions.csv",
        index=False
    )


    print(
        "Promotions generated successfully"
    )


if __name__ == "__main__":
    save_promotions()