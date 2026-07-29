from customer_generator import save_customers
from store_generator import save_stores
from product_generator import save_products
from promotion_generator import save_promotions
from order_generator import generate_orders
from inventory_generator import generate_inventory
from returns_generator import generate_returns



def main():

    print("\nStarting RetailPulse Data Generation\n")


    save_customers()

    save_stores()

    save_products()

    save_promotions()

    generate_orders()

    generate_inventory()

    generate_returns()


    print(
        "\nRetailPulse data generation completed!"
    )



if __name__ == "__main__":

    main()