# Главная программа, запускающая проект.
from database.note_operations import *

path_db = 'notes.db'

notes = [
    {
        'username': 'Мария',
        'title': 'Учеба',
        'content': 'Подготовиться к экзамену',
        'status': 'в процессе',
        'created_date': '11-11-2024',
        'issue_date': '13-01-2025'
    },
    {
        'username': 'Владимир',
        'title': 'Работа',
        'content': 'Написать код на Python',
        'status': 'выполнено',
        'created_date': '20-11-2024',
        'issue_date': '02-12-2024'
    },
    {
        'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'created_date': '27-11-2024',
        'issue_date': '30-11-2024'
    }
]

if __name__ == '__main__':
    create_note_db(path_db)
    for note in notes:
        save_note_to_db(note, path_db)
    updates = {'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено', 'issue_date': '26-11-2024'}
    update_note_in_db(2, updates, path_db)
    print('_____Поиск по слову_____')
    print(search_notes_by_keyword('Учеба', path_db))
    print('___Фильтр по статусу___')
    print(filter_notes_by_status('новая', path_db))
    delete_note_from_db(1, path_db)
    print('____После удаления____')
    print(load_notes_from_db(path_db))
