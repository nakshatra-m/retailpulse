import pandas as pd
import random
from pathlib import Path


OUTPUT_PATH=Path("data/raw")



def generate_inventory():

    stores=pd.read_csv(
        OUTPUT_PATH/"stores.csv"
    )

    products=pd.read_csv(
        OUTPUT_PATH/"products.csv"
    )


    inventory=[]


    counter=1


    for _,store in stores.iterrows():

        for _,product in products.iterrows():

            inventory.append({

                "inventory_id":f"I{counter:06}",

                "store_id":store.store_id,

                "product_id":product.product_id,

                "stock_quantity":random.randint(
                    0,500
                ),

                "last_updated":"2026-01-01"

            })


            counter+=1



    pd.DataFrame(inventory).to_csv(
        OUTPUT_PATH/"inventory.csv",
        index=False
    )


    print("Inventory generated")



if __name__=="__main__":
    generate_inventory()