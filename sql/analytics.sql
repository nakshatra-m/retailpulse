
-- ============================================================
-- RetailPulse Analytics Queries
-- ============================================================
-- Purpose:
-- Business-level analytical queries using the transformed
-- analytics tables.
--
-- Source:
-- analytics_daily_sales
-- analytics_product_performance
-- analytics_customer_performance
-- analytics_store_performance
-- ============================================================


-- ============================================================
-- 1. OVERALL BUSINESS PERFORMANCE
-- ============================================================

SELECT
    SUM(total_orders) AS total_orders,
    SUM(units_sold) AS units_sold,
    ROUND(SUM(gross_sales), 2) AS gross_sales,
    ROUND(SUM(refunds), 2) AS refunds,
    ROUND(SUM(net_sales), 2) AS net_sales
FROM analytics_daily_sales;


-- ============================================================
-- 2. STORE PERFORMANCE
-- ============================================================

SELECT
    store_id,
    store_name,
    city,
    province,
    total_orders,
    units_sold,
    ROUND(total_sales, 2) AS total_sales,
    ROUND(average_order_value, 2) AS average_order_value,
    unique_customers
FROM analytics_store_performance
ORDER BY total_sales DESC;


-- ============================================================
-- 3. TOP 10 PRODUCTS BY SALES
-- ============================================================

SELECT
    product_id,
    product_name,
    category,
    brand,
    units_sold,
    ROUND(sales_revenue, 2) AS sales_revenue,
    ROUND(gross_profit, 2) AS gross_profit,
    current_inventory
FROM analytics_product_performance
ORDER BY sales_revenue DESC
LIMIT 10;


-- ============================================================
-- 4. TOP 10 PRODUCTS BY PROFIT
-- ============================================================

SELECT
    product_id,
    product_name,
    category,
    brand,
    units_sold,
    ROUND(sales_revenue, 2) AS sales_revenue,
    ROUND(gross_profit, 2) AS gross_profit,
    current_inventory
FROM analytics_product_performance
ORDER BY gross_profit DESC
LIMIT 10;


-- ============================================================
-- 5. LOW INVENTORY PRODUCTS
-- ============================================================

SELECT
    product_id,
    product_name,
    category,
    current_inventory,
    units_sold,
    ROUND(sales_revenue, 2) AS sales_revenue
FROM analytics_product_performance
WHERE current_inventory < 500
ORDER BY current_inventory ASC;


-- ============================================================
-- 6. CUSTOMER PERFORMANCE
-- ============================================================

SELECT
    customer_id,
    first_name,
    last_name,
    city,
    province,
    total_orders,
    ROUND(total_spend, 2) AS total_spend,
    ROUND(average_order_value, 2) AS average_order_value,
    first_order_date,
    last_order_date
FROM analytics_customer_performance
ORDER BY total_spend DESC
LIMIT 10;


-- ============================================================
-- 7. DAILY SALES TREND
-- ============================================================

SELECT
    order_date,
    SUM(total_orders) AS total_orders,
    SUM(units_sold) AS units_sold,
    ROUND(SUM(gross_sales), 2) AS gross_sales,
    ROUND(SUM(refunds), 2) AS refunds,
    ROUND(SUM(net_sales), 2) AS net_sales
FROM analytics_daily_sales
GROUP BY order_date
ORDER BY order_date;


-- ============================================================
-- 8. SALES BY PROVINCE
-- ============================================================

SELECT
    province,
    SUM(total_orders) AS total_orders,
    SUM(units_sold) AS units_sold,
    ROUND(SUM(gross_sales), 2) AS gross_sales,
    ROUND(SUM(refunds), 2) AS refunds,
    ROUND(SUM(net_sales), 2) AS net_sales
FROM analytics_daily_sales
GROUP BY province
ORDER BY net_sales DESC;


-- ============================================================
-- 9. PRODUCT CATEGORY PERFORMANCE
-- ============================================================

SELECT
    category,
    SUM(units_sold) AS units_sold,
    ROUND(SUM(sales_revenue), 2) AS sales_revenue,
    ROUND(SUM(gross_profit), 2) AS gross_profit,
    SUM(current_inventory) AS current_inventory
FROM analytics_product_performance
GROUP BY category
ORDER BY sales_revenue DESC;


-- ============================================================
-- 10. REFUND ANALYSIS
-- ============================================================

SELECT
    product_id,
    product_name,
    category,
    ROUND(sales_revenue, 2) AS sales_revenue,
    ROUND(refund_amount, 2) AS refund_amount,
    ROUND(
        CASE
            WHEN sales_revenue > 0
            THEN (refund_amount / sales_revenue) * 100
            ELSE 0
        END,
        2
    ) AS refund_rate_percentage
FROM analytics_product_performance
WHERE refund_amount > 0
ORDER BY refund_rate_percentage DESC;
