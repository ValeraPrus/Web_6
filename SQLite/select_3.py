# Знайти середній бал у групах з певного предмета.

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT st.group_id, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades AS g
JOIN students AS st ON st.id = g.student_id
WHERE g.subject_id = 1
GROUP BY st.group_id
ORDER BY st.group_id;
"""
print(execute_query(sql))
