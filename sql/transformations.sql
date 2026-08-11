-- ============================================================
-- 1. DAILY SALES
-- ============================================================

DROP TABLE IF EXISTS analytics_daily_sales;

CREATE TABLE analytics_daily_sales AS
WITH order_sales AS (
    SELECT
        o.order_id,
        o.order_date,
        o.store_id,
        SUM(oi.quantity) AS units_sold,
        SUM(oi.quantity * oi.unit_price) AS gross_sales
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    GROUP BY
        o.order_id,
        o.order_date,
        o.store_id
),
order_refunds AS (
    SELECT
        order_id,
        SUM(refund_amount) AS refunds
    FROM returns
    GROUP BY order_id
)
SELECT
    os.order_date,
    os.store_id,
    s.store_name,
    s.city,
    s.province,

    COUNT(DISTINCT os.order_id) AS total_orders,

    SUM(os.units_sold) AS units_sold,

    SUM(os.gross_sales) AS gross_sales,

    COALESCE(
        SUM(orx.refunds),
        0
    ) AS refunds,

    SUM(os.gross_sales)
        - COALESCE(SUM(orx.refunds), 0) AS net_sales

FROM order_sales os

JOIN stores s
    ON os.store_id = s.store_id

LEFT JOIN order_refunds orx
    ON os.order_id = orx.order_id

GROUP BY
    os.order_date,
    os.store_id,
    s.store_name,
    s.city,
    s.province;


-- ============================================================
-- 2. PRODUCT PERFORMANCE
-- ============================================================

DROP TABLE IF EXISTS analytics_product_performance;

CREATE TABLE analytics_product_performance AS
WITH product_sales AS (
    SELECT
        oi.product_id,

        SUM(oi.quantity) AS units_sold,

        SUM(
            oi.quantity * oi.unit_price
        ) AS sales_revenue,

        SUM(
            oi.quantity * (oi.unit_price - p.cost)
        ) AS gross_profit

    FROM order_items oi

    JOIN products p
        ON oi.product_id = p.product_id

    GROUP BY
        oi.product_id
),
product_refunds AS (
    SELECT
        product_id,
        SUM(refund_amount) AS refund_amount
    FROM returns
    GROUP BY product_id
),
product_inventory AS (
    SELECT
        product_id,
        SUM(stock_quantity) AS current_inventory
    FROM inventory
    GROUP BY product_id
)
SELECT
    p.product_id,
    p.product_name,
    p.category,
    p.brand,
    p.supplier,
    p.price,
    p.cost,

    COALESCE(
        ps.units_sold,
        0
    ) AS units_sold,

    COALESCE(
        ps.sales_revenue,
        0
    ) AS sales_revenue,

    COALESCE(
        ps.gross_profit,
        0
    ) AS gross_profit,

    COALESCE(
        pr.refund_amount,
        0
    ) AS refund_amount,

    COALESCE(
        pi.current_inventory,
        0
    ) AS current_inventory

FROM products p

LEFT JOIN product_sales ps
    ON p.product_id = ps.product_id

LEFT JOIN product_refunds pr
    ON p.product_id = pr.product_id

LEFT JOIN product_inventory pi
    ON p.product_id = pi.product_id;


-- ============================================================
-- 3. CUSTOMER PERFORMANCE
-- ============================================================

DROP TABLE IF EXISTS analytics_customer_performance;

CREATE TABLE analytics_customer_performance AS
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.email,
    c.city,
    c.province,
    c.created_date,

    COUNT(DISTINCT o.order_id) AS total_orders,

    COALESCE(
        SUM(o.total_amount),
        0
    ) AS total_spend,

    COALESCE(
        AVG(o.total_amount),
        0
    ) AS average_order_value,

    MIN(o.order_date) AS first_order_date,

    MAX(o.order_date) AS last_order_date

FROM customers c

LEFT JOIN orders o
    ON c.customer_id = o.customer_id

GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    c.email,
    c.city,
    c.province,
    c.created_date;


-- ============================================================
-- 4. STORE PERFORMANCE
-- ============================================================

DROP TABLE IF EXISTS analytics_store_performance;

CREATE TABLE analytics_store_performance AS
WITH store_orders AS (
    SELECT
        store_id,
        order_id,
        customer_id,
        total_amount
    FROM orders
),
store_items AS (
    SELECT
        o.store_id,
        SUM(oi.quantity) AS units_sold
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    GROUP BY
        o.store_id
)
SELECT
    s.store_id,
    s.store_name,
    s.city,
    s.province,
    s.store_type,
    s.opening_date,

    COUNT(DISTINCT so.order_id) AS total_orders,

    COALESCE(
        SUM(so.total_amount),
        0
    ) AS total_sales,

    COALESCE(
        AVG(so.total_amount),
        0
    ) AS average_order_value,

    COUNT(DISTINCT so.customer_id) AS unique_customers,

    COALESCE(
        si.units_sold,
        0
    ) AS units_sold

FROM stores s

LEFT JOIN store_orders so
    ON s.store_id = so.store_id

LEFT JOIN store_items si
    ON s.store_id = si.store_id

GROUP BY
    s.store_id,
    s.store_name,
    s.city,
    s.province,
    s.store_type,
    s.opening_date,
    si.units_sold;


-- ============================================================
-- 5. INDEXES
-- ============================================================

CREATE INDEX idx_daily_sales_date
    ON analytics_daily_sales(order_date);

CREATE INDEX idx_daily_sales_store
    ON analytics_daily_sales(store_id);

CREATE INDEX idx_product_performance_product
    ON analytics_product_performance(product_id);

CREATE INDEX idx_customer_performance_customer
    ON analytics_customer_performance(customer_id);

CREATE INDEX idx_store_performance_store
    ON analytics_store_performance(store_id);

