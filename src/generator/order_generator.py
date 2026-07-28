import pandas as pd
import random
from pathlib import Path
from datetime import datetime, timedelta


OUTPUT_PATH=Path("data/raw")



def generate_orders(number=50000):

    customers=pd.read_csv(
        OUTPUT_PATH/"customers.csv"
    )

    stores=pd.read_csv(
        OUTPUT_PATH/"stores.csv"
    )

    products=pd.read_csv(
        OUTPUT_PATH/"products.csv"
    )


    orders=[]

    items=[]


    for i in range(number):

        order_id=f"O{i+1:06}"


        customer=random.choice(
            customers.customer_id.tolist()
        )


        store=random.choice(
            stores.store_id.tolist()
        )


        order_date=datetime.now()-timedelta(
            days=random.randint(0,365)
        )


        orders.append({

            "order_id":order_id,

            "customer_id":customer,

            "store_id":store,

            "order_date":order_date.date(),

            "payment_method":random.choice(
                ["Credit Card","Debit","Cash"]
            ),

            "order_status":"Completed"

        })


        item_count=random.randint(1,5)


        selected_products=products.sample(
            item_count
        )


        for _,p in selected_products.iterrows():

            quantity=random.randint(1,3)


            discount=random.choice(
                [0,0,0,10,20]
            )


            items.append({

                "order_item_id":f"{order_id}_{p.product_id}",

                "order_id":order_id,

                "product_id":p.product_id,

                "quantity":quantity,

                "unit_price":p.price,

                "discount":discount

            })



    pd.DataFrame(orders).to_csv(
        OUTPUT_PATH/"orders.csv",
        index=False
    )


    pd.DataFrame(items).to_csv(
        OUTPUT_PATH/"order_items.csv",
        index=False
    )


    print("Orders generated")



if __name__=="__main__":
    generate_orders()