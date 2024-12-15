from datetime import datetime

username = input('Введите имя пользователя - ')
title1 = input('Введите первый заголовок заметки - ')
title2 = input('Введите второй заголовок заметки - ')
title3 = input('Введите третий заголовок заметки - ')
content = input('Введите описание заметки - ')
status = input('Введите статус заметки - ')
created_date = input('Введите дату создания заметки (дд-мм-гггг) - ')
issue_date = input('Введите дату истечения заметки (дд-мм-гггг) - ')

created_date_obj = datetime.strptime(created_date, "%d-%m-%Y")
issue_date_obj = datetime.strptime(issue_date, "%d-%m-%Y")

title_list = [title1, title2, title3]

print('Имя пользователя:', username)
print('Заголовоки заметки:', title_list)
print('Описание заметки:', content)
print('Статус заметки:', status)
print('Дата создания заметки:', created_date_obj.strftime("%d-%m"))
print('Дата истечения заметки:', issue_date_obj.strftime("%d-%m"))
