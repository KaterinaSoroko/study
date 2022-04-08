# Создать таблицу аудиторий в БД
import lesson12_1


create_table_classroom = """
CREATE TABLE IF NOT EXISTS classroom (
    number INTEGER PRIMARY KEY,
    appointment TEXT NOT NULL,
    subject TEXT,
    professor TEXT 
    );
"""

fill_table_classroom = """
INSERT INTO
    classroom(number, appointment, subject, professor)
VALUES
    (101, 'lecture', 'geography', 'Bering'),
    (102, 'laboratory', 'informatics', 'Guido van Rossum'),
    (201, 'practical', 'literature', 'Dostoevsky'),
    (202, 'lecture', 'maths', 'Fourier'),
    (301, 'practical', 'geography', 'Columbus'),
    (302, 'practical', 'maths', 'Pythagoras');
"""

lesson12_1.send_query(lesson12_1.connects, create_table_classroom)
lesson12_1.send_query(lesson12_1.connects, fill_table_classroom)
