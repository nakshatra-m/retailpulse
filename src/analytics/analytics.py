
from pathlib import Path
import re
import sys

from sqlalchemy import text

from src.config.database import engine


ANALYTICS_SQL = Path("sql/analytics.sql")


def load_analytics_queries():
    """
    Load analytics SQL and split it into individual
    SQL statements.
    """

    if not ANALYTICS_SQL.exists():
        raise FileNotFoundError(
            f"Analytics SQL file not found: {ANALYTICS_SQL}"
        )

    sql = ANALYTICS_SQL.read_text(
        encoding="utf-8"
    )

    # Remove single-line SQL comments.
    sql = re.sub(
        r"(?m)^\s*--.*$",
        "",
        sql
    )

    # Split SQL statements.
    queries = [
        query.strip()
        for query in sql.split(";")
        if query.strip()
    ]

    return queries


def run_analytics():
    """
    Execute RetailPulse analytics queries
    and print the results.
    """

    print("=" * 60)
    print("RetailPulse Business Analytics")
    print("=" * 60)

    try:
        queries = load_analytics_queries()

        print(
            f"Loaded {len(queries)} analytics queries."
        )
        print()

        with engine.connect() as connection:

            for index, query in enumerate(
                queries,
                start=1
            ):
                print(
                    f"Analytics Query {index}"
                )
                print("-" * 60)

                try:
                    result = connection.execute(
                        text(query)
                    )

                    rows = result.fetchall()
                    columns = list(result.keys())

                    if not rows:
                        print("No results.")
                    else:
                        for row in rows:
                            print(
                                dict(
                                    zip(
                                        columns,
                                        row
                                    )
                                )
                            )

                    print()
                    print("[PASS]")
                    print()

                except Exception as error:
                    print("[FAIL]")
                    print(f"Error: {error}")
                    print()

                    raise

        print("=" * 60)
        print("ANALYTICS SUMMARY")
        print("=" * 60)
        print(
            f"Queries executed: {len(queries)}"
        )
        print(
            f"Passed: {len(queries)}"
        )
        print("Failed: 0")
        print()
        print("ANALYTICS RESULT: PASSED")
        print("=" * 60)

        return True

    except Exception as error:

        print("=" * 60)
        print("ANALYTICS SUMMARY")
        print("=" * 60)
        print("ANALYTICS RESULT: FAILED")
        print()
        print(f"Error: {error}")
        print("=" * 60)

        return False


if __name__ == "__main__":
    success = run_analytics()

    if not success:
        sys.exit(1)
