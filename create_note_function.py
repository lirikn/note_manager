# Пример функции для создания новой заметки и возврата словаря.
from datetime import datetime, timedelta

def input_check(text):
    while True:
        ret = input(f'Введите {text}: ')
        if ret != '':
            return ret
        print('Ввод не может быть пустым')

def input_status(stats):
    while True:
        status = input(f'Введите статус заметки {stats}: ')
        if status in stats:
            return status
        print('Неправильный статус -', status)

def input_date(days):
    default = datetime.now() + timedelta(days=days)
    while True:
        date = input(f'Введите дату дедлайна (по умолчанию {default.strftime("%d-%m-%Y")}):')
        if date == '':
            return default
        try:
            date = datetime.strptime(date, '%d-%m-%Y')
        except:
            print('Убедитесь, что вводите дату в формате день-месяц-год, например: 10-12-2024.')
            continue
        if date > datetime.now():
            return date
        print('Дедлайн истек! Введите другую дату.')

def note_function(notes_):
    print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
    while True:
        note_ = {
            'name': input_check('имя пользователя'),
            'title': input_check('заголовок заметки'),
            'content': input_check('описание заметки'),
            'status': input_status(('новая', 'в процессе', 'выполнено')),
            'created_date': datetime.now(),
            'issue_date': input_date(7)
        }
        notes_.append(note_)

        ask = None
        while ask not in ['да', 'нет']:
            ask = input('Хотите добавить ещё одну заметку? (да/нет): ')
        if ask == 'нет':
            break
    return notes

notes = []
notes = note_function(notes)

print('Список заметок: ')
for note in notes:
    print('\n\t\tЗаметка №', notes.index(note) + 1)
    print('Имя:', note['name'])
    print('Заголовок:', note['title'])
    print('Описание:', note['content'])
    print('Статус:', note['status'])
    print('Дата создания:', note['created_date'].strftime('%d-%m-%Y'))
    print('Дедлайн:', note['issue_date'].strftime('%d-%m-%Y'))