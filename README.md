# RetailPulse — Retail Analytics Pipeline & Power BI Dashboard

RetailPulse is a project I built to bring together the different parts of a data workflow in one place. It starts with generating realistic retail data, loads that data into PostgreSQL, validates and transforms it, runs the workflow through Airflow, and finishes with an interactive Power BI dashboard.

The idea was straightforward: create a realistic retail dataset and build the kind of pipeline an analytics or data team could use to turn raw transactions into useful business information.

---

## What is RetailPulse?

RetailPulse simulates a Canadian retail business operating across multiple cities. I generated the data myself so that I could control the size and structure of the dataset while still working with the kinds of relationships and problems you would expect in a retail environment.

The project covers:

* Stores
* Products
* Customers
* Orders
* Order Items
* Inventory
* Promotions
* Returns

The raw data is loaded into PostgreSQL, transformed with SQL into analytics-ready tables, validated, and then used by Power BI for reporting and analysis.

### The flow


Python Data Generator
        ↓
Raw CSV Data
        ↓
PostgreSQL
        ↓
Data Validation
        ↓
SQL Transformations
        ↓
Analytics Tables
        ↓
Apache Airflow
        ↓
Power BI Dashboard


---

## Why I Built It

I wanted RetailPulse to be more than just a Power BI dashboard. My goal was to build the complete path from raw data to a business-facing report and understand what happens at each stage along the way.

From a business perspective, the dashboard answers questions such as:

* Sales performance
* Order volume
* Units sold
* Gross profit
* Refunds
* Average order value
* Store performance
* Product performance
* Customer performance
* Inventory activity

I also added validation and reconciliation checks so that the numbers shown in Power BI can be checked against the PostgreSQL analytics layer instead of simply assuming the dashboard is correct.

---

## Architecture


                    ┌──────────────────────┐
                    │   Python Generator   │
                    │                      │
                    │ Stores               │
                    │ Products             │
                    │ Customers            │
                    │ Orders               │
                    │ Inventory            │
                    │ Promotions           │
                    │ Returns              │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Raw CSVs        │
                    │      data/raw        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     PostgreSQL       │
                    │                      │
                    │ Raw / operational    │
                    │ tables               │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  SQL Transformations │
                    │                      │
                    │ Business logic       │
                    │ Aggregations         │
                    │ Analytics models     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Analytics Tables   │
                    │                      │
                    │ Daily Sales          │
                    │ Product Performance  │
                    │ Store Performance    │
                    │ Customer Performance │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Apache Airflow    │
                    │    Orchestration     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Power BI        │
                    │ Interactive Dashboard│
                    └──────────────────────┘


---

## Tools I Used

| Technology     | What I used it for                                 |
| -------------- | -------------------------------------------------- |
| Python         | Data generation, ingestion and pipeline logic      |
| PostgreSQL     | Relational database and analytical storage         |
| SQL            | Data transformation and analytics                  |
| Docker         | Containerized database and pipeline infrastructure |
| Apache Airflow | Workflow orchestration                             |
| Power BI       | Interactive business intelligence dashboard        |
| Pandas         | Data processing                                    |
| SQLAlchemy     | PostgreSQL connectivity                            |
| Git/GitHub     | Version control and project management             |

---

## Project Structure

### `.github/`
Contains GitHub-related configuration and workflow files.

### `airflow/`
Contains the Apache Airflow orchestration setup.

- `dags/retailpulse_pipeline.py` — Main Airflow DAG that orchestrates the pipeline.
- `Dockerfile` — Docker configuration for the Airflow environment.
- `requirements.txt` — Python dependencies required by Airflow.

### `dashboard/`
Contains the Power BI dashboard.

- `retail pulse analysis.pbix` — Final Power BI report containing the retail analytics dashboard and KPI measures.

### `data/`
Contains the datasets used throughout the project.

- `raw/` — Generated raw CSV datasets before processing.
- `processed/` — Processed datasets produced during the pipeline.

### `docs/`
Contains project documentation, development notes, database documentation, and screenshots.

### `logs/`
Contains runtime and Airflow execution logs generated during development and testing.

### `notebooks/`
Contains notebooks used for exploratory analysis and development.

### `sql/`
Contains the SQL logic used throughout the database and analytics layers.

- `schema.sql` — Defines the PostgreSQL database schema.
- `analytics.sql` — Contains analytics queries and analytical table logic.
- `transformations.sql` — Contains SQL transformations used to prepare reporting data.
- `validation.sql` — Contains SQL validation and data-quality checks.

### `src/`
Contains the main Python application code.

