from pathlib import Path
import re
import sys

from sqlalchemy import text

from src.config.database import engine


VALIDATION_SQL = Path("sql/validation.sql")


def load_validation_queries():
    """
    Load validation SQL and split it into individual SQL statements.
    SQL comments are removed before splitting.
    """

    if not VALIDATION_SQL.exists():
        raise FileNotFoundError(
            f"Validation SQL file not found: {VALIDATION_SQL}"
        )

    sql = VALIDATION_SQL.read_text(encoding="utf-8")

    # Remove single-line SQL comments.
    sql = re.sub(r"(?m)^\s*--.*$", "", sql)

    # Split individual SQL statements.
    queries = [
        query.strip()
        for query in sql.split(";")
        if query.strip()
    ]

    return queries


def run_validation():
    """
    Execute all RetailPulse validation queries.
    """

    print("=" * 60)
    print("RetailPulse Data Validation")
    print("=" * 60)

    try:
        queries = load_validation_queries()

        print(f"Loaded {len(queries)} validation queries.")
        print()

        passed = 0
        failed = 0

        with engine.connect() as connection:

            for index, query in enumerate(queries, start=1):

                try:
                    result = connection.execute(text(query))

                    rows = result.fetchall()
                    columns = list(result.keys())

                    print(f"Validation Query {index}")
                    print("-" * 60)

                    for row in rows:
                        print(dict(zip(columns, row)))

                    # Determine whether this validation failed.
                    if "invalid_rows" in columns:
                        invalid_index = columns.index("invalid_rows")

                        query_failed = any(
                            row[invalid_index] != 0
                            for row in rows
                        )

                    elif "duplicate_groups" in columns:
                        duplicate_index = columns.index(
                            "duplicate_groups"
                        )

                        query_failed = any(
                            row[duplicate_index] != 0
                            for row in rows
                        )

                    else:
                        # Row-count validation and other informational
                        # queries are considered successfully executed.
                        query_failed = False

                    if query_failed:
                        print("[FAIL]")
                        failed += 1
                    else:
                        print("[PASS]")
                        passed += 1

                    print()

                except Exception as error:
                    print(f"[FAIL] Query {index}")
                    print(f"Error: {error}")
                    print()
                    failed += 1

        print("=" * 60)
        print("VALIDATION SUMMARY")
        print("=" * 60)
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print()

        if failed == 0:
            print("VALIDATION RESULT: PASSED")
            print("=" * 60)
            return True

        print("VALIDATION RESULT: FAILED")
        print("=" * 60)
        return False

    except Exception as error:
        print("VALIDATION ERROR")
        print(error)
        return False


if __name__ == "__main__":
    success = run_validation()

    if not success:
        sys.exit(1)