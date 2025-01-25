# Операции с базой данных notes
import sqlite3
from database.setup_database import *

# Сохраняет заметку в таблицу notes
def save_note_to_db(note, db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO notes (
            username, title, content, status, created_date, issue_date)
        VALUES (?, ?, ?, ?, ?, ?);
    """, (
        note['username'],
        note['title'],
        note['content'],
        note['status'],
        note['created_date'],
        note['issue_date']
    ))
    connection.commit()
    connection.close()

# Загрузка всех заметок
def load_notes_from_db(db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM notes;")
    rows = cursor.fetchall()
    notes = []
    for row in rows:
        notes.append({
            'id': row[0],
            'username': row[1],
            'title': row[2],
            'content': row[3],
            'status': row[4],
            'created_date': row[5],
            'issue_date': row[6],
        })
    connection.close()
    return notes

# Удаление заметок
def delete_note_from_db(note_id, db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?;", (note_id,))
    connection.commit()
    connection.close()

# Обновления заметок
def update_note_in_db(note_id, updates, db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE notes
        SET title = ?, content = ?, status = ?, issue_date = ?
        WHERE id = ?;
    """, (updates['title'], updates['content'], updates['status'], updates['issue_date'], note_id))
    connection.commit()
    connection.close()

# Поиск заметок
def search_notes_by_keyword(keyword, db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM notes
        WHERE title LIKE ? OR content LIKE ?;
    """, (f"%{keyword}%", f"%{keyword}%")
    )
    rows = cursor.fetchall()
    connection.close()
    return [{
            'id': row[0],
            'username': row[1],
            'title': row[2],
            'content': row[3],
            'status': row[4],
            'created_date': row[5],
            'issue_date': row[6]
        } for row in rows
    ]

# Фильтрация заметок
def filter_notes_by_status(status, db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM notes WHERE status = ?;",(status,))
    rows = cursor.fetchall()
    connection.close()
    return [{
            'id': row[0],
            'username': row[1],
            'title': row[2],
            'content': row[3],
            'status': row[4],
            'created_date': row[5],
            'issue_date': row[6]
        } for row in rows
    ]


if __name__ == '__main__':
    create_note_db('notes.db')
    note = {
        'username': 'Мария',
        'title': 'Учеба',
        'content': 'Подготовиться к экзамену',
        'status': 'в процессе',
        'created_date': '11-11-2024',
        'issue_date': '13-01-2025'
    }
    save_note_to_db(note, 'notes.db')
    print(filter_notes_by_status('в процессе', 'notes.db'))
    delete_note_from_db(1, 'notes.db')