#### `src/analytics/`
Contains analytics calculations and analytics validation logic.

- `analytics.py` — Builds and processes analytical datasets.
- `analytics_validation.py` — Performs checks on analytical results.

#### `src/config/`
Contains project and database configuration.

- `config.py` — Application configuration.
- `database.py` — PostgreSQL database connection setup.

#### `src/generator/`
Generates the synthetic retail data used by the project.

- `customer_generator.py` — Generates customer data.
- `inventory_generator.py` — Generates inventory data.
- `main.py` — Main entry point for data generation.
- `order_generator.py` — Generates order data.
- `product_generator.py` — Generates product data.
- `promotion_generator.py` — Generates promotion data.
- `returns_generator.py` — Generates return data.
- `store_generator.py` — Generates store data.

#### `src/ingestion/`
Loads the generated CSV files into PostgreSQL.

- `load_customers.py` — Loads customer data.
- `load_inventory.py` — Loads inventory data.
- `load_orders.py` — Loads order data.
- `load_order_items.py` — Loads order-item data.
- `load_products.py` — Loads product data.
- `load_promotions.py` — Loads promotion data.
- `load_returns.py` — Loads return data.
- `load_stores.py` — Loads store data.
- `main.py` — Main ingestion entry point.

#### `src/transformations/`
Contains Python-based transformation logic.

- `transform.py` — Runs the required data transformations.

#### `src/validation/`
Contains data-quality validation logic.

- `validation.py` — Validates the loaded data and checks expected results.

### `tests/`
Contains project test files.

### `docker-compose.yml`
Defines the Docker services used to run the project's infrastructure.

### `requirements.txt`
Contains the Python dependencies required by the project.

### `README.md`
Contains the project overview, architecture, setup instructions, pipeline explanation, challenges, and documentation.

### `.gitignore`
Defines files and folders that should not be committed to Git, including environment files, virtual environments, cache files, and generated runtime files.

The repository also contains local development folders such as `.venv/` and generated Airflow logs. These are environment or runtime files rather than part of the application logic and are excluded from the portfolio structure above.

---

# How the Pipeline Works

I broke the pipeline into a few clear stages so that each part has a specific job.

### 1. Generate the data

Python scripts generate the simulated retail data.

The current dataset contains:

* 8 stores
* 100 products
* 500 customers
* 5,000 orders
* 15,023 order items
* 800 inventory records
* 30 promotions
* 250 returns

The generated files are stored as CSV data before being loaded into the database.

---

### 2. Load it into PostgreSQL

The CSV datasets are loaded into PostgreSQL, which acts as the main storage and analytics database for the project.

* Customers
* Products
* Stores
* Orders
* Order Items
* Inventory
* Promotions
* Returns

---

### 3. Validate the data

Before relying on the data for reporting, I run validation checks to make sure the expected tables and records are present.

Example validation results:

| Dataset     | Records |
| ----------- | ------: |
| Customers   |     500 |
| Inventory   |     800 |
| Order Items |  15,023 |
| Orders      |   5,000 |
| Products    |     100 |
| Promotions  |      30 |
| Returns     |     250 |
| Stores      |       8 |

### Validation Summary


Passed: 7
Failed: 0

This gives me a basic quality check before the data moves further down the pipeline.

---

# Analytics Layer

Once the data is in PostgreSQL, SQL transformations turn the transactional data into smaller, reporting-friendly analytics tables.

The project produces analytical tables including:

### `analytics_daily_sales`

This table is used to look at sales trends over time.

### `analytics_product_performance`

This table brings together information used to understand:

* Units sold
* Sales revenue
* Gross profit
* Refunds
* Inventory

### `analytics_store_performance`

This table is used to compare stores and their performance.

### `analytics_customer_performance`

This table is used to understand customer purchasing activity and performance.

Keeping these analytics tables separate from the raw transactional tables makes the Power BI layer easier to work with and keeps the business logic in the database where it can be tested independently.

---

# Power BI & KPIs

The Power BI dashboard brings the analytics tables together into an interactive report. The main KPIs I created are:

| KPI                 | Description                     |
| ------------------- | ------------------------------- |
| Total Sales         | Total gross sales generated     |
| Net Sales           | Sales after applicable refunds  |
| Total Orders        | Total number of customer orders |
| Units Sold          | Total quantity of products sold |
| Refunds             | Total refunded sales amount     |
| Gross Profit        | Profit generated from sales     |
| Average Order Value | Average sales value per order   |

