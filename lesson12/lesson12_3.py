# *Сделать связь таблиц
import lesson12_1

create_table_groups = """
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, 
    classroom INTEGER NOT NULL,
    FOREIGN KEY (classroom) REFERENCES classroom (number) FOREIGN KEY (name) REFERENCES students (group_ID)
    );
"""

fill_table_groups = """
INSERT INTO
    groups (name, classroom)
VALUES
    ('A-20', 201),
    ('B-19', 301),
    ('C-21', 302);
"""

change_table_student_1 = """ALTER TABLE students ADD COLUMN group_ID TEXT;"""

fill_table_student_group_1 = """
UPDATE students
SET group_ID = 'A-20' WHERE id IN (1, 4, 6, 8);"""
fill_table_student_group_2 = """
UPDATE students
SET group_ID = 'B-19' WHERE id IN (2, 5, 9);"""
fill_table_student_group_3 = """
UPDATE students
SET group_ID = 'C-21' WHERE id IN (3, 7);"""

lesson12_1.send_query(lesson12_1.connects, change_table_student_1)
lesson12_1.send_query(lesson12_1.connects, fill_table_student_group_1)
lesson12_1.send_query(lesson12_1.connects, fill_table_student_group_2)
lesson12_1.send_query(lesson12_1.connects, fill_table_student_group_3)
lesson12_1.send_query(lesson12_1.connects, create_table_groups)
lesson12_1.send_query(lesson12_1.connects, fill_table_groups)
