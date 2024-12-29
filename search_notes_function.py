# Функция поиска заметок

notes_ = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе', 'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено', 'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]

def search_notes(notes, keyword=None, status=None):
    ret_notes = []
    if keyword is not None:
        for note in notes:
            if [x for x in ('username', 'title', 'content') if keyword in note[x]] != []:
                ret_notes.append(note)
        notes = ret_notes
    if status is not None:
        ret_notes = []
        for note in notes:
            if status == note['status']:
                ret_notes.append(note)
    return ret_notes

def output_notes(notes):
    if notes == []:
        print('Заметки, соответствующие запросу, не найдены.')
        print()
        return
    print('Найдены заметки:')
    for num, note in enumerate(notes, 1):
        print(f'Заметка №{num}:')
        print('Имя пользователя:', note['username'])
        print('Заголовок:', note['title'])
        print('Описание:', note['content'])
        print('Статус:', note['status'])
        print()

print('Проверка работы функции на пустом списке заметок:')
output_notes(search_notes([], 'keyword'))

print('Поиск по ключевому слову:')
output_notes(search_notes(notes_, keyword='покупок'))

print('Поиск по статусу:')
output_notes(search_notes(notes_, status='в процессе'))

print('Поиск по ключевому слову и статусу:')
output_notes(search_notes(notes_, keyword='работы', status='выполнено'))

