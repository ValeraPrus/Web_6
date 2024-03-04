# Знайти середній бал, який ставить певний викладач зі своїх предметів.

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT te.fullname AS teacher, su.name AS subject, ROUND(AVG(gr.grade), 2)
FROM teachers as te
JOIN subjects AS su ON te.id = su.teacher_id
JOIN grades AS gr ON su.id = gr.subject_id
WHERE te.id = 1
GROUP BY te.fullname, su.name;
"""
print(execute_query(sql))
