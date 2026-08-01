import random
from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]

OUTPUT_PATH = BASE_DIR / "data" / "raw"



def generate_returns():

    orders = pd.read_csv(
        OUTPUT_PATH/"orders.csv"
    )


    order_items = pd.read_csv(
        OUTPUT_PATH/"order_items.csv"
    )


    returns=[]


    reasons=[

        "Damaged",

        "Wrong Item",

        "Defective",

        "Changed Mind"

    ]


    selected = orders.sample(
        frac=0.05,
        random_state=42
    )


    counter=1


    for _,order in selected.iterrows():


        items = order_items[
            order_items.order_id ==
            order.order_id
        ]


        product = items.sample(
            1
        ).iloc[0]


        return_date = (
            pd.to_datetime(order.order_date)
            +
            pd.Timedelta(
                days=random.randint(1,30)
            )
        )


        returns.append({

            "return_id":
                f"R{counter:05}",


            "order_id":
                order.order_id,


            "product_id":
                product.product_id,


            "return_date":
                return_date.date(),


            "reason":
                random.choice(reasons),


            "refund_amount":
                round(
                    random.uniform(
                        20,
                        order.total_amount
                    ),
                    2
                )

        })


        counter+=1



    pd.DataFrame(returns).to_csv(
        OUTPUT_PATH/"returns.csv",
        index=False
    )


    print("Returns generated")



if __name__=="__main__":

    generate_returns()