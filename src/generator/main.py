from src.generator.customer_generator import save_customers
from src.generator.store_generator import save_stores
from src.generator.product_generator import save_products
from src.generator.promotion_generator import save_promotions

from src.generator.order_generator import (
    generate_orders,
    generate_order_items
)

from src.generator.inventory_generator import generate_inventory
from src.generator.returns_generator import generate_returns


def main():

    print("\nStarting RetailPulse Data Generation\n")

    # Dimension tables first
    save_customers()

    save_stores()

    save_products()

    save_promotions()

    # Transaction tables
    generate_orders()

    generate_order_items()

    # Supporting tables
    generate_inventory()

    generate_returns()

    print("\nRetailPulse data generation completed!")


if __name__ == "__main__":
    main()