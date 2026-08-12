from pathlib import Path
import sys


BASE_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = BASE_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


from ingestion.load_stores import load_stores
from ingestion.load_products import load_products
from ingestion.load_customers import load_customers
from ingestion.load_promotions import load_promotions
from ingestion.load_orders import load_orders
from ingestion.load_order_items import load_order_items
from ingestion.load_inventory import load_inventory
from ingestion.load_returns import load_returns



def main():

    print("\nStarting full ingestion pipeline...\n")


    load_stores()

    load_products()

    load_customers()

    load_promotions()

    load_orders()

    load_order_items()

    load_inventory()

    load_returns()


    print("\nFull ingestion pipeline completed successfully!")



if __name__ == "__main__":

    main()