# Функция отображения заметок.
from datetime import datetime

def mySort(elem):
    return datetime.strptime(elem['issue_date'], '%d-%m-%Y')

def display_notes(notes):
    if notes == []:
        print('У вас нет сохранённых заметок.')
        return
    print('Список заметок: ')
    print('------------------------')
    for num, note in enumerate(notes, 1):
        print('\t\tЗаметка №', num)
        print('Имя пользователя:', note['name'])
        print('Заголовок:', note['title'])
        print('Описание:', note['content'])
        print('Статус:', note['status'])
        print('Дата создания:', note['created_date'])
        print('Дедлайн:', note['issue_date'])
        print('------------------------')
# вывод 5 заметок на станице
        if num % 5 == 0:
            input('Ввод для продолжения')

# пустой список
notes = []
display_notes(notes)

# одна заметка
input('Ввод для продолжения')
notes.append({
    'name': 'Алексей',
    'title': 'Список покупок',
    'content': 'Купить продукты на неделю',
    'status': 'новая',
    'created_date': '27-11-2024',
    'issue_date': '30-11-2024'
})
display_notes(notes)

# вывод трёх заметок, с сортировкой по дедлайну
input('Ввод для продолжения')
notes.extend([
    {
        'name': 'Мария',
        'title': 'Учеба',
        'content': 'Подготовиться к экзамену',
        'status': 'в процессе',
        'created_date': '11-11-2024',
        'issue_date': '13-01-2025'
    },
    {
        'name': 'Владимир',
        'title': 'Работа',
        'content': 'Написать код на Python',
        'status': 'выполнено',
        'created_date': '20-11-2024',
        'issue_date': '02-12-2024'
    }
])
notes.sort(key=mySort)
display_notes(notes)

input('Ввод для продолжения')
# большой масив данных
display_notes(notes*4)
