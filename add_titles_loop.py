# Реализация цикла для добавления заголовков.
titles = []
max_ = 10 # максимальное количество заголовков

while len(titles) < max_:
    title = input('Введите заголовок (Пустой ввод - завершить): ')
    if title == '':
        if len(titles) == 0:
            print('Нет ни одного заголовка')
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
