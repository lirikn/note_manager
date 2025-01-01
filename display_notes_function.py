# Функция отображения заметок.
from datetime import datetime

def my_sort(elem):
    return datetime.strptime(elem['issue_date'], '%d-%m-%Y')

def display_notes(notes):
    if not notes:
        print('Заметки не найдены.')
        return
    print('Список заметок: ')
    print('------------------------')
    for num, note in enumerate(notes, 1):
        print('\t\tЗаметка №', num)
        print('Имя пользователя:', note['username'])
        print('Заголовок:', note['title'])
        print('Описание:', note['content'])
        print('Статус:', note['status'])
        print('Дата создания:', note['created_date'])
        print('Дедлайн:', note['issue_date'])
        print('------------------------')
# вывод 5 заметок на станице
        if num % 5 == 0:
            input('Ввод для продолжения')

if __name__ == "__main__":
    # пустой список
    notes_ = []
    display_notes(notes_)

    # одна заметка
    input('Ввод для продолжения')
    notes_.append({
        'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'created_date': '27-11-2024',
        'issue_date': '30-11-2024'
    })
    display_notes(notes_)

    # вывод трёх заметок, с сортировкой по дедлайну
    input('Ввод для продолжения')
    notes_.extend([
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
        }
    ])
    notes_.sort(key=my_sort)
    display_notes(notes_)

    input('Ввод для продолжения')
    # большой масив данных
    display_notes(notes_*4)
