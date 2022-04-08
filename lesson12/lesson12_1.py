# Создать таблицу со студентами в БД
import os
import sqlite3
from sqlite3 import Error

File_DB = "Students"


def create_connect(path):
    connects = None
    try:
        connects = sqlite3.connect(path)
    except Error:
        print("не конектит")
    return connects


def send_query(connects, query):
    cursor = connects.cursor()
    try:
        cursor.execute(query)
        connects.commit()
    except Error:
        print("Не отправляет данные")


path_dir = os.getcwd()
path = os.path.join(path_dir, File_DB)
connects = create_connect(path)

if __name__ == "__main__":
    create_table_student = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        surname TEXT NOT NULL,
        name TEXT NOT NULL
        );
    """

    fill_table_student = """
    INSERT INTO
        students(surname, name)
    VALUES
        ('Antonov', 'Anton'),
        ('Ivanov', 'Ivan'),
        ('Petrov', 'Petr'),
        ('Sidorov', 'Fedor'),
        ('Fedorov', 'Fedor'),
        ('Vasilev', 'Vasiliy'),
        ('Alekseev', 'Aleksey'),
        ('Aleksandrov', 'Aleksandr'),
        ('Egorov', 'Egor');
    """

    send_query(connects, create_table_student)
    send_query(connects, fill_table_student)
