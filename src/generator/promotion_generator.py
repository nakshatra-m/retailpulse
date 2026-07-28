import pandas as pd
from pathlib import Path


OUTPUT_PATH=Path("data/raw")



def generate_promotions():

    promotions=[

        ["PR001","Black Friday",30],
        ["PR002","Christmas Sale",20],
        ["PR003","Boxing Day",25],
        ["PR004","Summer Sale",15],
        ["PR005","Winter Clearance",40]

    ]


    return pd.DataFrame(
        promotions,
        columns=[
            "promotion_id",
            "promotion_name",
            "discount_percentage"
        ]
    )



def save_promotions():

    OUTPUT_PATH.mkdir(
        exist_ok=True
    )


    df=generate_promotions()

    df.to_csv(
        OUTPUT_PATH/"promotions.csv",
        index=False
    )


    print("Promotions generated")



if __name__=="__main__":
    save_promotions()