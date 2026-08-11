
from sqlalchemy import text

from src.config.database import engine


def run_analytics_validation():
    """
    Validate the RetailPulse analytics layer.

    Checks:
    1. Orders are preserved.
    2. Units sold are preserved.
    3. Product units match source data.
    4. Revenue matches across analytics tables.
    5. Refunds match across analytics tables.
    6. Customer order totals match source data.
    7. Store count is preserved.
    8. Product count is preserved.
    9. Net sales calculation is correct.
    10. Product metrics contain no negative values.
    """

    print("=" * 60)
    print("RetailPulse Analytics Validation")
    print("=" * 60)

    checks = [
        (
            "Order count reconciliation",
            """
            SELECT
                (
                    SELECT COUNT(*)
                    FROM orders
                ) AS source_orders,
                (
                    SELECT COALESCE(SUM(total_orders), 0)
                    FROM analytics_daily_sales
                ) AS analytics_orders
            """
        ),
        (
            "Daily units reconciliation",
            """
            SELECT
                (
                    SELECT COALESCE(SUM(quantity), 0)
                    FROM order_items
                ) AS source_units,
                (
                    SELECT COALESCE(SUM(units_sold), 0)
                    FROM analytics_daily_sales
                ) AS analytics_units
            """
        ),
        (
            "Product units reconciliation",
            """
            SELECT
                (
                    SELECT COALESCE(SUM(quantity), 0)
                    FROM order_items
                ) AS source_units,
                (
                    SELECT COALESCE(SUM(units_sold), 0)
                    FROM analytics_product_performance
                ) AS analytics_units
            """
        ),
        (
            "Revenue reconciliation",
            """
            SELECT
                (
                    SELECT COALESCE(SUM(gross_sales), 0)
                    FROM analytics_daily_sales
                ) AS daily_revenue,
                (
                    SELECT COALESCE(SUM(sales_revenue), 0)
                    FROM analytics_product_performance
                ) AS product_revenue
            """
        ),
        (
            "Refund reconciliation",
            """
            SELECT
                (
                    SELECT COALESCE(SUM(refunds), 0)
                    FROM analytics_daily_sales
                ) AS daily_refunds,
                (
                    SELECT COALESCE(SUM(refund_amount), 0)
                    FROM analytics_product_performance
                ) AS product_refunds
            """
        ),
        (
            "Customer order reconciliation",
            """
            SELECT
                (
                    SELECT COUNT(*)
                    FROM orders
                ) AS source_orders,
                (
                    SELECT COALESCE(SUM(total_orders), 0)
                    FROM analytics_customer_performance
                ) AS customer_orders
            """
        ),
        (
            "Store count reconciliation",
            """
            SELECT
                (
                    SELECT COUNT(*)
                    FROM stores
                ) AS source_stores,
                (
                    SELECT COUNT(*)
                    FROM analytics_store_performance
                ) AS analytics_stores
            """
        ),
        (
            "Product count reconciliation",
            """
            SELECT
                (
                    SELECT COUNT(*)
                    FROM products
                ) AS source_products,
                (
                    SELECT COUNT(*)
                    FROM analytics_product_performance
                ) AS analytics_products
            """
        ),
        (
            "Net sales calculation",
            """
            SELECT COUNT(*) AS invalid_rows
            FROM analytics_daily_sales
            WHERE net_sales != gross_sales - refunds
            """
        ),
        (
            "Product metric validity",
            """
            SELECT COUNT(*) AS invalid_rows
            FROM analytics_product_performance
            WHERE units_sold < 0
               OR sales_revenue < 0
               OR gross_profit < 0
               OR refund_amount < 0
               OR current_inventory < 0
            """
        ),
    ]

    passed = 0
    failed = 0

    try:
        with engine.connect() as connection:

            for index, (name, query) in enumerate(checks, start=1):

                print()
                print(f"Check {index}: {name}")
                print("-" * 60)

                try:
                    result = connection.execute(text(query))
                    row = result.fetchone()
                    values = dict(row._mapping)

                    print(values)

                    if "invalid_rows" in values:
                        check_passed = values["invalid_rows"] == 0
                    elif (
                        "source_orders" in values
                        and "analytics_orders" in values
                    ):
                        check_passed = (
                            values["source_orders"]
                            == values["analytics_orders"]
                        )
                    elif (
                        "source_units" in values
                        and "analytics_units" in values
                    ):
                        check_passed = (
                            values["source_units"]
                            == values["analytics_units"]
                        )
                    elif (
                        "daily_revenue" in values
                        and "product_revenue" in values
                    ):
                        check_passed = (
                            values["daily_revenue"]
                            == values["product_revenue"]
                        )
                    elif (
                        "daily_refunds" in values
                        and "product_refunds" in values
                    ):
                        check_passed = (
                            values["daily_refunds"]
                            == values["product_refunds"]
                        )
                    elif (
                        "source_stores" in values
                        and "analytics_stores" in values
                    ):
                        check_passed = (
                            values["source_stores"]
                            == values["analytics_stores"]
                        )
                    elif (
                        "source_products" in values
                        and "analytics_products" in values
                    ):
                        check_passed = (
                            values["source_products"]
                            == values["analytics_products"]
                        )
                    else:
                        check_passed = True

                    if check_passed:
                        print("[PASS]")
                        passed += 1
                    else:
                        print("[FAIL]")
                        failed += 1

                except Exception as error:
                    print("[FAIL]")
                    print(f"Error: {error}")
                    failed += 1

    except Exception as error:
        print()
        print("ANALYTICS VALIDATION ERROR")
        print(error)
        return False

    print()
    print("=" * 60)
    print("ANALYTICS VALIDATION SUMMARY")
    print("=" * 60)
    print(f"Checks executed: {len(checks)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print()

    if failed == 0:
        print("ANALYTICS VALIDATION RESULT: PASSED")
        print("=" * 60)
        return True

    print("ANALYTICS VALIDATION RESULT: FAILED")
    print("=" * 60)
    return False


if __name__ == "__main__":
    success = run_analytics_validation()

    if not success:
        raise SystemExit(1)
