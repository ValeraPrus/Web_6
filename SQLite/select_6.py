# Знайти список студентів у певній групі.

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT st.id, st.fullname
FROM groups as gr
JOIN students AS st ON gr.id = st.group_id
WHERE st.group_id = 1
GROUP BY st.id;
"""
print(execute_query(sql))
