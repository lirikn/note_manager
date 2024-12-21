from datetime import datetime

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
        print('Неправельный статус -', status)

def input_date(name):
    while True:
        date = input(f'Введите дату {name} (дд-мм-гггг):')
        try:
            date = datetime.strptime(date, '%d-%m-%Y')
            return date
        except:
            print('Убедитесь, что вводите дату в формате день-месяц-год, например: 10-12-2024.')

notes = []
print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
while True:
    note = {}
    notes.append(note)
    note['name'] = input_check('имя пользователя')
    note['title'] = input_check('заголовок заметки')
    note['content'] = input_check('описание заметки')
    note['status'] = input_status(('новая', 'в процессе', 'выполнено'))
    note['created_date'] = input_date('создания')
    note['issue_date'] = input_date('дедлайна')

    ask = None
    while ask not in ['да', 'нет']:
        ask = input('Хотите добавить ещё одну заметку? (да/нет): ')
    if ask == 'нет':
        break

print('Список заметок: ')
for note in notes:
    print('\n\t\tЗаметка №', notes.index(note) + 1)
    print('Имя:', note['name'])
    print('Заголовок:', note['title'])
    print('Описание:', note['content'])
    print('Статус:', note['status'])
    print('Дата создания:', note['created_date'])
    print('Дедлайн:', note['issue_date'])