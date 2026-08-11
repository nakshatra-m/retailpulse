-- ============================================================
-- RetailPulse Data Validation
-- ============================================================


-- ============================================================
-- 1. ROW COUNTS
-- ============================================================

SELECT 'stores' AS table_name, COUNT(*) AS row_count FROM stores
UNION ALL
SELECT 'products', COUNT(*) FROM products
UNION ALL
SELECT 'customers', COUNT(*) FROM customers
UNION ALL
SELECT 'promotions', COUNT(*) FROM promotions
UNION ALL
SELECT 'orders', COUNT(*) FROM orders
UNION ALL
SELECT 'order_items', COUNT(*) FROM order_items
UNION ALL
SELECT 'inventory', COUNT(*) FROM inventory
UNION ALL
SELECT 'returns', COUNT(*) FROM returns
ORDER BY table_name;


-- ============================================================
-- 2. PRIMARY KEY / DUPLICATE VALIDATION
-- ============================================================

SELECT 'stores' AS table_name, 'store_id' AS primary_key,
       COUNT(*) AS duplicate_groups
FROM (
    SELECT store_id
    FROM stores
    GROUP BY store_id
    HAVING COUNT(*) > 1
) d

UNION ALL

SELECT 'products', 'product_id', COUNT(*)
FROM (
    SELECT product_id
    FROM products
    GROUP BY product_id
    HAVING COUNT(*) > 1
) d

UNION ALL

SELECT 'customers', 'customer_id', COUNT(*)
FROM (
    SELECT customer_id
    FROM customers
    GROUP BY customer_id
    HAVING COUNT(*) > 1
) d

UNION ALL

SELECT 'promotions', 'promotion_id', COUNT(*)
FROM (
    SELECT promotion_id
    FROM promotions
    GROUP BY promotion_id
    HAVING COUNT(*) > 1
) d

UNION ALL

SELECT 'orders', 'order_id', COUNT(*)
FROM (
    SELECT order_id
    FROM orders
    GROUP BY order_id
    HAVING COUNT(*) > 1
) d

UNION ALL

SELECT 'order_items', 'order_item_id', COUNT(*)
FROM (
    SELECT order_item_id
    FROM order_items
    GROUP BY order_item_id
    HAVING COUNT(*) > 1
) d

UNION ALL

SELECT 'inventory', 'inventory_id', COUNT(*)
FROM (
    SELECT inventory_id
    FROM inventory
    GROUP BY inventory_id
    HAVING COUNT(*) > 1
) d

UNION ALL

SELECT 'returns', 'return_id', COUNT(*)
FROM (
    SELECT return_id
    FROM returns
    GROUP BY return_id
    HAVING COUNT(*) > 1
) d;


-- ============================================================
-- 3. REQUIRED FIELD VALIDATION
-- ============================================================

SELECT 'stores' AS table_name, COUNT(*) AS invalid_rows
FROM stores
WHERE store_id IS NULL OR store_name IS NULL

UNION ALL

SELECT 'products', COUNT(*)
FROM products
WHERE product_id IS NULL OR product_name IS NULL

UNION ALL

SELECT 'customers', COUNT(*)
FROM customers
WHERE customer_id IS NULL
   OR first_name IS NULL
   OR last_name IS NULL
   OR created_date IS NULL

UNION ALL

SELECT 'promotions', COUNT(*)
FROM promotions
WHERE promotion_id IS NULL OR product_id IS NULL

UNION ALL

SELECT 'orders', COUNT(*)
FROM orders
WHERE order_id IS NULL
   OR customer_id IS NULL
   OR store_id IS NULL
   OR order_date IS NULL

UNION ALL

SELECT 'order_items', COUNT(*)
FROM order_items
WHERE order_item_id IS NULL
   OR order_id IS NULL
   OR product_id IS NULL

UNION ALL

SELECT 'inventory', COUNT(*)
FROM inventory
WHERE inventory_id IS NULL
   OR store_id IS NULL
   OR product_id IS NULL

UNION ALL

SELECT 'returns', COUNT(*)
FROM returns
WHERE return_id IS NULL
   OR order_id IS NULL
   OR product_id IS NULL;


-- ============================================================
-- 4. FOREIGN KEY INTEGRITY
-- ============================================================

SELECT 'orders -> customers' AS check_name,
       COUNT(*) AS invalid_rows
FROM orders o
LEFT JOIN customers c
    ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL

UNION ALL

SELECT 'orders -> stores',
       COUNT(*)
FROM orders o
LEFT JOIN stores s
    ON o.store_id = s.store_id
