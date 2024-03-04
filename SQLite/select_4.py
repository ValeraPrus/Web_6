# Знайти середній бал на потоці (по всій таблиці оцінок).

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT ROUND(AVG(grade), 2)
FROM grades
LIMIT 1;
"""
print(execute_query(sql))
