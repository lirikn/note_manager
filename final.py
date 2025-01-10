from datetime import datetime

note = {'name': input('Введите имя пользователя - '), 'title': []}
note['title'].append(input('Введите первый заголовок заметки - '))
note['title'].append(input('Введите второй заголовок заметки - '))
note['title'].append(input('Введите третий заголовок заметки - '))
note['content'] = input('Введите описание заметки - ')
note['status'] = input('Введите статус заметки - ')
note['created_date'] = datetime.strptime(input('Введите дату создания заметки (дд-мм-гггг) - '), "%d-%m-%Y")
note['issue_date'] = datetime.strptime(input('Введите дату истечения заметки (дд-мм-гггг) - '), "%d-%m-%Y")

print('Имя пользователя:', note['name'])
print('Заголовки заметки:', note['title'][0], note['title'][1], note['title'][2])
print('Описание заметки:', note['content'])
print('Статус заметки:', note['status'])
print('Дата создания заметки:', note['created_date'].strftime("%d-%m"))
print('Дата истечения заметки:', note['issue_date'].strftime("%d-%m"))

print(note)
