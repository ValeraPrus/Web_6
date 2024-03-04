# Список курсів, які певному студенту читає певний викладач.

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT su.name
FROM subjects as su
JOIN grades AS gr ON su.id = gr.subject_id
WHERE gr.student_id = 1
AND su.teacher_id = 1
GROUP BY su.id;
"""
print(execute_query(sql))
