# RetailPulse Data Model

## Overview

RetailPulse simulates a Canadian retail chain.
The data model represents customers, stores, products,
sales transactions, promotions, inventory, and returns.

---

# Tables

## Customers

Stores customer information.

| Column | Data Type | Description |
|---|---|---|
| customer_id | VARCHAR | Unique customer identifier |
| first_name | VARCHAR | Customer first name |
| last_name | VARCHAR | Customer last name |
| email | VARCHAR | Customer email |
| city | VARCHAR | Customer city |
| province | VARCHAR | Customer province |
| signup_date | DATE | Account creation date |
| loyalty_level | VARCHAR | Bronze/Silver/Gold |

Primary Key:

customer_id


---

## Stores

Stores retail location information.

| Column | Data Type | Description |
|---|---|---|
| store_id | VARCHAR | Unique store identifier |
| store_name | VARCHAR | Store name |
| city | VARCHAR | Store city |
| province | VARCHAR | Store province |
| opening_date | DATE | Store opening date |

Primary Key:

store_id


---

## Products

Stores product catalogue information.

| Column | Data Type | Description |
|---|---|---|
| product_id | VARCHAR | Unique product identifier |
| product_name | VARCHAR | Product name |
| category | VARCHAR | Product category |
| brand | VARCHAR | Product brand |
| price | DECIMAL | Product price |
| supplier | VARCHAR | Supplier name |

Primary Key:

product_id


---

## Orders

Stores customer transactions.

| Column | Data Type | Description |
|---|---|---|
| order_id | VARCHAR | Unique order identifier |
| customer_id | VARCHAR | Customer reference |
| store_id | VARCHAR | Store reference |
| order_date | DATE | Purchase date |
| payment_method | VARCHAR | Payment type |
| order_status | VARCHAR | Completed/Returned |

Primary Key:

order_id

Foreign Keys:

customer_id → Customers

store_id → Stores


---

## Order Items

Stores products inside each order.

| Column | Data Type | Description |
|---|---|---|
| order_item_id | VARCHAR | Unique item identifier |
| order_id | VARCHAR | Order reference |
| product_id | VARCHAR | Product reference |
| quantity | INTEGER | Quantity purchased |
| unit_price | DECIMAL | Price at purchase |
| discount | DECIMAL | Discount applied |

Primary Key:

order_item_id

Foreign Keys:

order_id → Orders

product_id → Products


---

## Promotions

Stores discount campaigns.

| Column | Data Type | Description |
|---|---|---|
| promotion_id | VARCHAR | Promotion identifier |
| promotion_name | VARCHAR | Campaign name |
| start_date | DATE | Start date |
| end_date | DATE | End date |
| discount_percentage | FLOAT | Discount percentage |


---

## Inventory

Tracks product stock.

| Column | Data Type | Description |
|---|---|---|
| inventory_id | VARCHAR | Inventory identifier |
| store_id | VARCHAR | Store reference |
| product_id | VARCHAR | Product reference |
| stock_quantity | INTEGER | Available stock |
| last_updated | DATE | Update date |

Foreign Keys:

store_id → Stores

product_id → Products


---

## Returns

Tracks returned products.

| Column | Data Type | Description |
|---|---|---|
| return_id | VARCHAR | Return identifier |
| order_id | VARCHAR | Original order |
| product_id | VARCHAR | Returned product |
| return_date | DATE | Return date |
| reason | VARCHAR | Return reason |

Foreign Keys:

order_id → Orders

product_id → Products


---

# Relationships

Customers

1 Customer

↓

Many Orders


Stores

1 Store

↓

Many Orders


Orders

1 Order

↓

Many Order Items


Products

1 Product

↓

Many Order Items


Stores + Products

↓

Inventory Records