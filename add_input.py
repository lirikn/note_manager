from datetime import datetime

username = input('Введите имя пользователя - ')
title = input('Введите заголовок заметки - ')
content = input('Введите описание заметки - ')
status = input('Введите статус заметки - ')
created_date = input('Введите дату создания заметки (дд-мм-гггг) - ')
issue_date = input('Введите дату истечения заметки (дд-мм-гггг) - ')

created_date_obj = datetime.strptime(created_date, "%d-%m-%Y")
issue_date_obj = datetime.strptime(issue_date, "%d-%m-%Y")



print('Имя пользователя:', username)
print('Заголовок заметки:', title)
print('Описание заметки:', content)
print('Статус заметки:', status)
print('Дата создания заметки:', created_date_obj.strftime("%d-%m"))
print('Дата истечения заметки:', issue_date_obj.strftime("%d-%m"))
