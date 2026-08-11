from pathlib import Path
import re
import sys

from sqlalchemy import text

from src.config.database import engine


TRANSFORMATION_SQL = Path("sql/transformations.sql")


def load_transformation_queries():
    """
    Load transformation SQL and split it into
    individual SQL statements.
    """

    if not TRANSFORMATION_SQL.exists():
        raise FileNotFoundError(
            f"Transformation SQL file not found: {TRANSFORMATION_SQL}"
        )

    sql = TRANSFORMATION_SQL.read_text(
        encoding="utf-8"
    )

    # Remove single-line SQL comments.
    sql = re.sub(
        r"(?m)^\s*--.*$",
        "",
        sql
    )

    # Split SQL into individual statements.
    queries = [
        query.strip()
        for query in sql.split(";")
        if query.strip()
    ]

    return queries


def run_transformations():
    """
    Execute all RetailPulse transformation queries.

    All transformations run inside a single transaction.
    If any query fails, the transaction is rolled back.
    """

    print("=" * 60)
    print("RetailPulse Data Transformations")
    print("=" * 60)

    try:
        queries = load_transformation_queries()

        print(
            f"Loaded {len(queries)} transformation queries."
        )
        print()

        with engine.begin() as connection:

            for index, query in enumerate(
                queries,
                start=1
            ):
                print(
                    f"Transformation Query {index}"
                )
                print("-" * 60)

                try:
                    connection.execute(
                        text(query)
                    )

                    print("[PASS]")
                    print()

                except Exception as error:
                    print("[FAIL]")
                    print(f"Error: {error}")
                    print()

                    # Raise the exception so that
                    # engine.begin() rolls back the
                    # entire transaction.
                    raise

        print("=" * 60)
        print("TRANSFORMATION SUMMARY")
        print("=" * 60)
        print(
            f"Queries executed: {len(queries)}"
        )
        print(
            f"Passed: {len(queries)}"
        )
        print("Failed: 0")
        print()
        print("TRANSFORMATION RESULT: PASSED")
        print("=" * 60)

        return True

    except Exception as error:

        print("=" * 60)
        print("TRANSFORMATION SUMMARY")
        print("=" * 60)
        print("TRANSFORMATION RESULT: FAILED")
        print()
        print(f"Error: {error}")
        print("=" * 60)

        return False


if __name__ == "__main__":
    success = run_transformations()

    if not success:
        sys.exit(1)

