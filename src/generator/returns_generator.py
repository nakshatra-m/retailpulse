import pandas as pd
import random
from pathlib import Path


OUTPUT_PATH=Path("data/raw")



def generate_returns():

    orders=pd.read_csv(
        OUTPUT_PATH/"orders.csv"
    )


    returns=[]


    selected=orders.sample(
        frac=0.05
    )


    for i,(_,row) in enumerate(selected.iterrows()):


        returns.append({

            "return_id":f"R{i+1:05}",

            "order_id":row.order_id,

            "return_reason":random.choice(
                [
                    "Damaged",
                    "Wrong Size",
                    "Defective",
                    "Changed Mind"
                ]
            )

        })


    pd.DataFrame(returns).to_csv(
        OUTPUT_PATH/"returns.csv",
        index=False
    )


    print("Returns generated")



if __name__=="__main__":
    generate_returns()