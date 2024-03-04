# Знайти оцінки студентів у окремій групі з певного предмета.

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT st.fullname, gr.grade
FROM students as st
JOIN grades AS gr ON st.id = gr.student_id
WHERE st.group_id = 1
AND gr.subject_id = 1;
"""
print(execute_query(sql))
