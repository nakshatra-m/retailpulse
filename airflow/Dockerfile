FROM apache/airflow:3.0.4

USER root

RUN pip install --no-cache-dir \
    Faker==40.36.0 \
    pandas==3.0.1 \
    SQLAlchemy==2.0.51 \
    psycopg2-binary==2.9.12 \
    python-dotenv==1.1.1

USER airflow