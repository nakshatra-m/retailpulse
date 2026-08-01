import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text


load_dotenv()


DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)


engine = create_engine(
    DATABASE_URL,
    echo=True
)


def test_connection():

    try:

        with engine.connect() as connection:

            result = connection.execute(
                text("SELECT current_database();")
            )

            print("Database connection successful")
            print(
                "Connected database:",
                result.fetchone()[0]
            )

    except Exception as e:

        print("Database connection failed")
        print(e)


if __name__ == "__main__":
    test_connection()