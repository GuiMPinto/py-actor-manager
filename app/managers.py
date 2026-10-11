import sqlite3

from app.models import Actor


def __init__(self, db_name, table_name):
    self.db_name = db_name
    self.table_name = table_name
    self.connection = sqlite3.connect(db_name)
    self._create_table()
def _create_table(self):
    query = f"""
    CREATE TABLE IF NOT EXISTS {self.table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL
    )
    """
    self.connection.execute(query)
    self.connection.commit()
