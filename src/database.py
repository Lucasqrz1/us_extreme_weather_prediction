"""
database.py
-----------
Reusable functions for connecting to and querying the project SQLite database.
Used by all notebooks in this project.
"""

import sqlite3
import pandas as pd
from pathlib import Path

# Path to the database file (relative to project root)
DB_PATH = Path(__file__).resolve().parent.parent / "data" / "processed" / "weather.db"


def get_connection() -> sqlite3.Connection:
    """Return a connection to the SQLite database."""
    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"Database not found at {DB_PATH}. "
            "Please run notebook 00_database_setup.ipynb first."
        )
    return sqlite3.connect(DB_PATH)


def query(sql: str, params: tuple = ()) -> pd.DataFrame:
    """
    Run a SQL query and return the result as a DataFrame.

    Parameters
    ----------
    sql : str
        SQL query string.
    params : tuple, optional
        Parameters to pass to the query (for safe value injection).

    Returns
    -------
    pd.DataFrame
    """
    conn = get_connection()
    try:
        df = pd.read_sql_query(sql, conn, params=params)
    finally:
        conn.close()
    return df


def list_tables() -> list:
    """Return a list of all table names in the database."""
    conn = get_connection()
    try:
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
    finally:
        conn.close()
    return tables


def table_info(table_name: str) -> pd.DataFrame:
    """Return column names and types for a given table."""
    return query(f"PRAGMA table_info({table_name});")