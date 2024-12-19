titles = []
max = 10 # максимальное количество заголовков

while len(titles) < max:
    title = input('Введите заголовок (Пустой ввод - завершить): ')
    if title == '':
        if len(titles) == 0:
            print('Нет ни одного зааголовка')
            continue
        else:
            break
    if title in titles:
        print('Такой заголовок уже есть')
    else:
        titles.append(title)

print('Заголовки заметки:')
for title in titles:
    print('-', title)