WHERE s.store_id IS NULL

UNION ALL

SELECT 'orders -> promotions',
       COUNT(*)
FROM orders o
LEFT JOIN promotions p
    ON o.promotion_id = p.promotion_id
WHERE o.promotion_id IS NOT NULL
  AND p.promotion_id IS NULL

UNION ALL

SELECT 'order_items -> orders',
       COUNT(*)
FROM order_items oi
LEFT JOIN orders o
    ON oi.order_id = o.order_id
WHERE o.order_id IS NULL

UNION ALL

SELECT 'order_items -> products',
       COUNT(*)
FROM order_items oi
LEFT JOIN products p
    ON oi.product_id = p.product_id
WHERE p.product_id IS NULL

UNION ALL

SELECT 'inventory -> stores',
       COUNT(*)
FROM inventory i
LEFT JOIN stores s
    ON i.store_id = s.store_id
WHERE s.store_id IS NULL

UNION ALL

SELECT 'inventory -> products',
       COUNT(*)
FROM inventory i
LEFT JOIN products p
    ON i.product_id = p.product_id
WHERE p.product_id IS NULL

UNION ALL

SELECT 'promotions -> products',
       COUNT(*)
FROM promotions pr
LEFT JOIN products p
    ON pr.product_id = p.product_id
WHERE p.product_id IS NULL

UNION ALL

SELECT 'returns -> orders',
       COUNT(*)
FROM returns r
LEFT JOIN orders o
    ON r.order_id = o.order_id
WHERE o.order_id IS NULL

UNION ALL

SELECT 'returns -> products',
       COUNT(*)
FROM returns r
LEFT JOIN products p
    ON r.product_id = p.product_id
WHERE p.product_id IS NULL;


-- ============================================================
-- 5. BUSINESS RULE VALIDATION
-- ============================================================

SELECT 'negative product prices/costs' AS check_name,
       COUNT(*) AS invalid_rows
FROM products
WHERE price < 0 OR cost < 0

UNION ALL

SELECT 'cost greater than price',
       COUNT(*)
FROM products
WHERE cost > price

UNION ALL

SELECT 'invalid order quantities',
       COUNT(*)
FROM order_items
WHERE quantity IS NULL OR quantity <= 0

UNION ALL

SELECT 'invalid order item prices',
       COUNT(*)
FROM order_items
WHERE unit_price IS NULL OR unit_price < 0

UNION ALL

SELECT 'invalid inventory quantities',
       COUNT(*)
FROM inventory
WHERE stock_quantity IS NULL OR stock_quantity < 0

UNION ALL

SELECT 'invalid order totals',
       COUNT(*)
FROM orders
WHERE total_amount IS NOT NULL
  AND total_amount < 0

UNION ALL

SELECT 'invalid refund amounts',
       COUNT(*)
FROM returns
WHERE refund_amount IS NOT NULL
  AND refund_amount < 0

UNION ALL

SELECT 'invalid discounts',
       COUNT(*)
FROM promotions
WHERE discount_percentage IS NOT NULL
  AND (
      discount_percentage < 0
      OR discount_percentage > 100
  );


-- ============================================================
-- 6. DATE VALIDATION
-- ============================================================

SELECT 'future orders' AS check_name,
       COUNT(*) AS invalid_rows
FROM orders
WHERE order_date > CURRENT_DATE

UNION ALL

SELECT 'future customer creation dates',
       COUNT(*)
FROM customers
WHERE created_date > CURRENT_DATE

UNION ALL

SELECT 'future inventory updates',
       COUNT(*)
FROM inventory
WHERE last_updated > CURRENT_DATE

UNION ALL

SELECT 'return before order',
       COUNT(*)
FROM returns r
JOIN orders o
    ON r.order_id = o.order_id
WHERE r.return_date IS NOT NULL
  AND r.return_date < o.order_date

UNION ALL

SELECT 'promotion end before start',
       COUNT(*)
FROM promotions
WHERE start_date IS NOT NULL
  AND end_date IS NOT NULL
  AND end_date < start_date

UNION ALL

SELECT 'order before store opening',
       COUNT(*)
FROM orders o
JOIN stores s
    ON o.store_id = s.store_id
WHERE s.opening_date IS NOT NULL
  AND o.order_date < s.opening_date;


-- ============================================================
-- 7. ORDER COMPLETENESS
-- ============================================================

SELECT 'orders without order items' AS check_name,
       COUNT(*) AS invalid_rows
FROM orders o
LEFT JOIN order_items oi
    ON o.order_id = oi.order_id
WHERE oi.order_item_id IS NULL;