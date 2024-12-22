notes = [{'name': 'Алексей',
          'title': 'Список покупок',
          'content': 'Купить продукты на неделю'},
         {'name': 'Мария',
          'title': 'Учеба',
          'content': 'Подготовиться к экзамену'}]

def output_notes(text):
    print(text)
    for note in notes:
        print(f'{notes.index(note)+1}. Имя:', note['name'])
        print('   Заголовок:', note['title'])
        print('   Описание:', note['content'])

def input_check(text):
    while True:
        ret = input(f'Введите {text}: ')
        if ret != '':
            return ret
        print('Ввод не может быть пустым')

output_notes('Текущие заметки:')
deleted = False
req = input_check('имя пользователя или заголовок для удаления заметки')
for note in notes:
    if req.lower() == note['title'].lower() or req == note['name']:
        notes.remove(note)
        deleted = True
if deleted:
    output_notes('Успешно удалено. Остались следующие заметки:')
else:
    print('Заметок с таким именем пользователя или заголовком не найдено.')
