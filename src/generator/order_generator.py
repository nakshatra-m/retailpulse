import random
from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]

OUTPUT_PATH = BASE_DIR / "data" / "raw"


OUTPUT_PATH.mkdir(
    parents=True,
    exist_ok=True
)



def generate_orders():

    customers = pd.read_csv(
        OUTPUT_PATH / "customers.csv"
    )

    stores = pd.read_csv(
        OUTPUT_PATH / "stores.csv"
    )

    promotions = pd.read_csv(
        OUTPUT_PATH / "promotions.csv"
    )


    payment_methods = [
        "Cash",
        "Credit Card",
        "Debit Card",
        "Online"
    ]


    order_statuses = [
        "Completed",
        "Completed",
        "Completed",
        "Cancelled"
    ]


    orders=[]


    for i in range(1,5001):

        promotion_id = None


        if random.random() < 0.35:

            promotion_id = random.choice(
                promotions["promotion_id"].tolist()
            )


        orders.append({

            "order_id":
                f"O{i:05}",


            "customer_id":
                random.choice(
                    customers.customer_id.tolist()
                ),


            "store_id":
                random.choice(
                    stores.store_id.tolist()
                ),


            "promotion_id":
                promotion_id,


            "order_date":
                (
                    pd.Timestamp("2025-01-01")
                    +
                    pd.Timedelta(
                        days=random.randint(0,364)
                    )
                ).date(),


            "payment_method":
                random.choice(payment_methods),


            "order_status":
                random.choice(order_statuses),


            "total_amount":
                0

        })


    pd.DataFrame(orders).to_csv(
        OUTPUT_PATH/"orders.csv",
        index=False
    )


    print("Orders generated")




def generate_order_items():

    orders = pd.read_csv(
        OUTPUT_PATH/"orders.csv"
    )


    products = pd.read_csv(
        OUTPUT_PATH/"products.csv"
    )


    items=[]

    totals={}


    counter=1


    for _,order in orders.iterrows():

        total=0


        selected = products.sample(
            random.randint(1,5)
        )


        for _,product in selected.iterrows():

            quantity=random.randint(
                1,
                4
            )


            price=float(
                product.price
            )


            total += quantity * price


            items.append({

                "order_item_id":
                    f"OI{counter:05}",


                "order_id":
                    order.order_id,


                "product_id":
                    product.product_id,


                "quantity":
                    quantity,


                "unit_price":
                    price

            })


            counter+=1


        totals[
            order.order_id
        ]=round(total,2)



    pd.DataFrame(items).to_csv(
        OUTPUT_PATH/"order_items.csv",
        index=False
    )


    orders["total_amount"] = (
        orders.order_id.map(totals)
    )


    orders.to_csv(
        OUTPUT_PATH/"orders.csv",
        index=False
    )


    print("Order Items generated")



if __name__=="__main__":

    generate_orders()

    generate_order_items()