# Знайти список курсів, які відвідує студент.

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT su.name
FROM grades as gr
JOIN subjects AS su ON su.id = gr.subject_id
WHERE gr.student_id = 30
GROUP BY su.id;
"""
print(execute_query(sql))
