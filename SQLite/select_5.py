# Знайти які курси читає певний викладач.

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT te.id, te.fullname, su.name
FROM teachers as te
JOIN subjects AS su ON te.id = su.teacher_id
WHERE te.id = 1;
"""
print(execute_query(sql))
