# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT st.id, st.fullname, ROUND(AVG(g.grade), 2) AS average_grade
FROM students as st
JOIN grades AS g ON st.id = g.student_id
GROUP BY st.id
ORDER BY average_grade DESC
LIMIT 5;
"""
print(execute_query(sql))
