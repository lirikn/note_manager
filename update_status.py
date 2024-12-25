# Проверка и обновление статуса заметки.
stats = ("выполнено", "в процессе", "отложено")

status = stats[1]
print('Текущий статус заметки:', status)

print('Выберите новый статус заметки:')
while True:
    for s in stats:
        print(f'{stats.index(s)+1}. {s}')
    s = input()
    if s.isdigit():
        num = int(s)
        if num > 0 and num <= len(stats):
            status = stats[num-1]
            break
    else:
        if s in stats:
            status = s
            break
    print('Непрвильный ввод')

print('Статус заметки успешно обновлён на:', status)
