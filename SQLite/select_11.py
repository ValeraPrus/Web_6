# Середній бал, який певний викладач ставить певному студентові.

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT te.fullname, st.fullname, ROUND(AVG(gr.grade), 2)
FROM grades as gr
JOIN students AS st ON st.id = gr.student_id
JOIN subjects AS su ON su.id = gr.subject_id
JOIN teachers AS te ON te.id = su.teacher_id
WHERE gr.student_id = 1
AND te.id = 1
GROUP BY st.fullname, te.fullname;
"""
print(execute_query(sql))
