# Пример функции для создания новой заметки и возврата словаря.
from datetime import datetime, timedelta

def input_check(text):
    while True:
        ret = input(f'Введите {text}: ')
        if ret:
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
        if not date:
            return default
        try:
            date = datetime.strptime(date, '%d-%m-%Y')
        except:
            print('Убедитесь, что вводите дату в формате день-месяц-год, например: 10-12-2024.')
            continue
        if date > datetime.now():
            return date
        print('Дедлайн истек! Введите другую дату.')

def create_note():
    return {
        'username': input_check('имя пользователя'),
        'title': input_check('заголовок заметки'),
        'content': input_check('описание заметки'),
        'status': input_status(('новая', 'в процессе', 'выполнено')),
        'created_date': datetime.now().strftime('%d-%m-%Y'),
        'issue_date': input_date(7).strftime('%d-%m-%Y')
    }

if __name__ == "__main__":
    notes = []
    print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
    while True:
        note = create_note()
        notes.append(note)

        ask = None
        while ask not in ('да', 'нет'):
            ask = input('Хотите добавить ещё одну заметку? (да/нет): ')
        if ask == 'нет':
            break

    print('Список заметок: ')
    for note in notes:
        print('\n\t\tЗаметка №', notes.index(note) + 1)
        print('Имя:', note['username'])
        print('Заголовок:', note['title'])
        print('Описание:', note['content'])
        print('Статус:', note['status'])
        print('Дата создания:', note['created_date'])
        print('Дедлайн:', note['issue_date'])