The measures are created in Power BI using DAX. I also compared the dashboard results with PostgreSQL queries to make sure the numbers were lining up with the source analytics tables.

---

# Dashboard

The dashboard is the business-facing part of RetailPulse. It sits on top of the PostgreSQL analytics layer and turns the processed data into visuals that are easier to explore and understand.

The dashboard supports analysis of:

* Sales trends
* Store performance
* Product performance
* Customer performance
* Order activity
* Refunds
* Gross profit
* Average order value

The report includes filters and slicers so the data can be explored across different business dimensions.

## Dashboard Preview

![RetailPulse Dashboard](screenshots/retailpulse anlysis.png)

---

# Airflow Orchestration

I also added Apache Airflow so the pipeline is not just a collection of scripts that have to be run manually. The main DAG ties the different stages together into a repeatable workflow.

The main DAG is:

retailpulse_pipeline


The pipeline contains the following tasks:


generate_data
      ↓
load_data
      ↓
run_analytics
      ↓
transform_data
      ↓
validate_data


Airflow gives me one place to trigger, monitor, and troubleshoot the pipeline.

---

# Docker

I used Docker to keep PostgreSQL and Airflow services consistent and easy to start locally. This also made it easier to reproduce the development environment instead of relying on a database installation that is specific to my machine.

The primary infrastructure configuration is defined in:


docker-compose.yml


---

# Running the Project

### Prerequisites

Install:

* Python 3.x
* Docker Desktop
* Git
* Power BI Desktop

---

### 1. Clone the repository


git clone <YOUR_GITHUB_REPOSITORY_URL>
cd retailpulse

---

### 2. Create a Python virtual environment

Windows:


python -m venv .venv


Activate it:


.venv\Scripts\activate


---

### 3. Install the dependencies


pip install -r requirements.txt


---

### 4. Configure environment variables

Create a `.env` file containing the PostgreSQL connection settings required by the project.

Example:

POSTGRES_USER=retailpulse
POSTGRES_PASSWORD=<your_password>
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
POSTGRES_DB=retailpulse


Do not commit `.env` to GitHub.

---

### 5. Start Docker services


docker compose up -d


Check running containers:

docker ps


---

### 6. Run the pipeline

The pipeline can be run through the configured Airflow DAG.

Open the Airflow interface and trigger:

retailpulse_pipeline


The DAG runs the configured generation, ingestion, analytics, transformation, and validation stages.

---

### 7. Open Power BI

Open the Power BI file located in:


dashboard/retail pulse analysis.pbix


The Power BI dashboard connects to the PostgreSQL analytics layer.

---

# Validation & Reconciliation

One of the parts of the project I paid particular attention to was making sure the dashboard numbers were trustworthy.

PostgreSQL analytical tables were queried independently and compared with Power BI results.

I compared PostgreSQL results with Power BI results to verify that:

* SQL transformations are producing expected results.
* Power BI is connected to the correct analytical tables.
* DAX measures are calculating expected values.
* Dashboard KPIs match the underlying database results.

---

# What I Learned From This Project

### Building an end-to-end pipeline

I connected data generation, ingestion, transformation, validation, orchestration, and reporting into one workflow rather than treating each part as a separate exercise.

### Working with SQL and data models

I used SQL transformations and aggregations to turn transactional data into analytics-ready tables that were easier to use in Power BI.

### Checking data quality

I added validation checks and compared database results with Power BI metrics instead of assuming that the dashboard numbers were correct.

### Understanding orchestration

I used Apache Airflow to organize the different pipeline stages into a repeatable workflow and make the process easier to monitor.

### Turning data into something useful

I built an interactive Power BI dashboard with KPI measures, filters, and analytical views that make the underlying data easier to explore.

### Working with Docker

I used Docker to simplify the local PostgreSQL and Airflow setup and make the development environment easier to reproduce.

---

# What I Would Add Next

If I continued developing RetailPulse, the next improvements I would make are:

* Cloud deployment using Azure or AWS
* Incremental data loading
* dbt-based transformation models
* Automated data-quality testing
* CI/CD using GitHub Actions
* Scheduled Power BI refresh
* Real-time retail data ingestion
* More advanced customer segmentation
* Sales forecasting
* Inventory demand forecasting

---

# About the Project

RetailPulse was built as a hands-on project to strengthen my experience across data engineering, analytics, databases, orchestration, and business intelligence.

**Nakshatra Murali**
Master of Applied Computing, Wilfrid Laurier University

GitHub: https://github.com/nakshatra-m?tab=repositories
LinkedIn: https://www.linkedin.com/in/nakshatra-murali-4305171b8/
