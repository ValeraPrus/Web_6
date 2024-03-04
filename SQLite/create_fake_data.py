import faker
from random import randint, choice
import sqlite3

STUDENTS = 30
GROUPS = 3
SUBJECTS = 6
TEACHERS = 3

fake = faker.Faker('uk-Ua')
subjects = ['Математика', 'Фізика', 'Хімія', 'Біологія', 'Історія', 'Література', 'Англійська', 'Філософія']

with sqlite3.connect('tables.db') as con:
    cur = con.cursor()

    for _ in range(GROUPS):
        cur.execute('INSERT INTO groups (name) VALUES (?)', (fake.word(),))

    for _ in range(TEACHERS):
        cur.execute('INSERT INTO teachers (fullname) VALUES (?)', (fake.name(),))

    for teacher_id in range(1, 4):
        for _ in range(2):
            fake_sub = choice(subjects)
            cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (fake_sub, teacher_id))
            subjects.remove(fake_sub)
    for group_id in range(1, 4):
        for _ in range(10):
            cur.execute("INSERT INTO students (fullname, group_id) VALUES (?, ?) RETURNING id", (fake.name(), group_id))
            student_id = cur.fetchone()[0]
            for subject_id in range(1, 7):
                for _ in range(3):
                    cur.execute("INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)", 
                                (student_id, subject_id, randint(0, 100), fake.date_this_decade())
                                )

    con.commit()
