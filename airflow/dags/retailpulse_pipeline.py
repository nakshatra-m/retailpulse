import sys
from datetime import datetime

# Make RetailPulse source code available to Airflow
sys.path.insert(0, "/opt/airflow/src")

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator


def generate_data():
    from generator.main import main
    main()


def load_data():
    from ingestion.main import main
    main()


def validate_data():
    from validation.validation import run_validation

    success = run_validation()

    if not success:
        raise RuntimeError("RetailPulse data validation failed.")


def transform_data(): 
    from transformations.transform import run_transformations 
    success = run_transformations() 

    if not success: 
        raise RuntimeError( "RetailPulse data transformations failed." )


def run_analytics(): 
    from analytics.analytics import run_analytics 
    success = run_analytics() 

    if not success: 
        raise RuntimeError( "RetailPulse analytics execution failed." )

with DAG(
    dag_id="retailpulse_pipeline",
    description="RetailPulse end-to-end retail data pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["retailpulse", "data-engineering"],
) as dag:

    generate = PythonOperator(
        task_id="generate_data",
        python_callable=generate_data,
    )

    ingest = PythonOperator(
        task_id="load_data",
        python_callable=load_data,
    )

    validate = PythonOperator(
        task_id="validate_data",
        python_callable=validate_data,
    )

    transform = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data,
    )

    analytics = PythonOperator(
        task_id="run_analytics",
        python_callable=run_analytics,
    )

    generate >> ingest >> validate >> transform >> analytics