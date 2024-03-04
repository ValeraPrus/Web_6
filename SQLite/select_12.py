# Оцінки студентів у певній групі з певного предмета на останньому занятті.

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
WITH StudentGrades AS (
SELECT st.group_id, su.name AS subject, gr.grade_date, gr.grade,
max(gr.grade_date) over (partition by st.group_id, su.id) AS last_lesson_date
FROM grades AS gr
JOIN students AS st ON st.id = gr.student_id
JOIN subjects AS su ON su.id = gr.subject_id
WHERE st.group_id = 1
AND su.id = 1)
SELECT group_id, subject, grade_date, grade
FROM StudentGrades
WHERE grade_date = last_lesson_date;
"""
print(execute_query(sql))
