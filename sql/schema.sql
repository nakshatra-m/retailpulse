-- ============================================================
-- RetailPulse Database Schema
-- Purpose: Retail Sales Data Warehouse Foundation
-- ============================================================


-- =========================
-- Customers Table
-- =========================

CREATE TABLE IF NOT EXISTS customers (

    customer_id VARCHAR(20) PRIMARY KEY,

    first_name VARCHAR(50) NOT NULL,

    last_name VARCHAR(50) NOT NULL,

    email VARCHAR(100) UNIQUE,

    phone VARCHAR(20),

    city VARCHAR(50),

    province VARCHAR(50),

    created_date DATE NOT NULL,

    loyalty_level VARCHAR(20)

);



-- =========================
-- Stores Table
-- =========================

CREATE TABLE IF NOT EXISTS stores (

    store_id VARCHAR(20) PRIMARY KEY,

    store_name VARCHAR(100) NOT NULL,

    city VARCHAR(50),

    province VARCHAR(50),

    address VARCHAR(200),

    store_type VARCHAR(50),

    opening_date DATE

);



-- =========================
-- Products Table
-- =========================

CREATE TABLE IF NOT EXISTS products (

    product_id VARCHAR(20) PRIMARY KEY,

    product_name VARCHAR(100) NOT NULL,

    category VARCHAR(50),

    brand VARCHAR(50),

    price NUMERIC(10,2) CHECK(price >= 0),

    cost NUMERIC(10,2) CHECK(cost >= 0),

    supplier VARCHAR(100),

    created_date DATE

);



-- =========================
-- Orders Table
-- =========================

CREATE TABLE IF NOT EXISTS orders (

    order_id VARCHAR(20) PRIMARY KEY,

    customer_id VARCHAR(20) NOT NULL,

    store_id VARCHAR(20) NOT NULL,

    order_date DATE NOT NULL,

    payment_method VARCHAR(50),

    order_status VARCHAR(50),

    total_amount NUMERIC(10,2)
        CHECK(total_amount >= 0),


    CONSTRAINT fk_order_customer

        FOREIGN KEY(customer_id)

        REFERENCES customers(customer_id),


    CONSTRAINT fk_order_store

        FOREIGN KEY(store_id)

        REFERENCES stores(store_id)

);



-- =========================
-- Order Items Table
-- =========================

CREATE TABLE IF NOT EXISTS order_items (

    order_item_id VARCHAR(20) PRIMARY KEY,

    order_id VARCHAR(20) NOT NULL,

    product_id VARCHAR(20) NOT NULL,

    quantity INTEGER
        CHECK(quantity > 0),

    unit_price NUMERIC(10,2)
        CHECK(unit_price >= 0),

    discount NUMERIC(5,2)
        CHECK(discount >= 0),



    CONSTRAINT fk_item_order

        FOREIGN KEY(order_id)

        REFERENCES orders(order_id),


    CONSTRAINT fk_item_product

        FOREIGN KEY(product_id)

        REFERENCES products(product_id)

);



-- =========================
-- Inventory Table
-- =========================

CREATE TABLE IF NOT EXISTS inventory (

    inventory_id VARCHAR(20) PRIMARY KEY,

    product_id VARCHAR(20) NOT NULL,

    store_id VARCHAR(20) NOT NULL,

    stock_quantity INTEGER
        CHECK(stock_quantity >= 0),

    last_updated DATE,



    CONSTRAINT fk_inventory_product

        FOREIGN KEY(product_id)

        REFERENCES products(product_id),



    CONSTRAINT fk_inventory_store

        FOREIGN KEY(store_id)

        REFERENCES stores(store_id)

);



-- =========================
-- Promotions Table
-- =========================

CREATE TABLE IF NOT EXISTS promotions (

    promotion_id VARCHAR(20) PRIMARY KEY,

    product_id VARCHAR(20) NOT NULL,

    promotion_name VARCHAR(100),

    discount_percentage NUMERIC(5,2)
        CHECK(discount_percentage >= 0),


    start_date DATE,

    end_date DATE,



    CONSTRAINT fk_promotion_product

        FOREIGN KEY(product_id)

        REFERENCES products(product_id)

);



-- =========================
-- Returns Table
-- =========================

CREATE TABLE IF NOT EXISTS returns (

    return_id VARCHAR(20) PRIMARY KEY,

    order_id VARCHAR(20) NOT NULL,

    product_id VARCHAR(20) NOT NULL,

    return_date DATE,

    reason VARCHAR(200),

    refund_amount NUMERIC(10,2)
        CHECK(refund_amount >= 0),



    CONSTRAINT fk_return_order

        FOREIGN KEY(order_id)

        REFERENCES orders(order_id),



    CONSTRAINT fk_return_product

        FOREIGN KEY(product_id)

        REFERENCES products(product_id)

);



-- ============================================================
-- Indexes for Performance
-- ============================================================


CREATE INDEX IF NOT EXISTS idx_orders_customer

ON orders(customer_id);



CREATE INDEX IF NOT EXISTS idx_orders_store

ON orders(store_id);



CREATE INDEX IF NOT EXISTS idx_orders_date

ON orders(order_date);



CREATE INDEX IF NOT EXISTS idx_order_items_product

ON order_items(product_id);



CREATE INDEX IF NOT EXISTS idx_inventory_product

ON inventory(product_id);



CREATE INDEX IF NOT EXISTS idx_inventory_store

ON inventory(store_id);



-- ============================================================
-- Schema Complete
-- ============================================================