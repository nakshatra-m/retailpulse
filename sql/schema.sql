DROP TABLE IF EXISTS returns;
DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS promotions;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS stores;



-- STORES
CREATE TABLE IF NOT EXISTS stores(

    store_id VARCHAR(20) PRIMARY KEY,

    store_name VARCHAR(100) NOT NULL,

    city VARCHAR(50),

    province VARCHAR(50),

    address VARCHAR(200),

    store_type VARCHAR(50),

    opening_date DATE

);



-- CUSTOMERS
CREATE TABLE IF NOT EXISTS customers(

    customer_id VARCHAR(20) PRIMARY KEY,

    first_name VARCHAR(50) NOT NULL,

    last_name VARCHAR(50) NOT NULL,

    email VARCHAR(100) UNIQUE,

    phone VARCHAR(30),

    city VARCHAR(50),

    province VARCHAR(50),

    created_date DATE NOT NULL

);



-- PRODUCTS
CREATE TABLE IF NOT EXISTS products(

    product_id VARCHAR(20) PRIMARY KEY,

    product_name VARCHAR(100) NOT NULL,

    category VARCHAR(50),

    brand VARCHAR(50),

    price NUMERIC(10,2),

    cost NUMERIC(10,2),

    supplier VARCHAR(100),

    CHECK(price >= 0),

    CHECK(cost >= 0)

);



-- PROMOTIONS
CREATE TABLE IF NOT EXISTS promotions(

    promotion_id VARCHAR(20) PRIMARY KEY,

    product_id VARCHAR(20) NOT NULL,

    promotion_name VARCHAR(100),

    discount_percentage NUMERIC(5,2),

    start_date DATE,

    end_date DATE,

    CHECK(discount_percentage >= 0),

    FOREIGN KEY(product_id)
        REFERENCES products(product_id)

);



-- ORDERS
CREATE TABLE IF NOT EXISTS orders(

    order_id VARCHAR(20) PRIMARY KEY,

    customer_id VARCHAR(20) NOT NULL,

    store_id VARCHAR(20) NOT NULL,

    promotion_id VARCHAR(20),

    order_date DATE NOT NULL,

    payment_method VARCHAR(50),

    order_status VARCHAR(50),

    total_amount NUMERIC(10,2),

    CHECK(total_amount >= 0),

    FOREIGN KEY(customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY(store_id)
        REFERENCES stores(store_id),

    FOREIGN KEY(promotion_id)
        REFERENCES promotions(promotion_id)

);



CREATE INDEX idx_orders_customer
ON orders(customer_id);


CREATE INDEX idx_orders_store
ON orders(store_id);


CREATE INDEX idx_orders_date
ON orders(order_date);




-- ORDER ITEMS
CREATE TABLE IF NOT EXISTS order_items(

    order_item_id VARCHAR(20) PRIMARY KEY,

    order_id VARCHAR(20) NOT NULL,

    product_id VARCHAR(20) NOT NULL,

    quantity INTEGER,

    unit_price NUMERIC(10,2),

    CHECK(quantity > 0),

    CHECK(unit_price >= 0),

    FOREIGN KEY(order_id)
        REFERENCES orders(order_id),

    FOREIGN KEY(product_id)
        REFERENCES products(product_id)

);



CREATE INDEX idx_order_items_order
ON order_items(order_id);


CREATE INDEX idx_order_items_product
ON order_items(product_id);





-- INVENTORY
CREATE TABLE IF NOT EXISTS inventory(

    inventory_id VARCHAR(20) PRIMARY KEY,

    store_id VARCHAR(20) NOT NULL,

    product_id VARCHAR(20) NOT NULL,

    stock_quantity INTEGER,

    last_updated DATE,

    CHECK(stock_quantity >= 0),

    FOREIGN KEY(store_id)
        REFERENCES stores(store_id),

    FOREIGN KEY(product_id)
        REFERENCES products(product_id)

);



CREATE INDEX idx_inventory_store
ON inventory(store_id);


CREATE INDEX idx_inventory_product
ON inventory(product_id);





-- RETURNS
CREATE TABLE IF NOT EXISTS returns(

    return_id VARCHAR(20) PRIMARY KEY,

    order_id VARCHAR(20) NOT NULL,

    product_id VARCHAR(20) NOT NULL,

    return_date DATE,

    reason VARCHAR(200),

    refund_amount NUMERIC(10,2),

    CHECK(refund_amount >= 0),

    FOREIGN KEY(order_id)
        REFERENCES orders(order_id),

    FOREIGN KEY(product_id)
        REFERENCES products(product_id)

);