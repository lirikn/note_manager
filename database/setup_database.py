# Создание базы данных и таблицы notes

import sqlite3

def create_note_db(db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            status TEXT NOT NULL,
            created_date TEXT NOT NULL,
            issue_date TEXT NOT NULL
        );
    """)
    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_note_db('notes.db')
